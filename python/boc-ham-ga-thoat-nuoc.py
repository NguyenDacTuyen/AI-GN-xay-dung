# -*- coding: utf-8 -*-
"""
BÓC KHỐI LƯỢNG ĐÀO ĐẮP HẦM GA (GIẾNG THU) TỪ BẢN VẼ TRẮC DỌC THOÁT NƯỚC
- Đọc số liệu ĐỘNG từ file DXF (bao nhiêu giếng cũng được).
- Lấy file Excel MẪU làm nền -> giữ nguyên 100% định dạng (in ngang, lề, hàng, cột, số lẻ...).
- Chỉ thêm/bớt số hàng cho khớp số giếng của công trình, rồi điền số liệu + công thức.

Cần cài sẵn: Python + thư viện ezdxf, openpyxl  (cài 1 lần: pip install ezdxf openpyxl)

CÁCH DÙNG: sửa 3 đường dẫn trong phần CẤU HÌNH bên dưới rồi chạy
(hoặc nhấp đúp file chay-boc-ham-ga.bat).
"""
import ezdxf, openpyxl, copy, os, re, sys
from openpyxl.utils import get_column_letter

# ================== CẤU HÌNH (anh sửa ở đây) ==================
DXF = r"F:/demo/Acad_BD_TD_TN Nhi Binh 5.dxf"   # bản vẽ trắc dọc thoát nước của công trình
MAU = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "template", "du-toan", "thoat-nuoc-giao-thong", "mau-boc-khoi-luong-tong-hop.xlsx")  # file mẫu chuẩn trong template (không sửa file này)
OUT = r"D:/SOFTWARE/15. AI/15.4 Claude/15.4.1 Lop hoc Cesslobal/02. AI_Xay Dung/AI_Cad_K1/ket-qua/KL-dao-dap-ham-ga_CONGTRINHMOI.xlsx"

# Tên LAYER trong bản vẽ (nếu công trình mới đặt tên layer khác thì sửa đúng tên ở đây):
LAYER_CAODO_TU_NHIEN = "TP33_TD_Caodotunhien"        # cao độ mặt đất tự nhiên
LAYER_DAY_CONG       = "TP115_TD_Caodo_daycong_TR"   # cao độ đáy (lòng trong) cống
LAYER_NAP_GIENG      = "TP45_TD_Caodo_dinhGiengthu"  # cao độ đỉnh/nắp giếng (mỗi giếng 1 giá trị)
LAYER_DAY_GIENG      = "TP46_TD_Caodo_daygienhthu"   # cao độ đáy hố ga/giếng
LAYER_DUONGKINH      = "TP118_TD_Khoangcachgiengthu" # chứa text đường kính %%cNNN
# ============================================================

NCOL=17; HROW=5; DSTART=6; BASE_N=30; TS="'Thong so'"

def doc_ban_ve(dxf):
    doc=ezdxf.readfile(dxf); msp=doc.modelspace()
    def check(lay):
        if lay not in [l.dxf.name for l in doc.layers]:
            print("!! Khong tim thay layer:",lay)
            print("   Cac layer co trong ban ve (loc 'gieng/cong/caodo'):")
            for l in sorted(x.dxf.name for x in doc.layers):
                if any(k in l.lower() for k in ("ieng","cong","caodo","day")): print("    -",l)
            sys.exit("=> Sua lai ten layer trong phan CAU HINH roi chay lai.")
    for L in (LAYER_CAODO_TU_NHIEN,LAYER_DAY_CONG,LAYER_NAP_GIENG,LAYER_DAY_GIENG,LAYER_DUONGKINH): check(L)
    def nums(l):
        r=[]
        for e in msp:
            if e.dxf.layer==l and e.dxftype()=="TEXT":
                try: r.append((e.dxf.insert.x,float(e.dxf.text.strip().replace(",","."))))
                except: pass
        return r
    dia=[]
    for e in msp:
        if e.dxf.layer==LAYER_DUONGKINH and e.dxftype()=="TEXT":
            m=re.match(r'%%[cC](\d+)',e.dxf.text.strip())
            if m: dia.append((e.dxf.insert.x,int(m.group(1))))
    def nr(x,a):
        b=None;bd=1e18
        for xx,v in a:
            if abs(x-xx)<bd: bd=abs(x-xx);b=v
        return b
    md=nums(LAYER_CAODO_TU_NHIEN);dc=nums(LAYER_DAY_CONG);dg=nums(LAYER_DAY_GIENG)
    nap=sorted(nums(LAYER_NAP_GIENG))
    return [dict(O=(nr(x,dia) if nr(x,dia) in (400,600,800) else 600),
                 nap=h,tn=nr(x,md),dayHG=nr(x,dg),daycong=nr(x,dc)) for x,h in nap]

