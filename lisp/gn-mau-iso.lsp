;;; ==========================================================================
;;; gn-mau-iso.lsp - Mau trinh bay ghi chu, so hieu thep, cao do (Cong ty Gia Nguyen)
;;; Lenh: GNMAU - Them vao ban ve dang mo:
;;;   - Block GN_SoHieuThep   : vong tron so hieu o cuoi duong ngang (dau duong dan ben trai)
;;;   - Block GN_SoHieuThep_T : ban doi xung (vong tron ben trai, dung khi ghi chu nam ben trai)
;;;   - Block GN_GhiChu       : chu ghi chu nam tren duong ngang (ghi chu ve ben phai)
;;;   - Block GN_GhiChu_T     : ban doi xung (ghi chu ve ben trai)
;;;   - Block GN_CaoDo        : ky hieu cao do mau cong ty
;;;   - 8 kieu Multileader "TP_1-xx GhiChu" va 8 kieu "TP_1-xx SoHieuThep"
;;;     cho cac ty le 1/10, 1/25, 1/50, 1/100, 1/150, 1/200, 1/250, 1/500
;;; Lenh: GNGC  - Ve ghi chu chu (vd DA 1x2 M300), tu canh do dai duong ngang theo chu
;;; Lenh: GNGCF - Canh lai ghi chu chu va so hieu thep da ve (sau khi sua chu hoac keo sang ben kia)
;;; Duong dan, mui ten, vong tron: layer 42.Tp_M learder. Chu (ca ghi chu va chu thep): layer 6.TP_Tex tNote.
;;; Kich thuoc cac block ve theo KICH THUOC TREN GIAY IN (mm).
;;; Khi chen block vao Model thi go he so = mau so ty le (1/50 -> 50).
;;; Mui ten = 2 x ty le (1/50 -> 100), theo quy dinh anh Tuyen 20/10/2026.
;;; Chay lai lenh nhieu lan khong sao: block da co thi giu nguyen, kieu Multileader thi cap nhat lai.
;;; ==========================================================================

(vl-load-com)