def main():
    gieng=doc_ban_ve(DXF); N=len(gieng)
    wb=openpyxl.load_workbook(MAU); ws=wb["Dao dap ho ga"]
    # them/bot hang cho khop N (giu dinh dang mau)
    extra=N-BASE_N; old_tong=DSTART+BASE_N
    def copy_row_style(src,dst):
        ws.row_dimensions[dst].height=ws.row_dimensions[src].height
        for c in range(1,NCOL+1):
            s=ws.cell(src,c);d=ws.cell(dst,c)
            d.font=copy.copy(s.font);d.fill=copy.copy(s.fill);d.border=copy.copy(s.border)
            d.alignment=copy.copy(s.alignment);d.number_format=s.number_format
    if extra>0:
        ws.insert_rows(old_tong,extra)
        for rr in range(old_tong,old_tong+extra): copy_row_style(DSTART,rr)
    elif extra<0:
        ws.delete_rows(DSTART+N,-extra)
    tong=DSTART+N
    for i,g in enumerate(gieng):
        r=DSTART+i
        ws.cell(r,1).value=i+1; ws.cell(r,2).value="HG%02d"%(i+1); ws.cell(r,3).value=g["O"]
        ws.cell(r,4).value=round(g["nap"],2)
        ws.cell(r,5).value=round(g["tn"],2) if g["tn"] is not None else None
        ws.cell(r,6).value=round(g["dayHG"],2) if g["dayHG"] is not None else None
        ws.cell(r,7).value=round(g["daycong"],2) if g["daycong"] is not None else None
        ws.cell(r,8).value=f"=IF(C{r}=600,{TS}!$B$11,{TS}!$B$10)"
        ws.cell(r,9).value=f"=H{r}+2*{TS}!$B$12+2*{TS}!$B$19"
        ws.cell(r,10).value=f"=I{r}+2*{TS}!$B$3"
        ws.cell(r,11).value=f"=E{r}-F{r}+{TS}!$B$18+{TS}!$B$14+{TS}!$B$13"
        ws.cell(r,12).value=f"=J{r}^2*K{r}"
        ws.cell(r,13).value=f"={TS}!$B$15*(D{r}-F{r})"
        ws.cell(r,14).value=f"=(D{r}-F{r})/{TS}!$B$20*{TS}!$B$21*{TS}!$B$22"
        ws.cell(r,15).value=f"=(4*H{r}+4*(H{r}+2*{TS}!$B$12))*(D{r}-F{r})"
        ws.cell(r,16).value=f"=((H{r}+2*{TS}!$B$12)^2-H{r}^2)*(D{r}-F{r})"
        ws.cell(r,17).value=f"=J{r}^2"
    ws.cell(tong,1).value="TỔNG"
    for c in range(12,NCOL+1):
        cl=get_column_letter(c); ws.cell(tong,c).value=f"=SUM({cl}{DSTART}:{cl}{tong-1})"
    os.makedirs(os.path.dirname(OUT),exist_ok=True)
    try:
        wb.save(OUT); print("XONG. So gieng =",N,"| File:",OUT)
    except PermissionError:
        print("!! File dang mo trong Excel. Dong file roi chay lai, hoac doi ten OUT.")

if __name__=="__main__":
    main()