;;; Ve 1 duong thang trong dinh nghia block
(defun GNM-L (lay x1 y1 x2 y2)
  (entmake (list '(0 . "LINE") (cons 8 lay) (list 10 x1 y1 0.0) (list 11 x2 y2 0.0))))

;;; Ve 1 o chu sua duoc (Attribute) trong dinh nghia block
;;; h = canh ngang (0 trai, 1 giua, 2 phai), v = canh dung (1 day, 2 giua)
(defun GNM-ATT (tag prompt def x y h v)
  (entmake (list '(0 . "ATTDEF") '(8 . "6.TP_Tex tNote") '(7 . "29.TP_1-1 Note")
                 (list 10 x y 0.0) (list 11 x y 0.0) '(40 . 2.5)
                 (cons 1 def) (cons 3 prompt) (cons 2 tag) '(70 . 0)
                 (cons 72 h) (cons 74 v))))

;;; Block so hieu thep. dir = 1: vong tron ben phai diem chen; dir = -1: ben trai.
;;; Diem chen nam o mep vong tron, la cho duong ngang cua Multileader cham vao.
(defun GNM-BLK-THEP (name dir / xc)
  (if (not (tblsearch "BLOCK" name))
    (progn
      (setq xc (* dir 2.5))
      (entmake (list '(0 . "BLOCK") (cons 2 name) '(70 . 2) '(10 0.0 0.0 0.0)))
      (entmake (list '(0 . "CIRCLE") '(8 . "42.Tp_M learder") (list 10 xc 0.0 0.0) '(40 . 2.5)))
      (GNM-ATT "SO_HIEU" "So hieu thep" "1" xc 0.0 1 2)
      ;; chu thep nam tren duong ngang, cach vong tron 1 mm, cach duong ngang 0,8 mm
      (if (> dir 0)
        (GNM-ATT "THEP" "Chu thep (vd 2%%c14)" "2%%c14" -1.0 0.8 2 1)
        (GNM-ATT "THEP" "Chu thep (vd 2%%c14)" "2%%c14" 1.0 0.8 0 1))
      (entmake '((0 . "ENDBLK"))))))

;;; Block ghi chu chu. Chi co 1 o chu nhieu dong (xuong dong bang \P), layer 6.TP_Tex tNote.
;;; Diem chen la dau cuoi duong ngang. dir = 1: chu nam ben trai diem chen (ghi chu ve ben phai);
;;; dir = -1: chu nam ben phai diem chen (ghi chu ve ben trai). Chu cach duong ngang 0,8 mm.
(defun GNM-BLK-GHICHU (name dir / blk a)
  (if (not (tblsearch "BLOCK" name))
    (progn
      (setq blk (vla-add (vla-get-blocks (vla-get-activedocument (vlax-get-acad-object)))
                         (vlax-3d-point 0.0 0.0 0.0) name))
      (setq a (vla-AddAttribute blk 2.5 acAttributeModeNormal "Noi dung ghi chu"
                                (vlax-3d-point (* dir -1.0) 0.8 0.0) "NOI_DUNG" "GHI CH\U+00DA"))
      (vla-put-Layer a "6.TP_Tex tNote")
      (vla-put-StyleName a "29.TP_1-1 Note")
      (vla-put-Height a 2.5)
      (vla-put-MTextAttribute a :vlax-true)
      (vla-put-Alignment a (if (> dir 0) acAlignmentBottomRight acAlignmentBottomLeft))
      (vla-put-TextAlignmentPoint a (vlax-3d-point (* dir -1.0) 0.8 0.0)))))

;;; Block cao do: diem chen la dinh tam giac (dung cao do can ghi)
(defun GNM-BLK-CAODO ()
  (if (not (tblsearch "BLOCK" "GN_CaoDo"))
    (progn
      (entmake '((0 . "BLOCK") (2 . "GN_CaoDo") (70 . 2) (10 0.0 0.0 0.0)))
      ;; tam giac nguoc rong 3, cao 1,5; nua trai to dac
      (GNM-L "1.Tp_dim" -1.5 1.5 1.5 1.5)
      (GNM-L "1.Tp_dim" -1.5 1.5 0.0 0.0)
      (GNM-L "1.Tp_dim" 1.5 1.5 0.0 0.0)
      (entmake '((0 . "SOLID") (8 . "3.TP_Hatch") (10 -1.5 1.5 0.0) (11 0.0 1.5 0.0)
                 (12 0.0 0.0 0.0) (13 0.0 0.0 0.0)))
      ;; duong ngang tai cao do, duong dung cao 7,5
      (GNM-L "1.Tp_dim" -1.5 0.0 2.6 0.0)
      (GNM-L "1.Tp_dim" 0.0 0.0 0.0 7.5)
      ;; duong do chu, cach dinh 3,44
      (GNM-L "1.Tp_dim" -2.2 3.44 9.0 3.44)
      (GNM-ATT "CAO_DO" "Cao do (vd %%p0.000, -1.500)" "%%p0.000" 1.0 4.24 0 1)
      (entmake '((0 . "ENDBLK"))))))

;;; Dat mau ByLayer cho 1 thuoc tinh mau cua kieu Multileader
(defun GNM-BYLAYER (obj prop / c)
  (setq c (vlax-get-property obj prop))
  (vla-put-ColorIndex c 256)
  (vlax-put-property obj prop c))

;;; Tao (hoac cap nhat) 1 kieu Multileader, noi dung la block blk, phong theo ty le k
(defun GNM-MLS (name k blk / dict obj)
  (setq dict (vla-item (vla-get-dictionaries (vla-get-activedocument (vlax-get-acad-object)))
                       "ACAD_MLEADERSTYLE"))
  (setq obj (vl-catch-all-apply 'vla-item (list dict name)))
  (if (vl-catch-all-error-p obj)
    (setq obj (vla-addobject dict name "AcDbMLeaderStyle")))
  ;; duong dan: thang, 2 diem, mau va net theo layer
  (vla-put-LeaderLineType obj 1)
  (vla-put-MaxLeaderSegmentsPoints obj 2)
  (GNM-BYLAYER obj 'LeaderLineColor)
  (vla-put-LeaderLineWeight obj -1)
  ;; mui ten dac (mac dinh cua kieu moi la Closed filled), cao = 2 x ty le
  (vla-put-ArrowSize obj (* 2.0 k))
  (vla-put-ScaleFactor obj 1.0)
  (vla-put-EnableLanding obj :vlax-true)
  (vla-put-EnableDogleg obj :vlax-true)
  ;; noi dung la block, phong theo ty le; chu trong block nam o layer 6.TP_Tex tNote
  (vla-put-ContentType obj 1)
  (vla-put-Block obj blk)
  (vla-put-BlockConnectionType obj 1)
  (vla-put-EnableBlockScale obj :vlax-true)
  (vla-put-BlockScale obj (float k))
  (GNM-BYLAYER obj 'BlockColor)
  ;; duong ngang mac dinh 15 mm tren giay; lenh GNGCF canh lai theo do dai chu
  (vla-put-DoglegLength obj (* 15.0 k))
  name)

(defun c:GNMAU ( / r)
  (GNM-BLK-THEP "GN_SoHieuThep" 1)
  (GNM-BLK-THEP "GN_SoHieuThep_T" -1)
  (GNM-BLK-GHICHU "GN_GhiChu" 1)
  (GNM-BLK-GHICHU "GN_GhiChu_T" -1)
  (GNM-BLK-CAODO)
  (foreach k '(10 25 50 100 150 200 250 500)
    (GNM-MLS (strcat "TP_1-" (itoa k) " GhiChu") k "GN_GhiChu")
    (GNM-MLS (strcat "TP_1-" (itoa k) " SoHieuThep") k "GN_SoHieuThep"))
  (princ "\nGNMAU: da them 5 block va 16 kieu Multileader.")
  (princ))

;;; ---------------------------------------------------------------- GNGC, GNGCF

;;; Ma so (ObjectID) cua o chu tag trong block blk
(defun GNM-ATTID (blk tag / id)
  (vlax-for o (vla-item (vla-get-blocks (vla-get-activedocument (vlax-get-acad-object))) blk)
    (if (and (= (vla-get-ObjectName o) "AcDbAttributeDefinition")
             (= (strcase (vla-get-TagString o)) tag))
      (setq id (vla-get-ObjectID o))))
  id)

;;; Doc noi dung o chu tag cua ghi chu ml (block blk).
;;; Doc thang du lieu goc (ma 302 ngay sau o chu), vi vla-GetBlockAttributeValue doi dau xuong dong \P thanh dau cach.
(defun GNM-DOCATT (ml blk tag / en ed)
  (vlax-for o (vla-item (vla-get-blocks (vla-get-activedocument (vlax-get-acad-object))) blk)
    (if (and (= (vla-get-ObjectName o) "AcDbAttributeDefinition")
             (= (strcase (vla-get-TagString o)) tag))
      (setq en (vlax-vla-object->ename o))))
  (setq ed (member (cons 330 en) (entget (vlax-vla-object->ename ml))))
  (if (assoc 302 ed)
    (cdr (assoc 302 ed))
    (vla-GetBlockAttributeValue ml (GNM-ATTID blk tag))))

;;; Chieu rong 1 dong chu tren giay (mm), chu cao 2,5
(defun GNM-RONG1 (ln / tb)
  (if (= ln "")
    0.0
    (progn
      (setq tb (textbox (list (cons 1 ln) (cons 7 "29.TP_1-1 Note") (cons 40 2.5))))
      (- (car (cadr tb)) (car (car tb))))))

;;; Chieu rong dong dai nhat (cac dong cach nhau bang \P)
(defun GNM-RONG (s / w i)
  (setq w 0.0)
  (while (setq i (vl-string-search "\\P" s))
    (setq w (max w (GNM-RONG1 (substr s 1 i)))
          s (substr s (+ i 3))))
  (max w (GNM-RONG1 s)))

;;; Canh lai 1 ghi chu: chon block dung phia, do dai duong ngang = chu + le, giu nguyen 2 diem da chon
(defun GNM-CANH (ml / v n ax ay lx ly cu lft k tags chinh le moi vals)
  (setq v  (vlax-invoke ml 'GetLeaderLineVertices 0)
        n  (length v)
        ax (nth 0 v) ay (nth 1 v)
        lx (nth (- n 3) v) ly (nth (- n 2) v)
        cu (vl-catch-all-apply 'vla-get-ContentBlockName (list ml))
        ;; giu nguyen huong duong ngang dang co (am = ve ben trai)
        lft (< (car (vlax-invoke ml 'GetDoglegDirection 0)) 0.0)
        k  (vla-get-BlockScale ml))
  ;; ghi chu khong phai block (chu thuong) thi bo qua
  (if (or (vl-catch-all-error-p cu) (null cu)) (setq cu ""))
  (cond ((wcmatch (strcase cu) "GN_GHICHU*")
         (setq tags '("NOI_DUNG") chinh "NOI_DUNG" le 2.0 moi (if lft "GN_GhiChu_T" "GN_GhiChu")))
        ((wcmatch (strcase cu) "GN_SOHIEUTHEP*")
         (setq tags '("SO_HIEU" "THEP") chinh "THEP" le 3.0 moi (if lft "GN_SoHieuThep_T" "GN_SoHieuThep"))))
  (if tags
    (progn
      ;; doc noi dung truoc, vi doi block thi noi dung tro ve mac dinh
      (setq vals (mapcar '(lambda (tg) (GNM-DOCATT ml cu tg)) tags))
      (if (/= (strcase cu) (strcase moi))
        (progn
          (vla-put-ContentBlockName ml moi)
          (mapcar '(lambda (tg s) (vla-SetBlockAttributeValue ml (GNM-ATTID moi tg) s)) tags vals)))
      (vla-put-DoglegLength ml (* k (+ (GNM-RONG (nth (vl-position chinh tags) vals)) le)))
      (vla-SetDoglegDirection ml 0 (vlax-3d-point (if lft -1.0 1.0) 0.0 0.0))
      (GNM-DATLAI ml ax ay lx ly)
      T)))

;;; Doi huong / do dai duong ngang lam lech vi tri: doi ca ghi chu ve dung diem gay (lx ly),
;;; roi dat lai duong dan tu mui ten (ax ay)
(defun GNM-DATLAI (ml ax ay lx ly / v n)
  (setq v (vlax-invoke ml 'GetLeaderLineVertices 0) n (length v))
  (vla-Move ml (vlax-3d-point (nth (- n 3) v) (nth (- n 2) v) 0.0) (vlax-3d-point lx ly 0.0))
  (vlax-invoke ml 'SetLeaderLineVertices 0 (mapcar 'float (list ax ay 0.0 lx ly 0.0))))

;;; Tao 1 ghi chu chu: mui ten (ax ay), diem gay (lx ly), ty le 1/k, noi dung s (xuong dong: \P)
(defun GNM-GHICHU (ax ay lx ly k s / ms ml)
  (setq ms (vla-get-modelspace (vla-get-activedocument (vlax-get-acad-object)))
        ml (vlax-invoke ms 'AddMLeader (mapcar 'float (list ax ay 0 lx ly 0)) 0))
  (vla-put-Layer ml "42.Tp_M learder")
  (vla-put-StyleName ml (strcat "TP_1-" (itoa k) " GhiChu"))
  (vla-put-ContentType ml 1)
  (vla-put-ContentBlockName ml "GN_GhiChu")
  (vla-put-BlockScale ml (float k))
  (vla-SetBlockAttributeValue ml (GNM-ATTID "GN_GhiChu" "NOI_DUNG") s)
  ;; diem gay ben nao cua mui ten thi chu nam ben do
  (vla-SetDoglegDirection ml 0 (vlax-3d-point (if (< lx ax) -1.0 1.0) 0.0 0.0))
  (GNM-DATLAI ml ax ay lx ly)
  (GNM-CANH ml)
  ml)

;;; Hoi ty le, mac dinh lay theo kieu Multileader dang dung (TP_1-50 ... -> 50)
(defun GNM-HOI-K (/ st d k)
  (setq st (getvar "CMLEADERSTYLE")
        d  (if (wcmatch st "TP_1-* *") (atoi (substr st 6)) 50))
  (if (not (member d '(10 25 50 100 150 200 250 500))) (setq d 50))
  (initget 6)
  (setq k (getint (strcat "\nTy le ban ve 1/<" (itoa d) ">: ")))
  (if (null k) (setq k d))
  (if (member k '(10 25 50 100 150 200 250 500))
    k
    (progn (princ "\nChi co cac ty le 10, 25, 50, 100, 150, 200, 250, 500.") nil)))

;;; Lenh GNGC: ve ghi chu chu
(defun c:GNGC (/ doc k p1 p2 s ln i)
  (setq doc (vla-get-activedocument (vlax-get-acad-object)))
  (if (not (tblsearch "BLOCK" "GN_GhiChu"))
    (princ "\nBan ve chua co mau ghi chu. Go GNMAU truoc.")
    (if (and (setq k (GNM-HOI-K))
             (setq p1 (getpoint "\nDiem mui ten: "))
             (setq p2 (getpoint p1 "\nDiem gay (diem ben nao thi chu nam ben do): ")))
      (progn
        (setq s "" i 1)
        (while (/= "" (setq ln (getstring T (strcat "\nDong " (itoa i) " (Enter de xong): "))))
          (setq s (if (= s "") ln (strcat s "\\P" ln)) i (1+ i)))
        (if (= s "")
          (princ "\nChua go noi dung, khong ve.")
          (progn
            (vla-StartUndoMark doc)
            (setq p1 (trans p1 1 0) p2 (trans p2 1 0))
            (GNM-GHICHU (car p1) (cadr p1) (car p2) (cadr p2) k s)
            (vla-EndUndoMark doc))))))
  (princ))

;;; Lenh GNGCF: canh lai cac ghi chu da ve
(defun c:GNGCF (/ doc ss i dem)
  (setq doc (vla-get-activedocument (vlax-get-acad-object)))
  (princ "\nChon cac ghi chu (Multileader) can canh lai: ")
  (if (setq ss (ssget '((0 . "MULTILEADER"))))
    (progn
      (vla-StartUndoMark doc)
      (setq i 0 dem 0)
      (repeat (sslength ss)
        (if (GNM-CANH (vlax-ename->vla-object (ssname ss i))) (setq dem (1+ dem)))
        (setq i (1+ i)))
      (vla-EndUndoMark doc)
      (princ (strcat "\nGNGCF: da canh lai " (itoa dem) " ghi chu."))))
  (princ))
