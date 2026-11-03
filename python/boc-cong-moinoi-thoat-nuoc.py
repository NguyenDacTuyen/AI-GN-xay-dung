# -*- coding: utf-8 -*-
"""
BÓC KHỐI LƯỢNG ĐÀO ĐẮP CỐNG + MỐI NỐI/GỐI CỐNG TỪ TRẮC DỌC THOÁT NƯỚC
- Đọc ĐỘNG từ file DXF (bao nhiêu đoạn cũng được), mỗi đoạn ghép 2 giếng đầu/sau.
- Lấy file Excel MẪU làm nền -> giữ nguyên 100% định dạng (in ngang, cột, số lẻ, font, canh lề, ô gộp).
- Các cột kỹ thuật TRA bảng "DINH HINH CONG" trong file mẫu (VLOOKUP theo đường kính).
- Xuất ra FILE KẾT QUẢ RIÊNG; KHÔNG ghi đè file mẫu.

Cần: Python + ezdxf + openpyxl  (cài 1 lần: pip install ezdxf openpyxl)
Chạy: sửa phần CẤU HÌNH rồi chạy (hoặc nhấp đúp chay-boc-cong-moinoi.bat).

Điều kiện: file mẫu phải có sẵn 3 sheet: "Thong so", "Dao dap cong", "Moi noi-goi cong",
"DINH HINH CONG". Bản vẽ dùng đúng bộ layer trắc dọc (sửa ở CẤU HÌNH nếu khác).
"""
import ezdxf, openpyxl, copy, re, os, sys
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, Alignment, Border, Side

# ================== CẤU HÌNH (sửa ở đây) ==================
DXF = r"F:/demo/Acad_BD_TD_TN Nhi Binh 5.dxf"
MAU = r"F:/demo/mau hamga.xlsx"
OUT = r"D:/SOFTWARE/15. AI/15.4 Claude/15.4.1 Lop hoc Cesslobal/02. AI_Xay Dung/AI_Cad_K1/ket-qua/KL-dao-dap-cong-moinoi_CONGTRINHMOI.xlsx"
LAYER_TU_NHIEN = "TP33_TD_Caodotunhien"
LAYER_DAY_CONG = "TP115_TD_Caodo_daycong_TR"
LAYER_NAP      = "TP45_TD_Caodo_dinhGiengthu"
LAYER_DUONGKINH= "TP118_TD_Khoangcachgiengthu"   # chua text duong kinh %%cNNN
LAYER_CHIEUDAI = "TP113_TD_Dodoccong"            # cot do doc - chieu dai cong (so khong co %)
# =========================================================

DSTART=6; TS="'Thong so'"; DH="'DINH HINH CONG'!$B$4:$R$13"
# cot trong DH: 2=catlotcao 3=btlotcao 5=rongcatlot/tdcat? (xem file tra) -> idx VLOOKUP:
# 2 catlot cao,3 btlot cao,5 td cat lot,6 td bt lot,7 vua moi,8 cao VK lot,9 chu vi VK chen,
# 11 BT 1 goi,13 B day phui,14 td cong,16 so cu goi,17 Dngoai

def main():
    doc=ezdxf.readfile(DXF);msp=doc.modelspace()
    have={l.dxf.name for l in doc.layers}
    for L in (LAYER_TU_NHIEN,LAYER_DAY_CONG,LAYER_NAP,LAYER_DUONGKINH,LAYER_CHIEUDAI):
        if L not in have:
            print("!! Khong thay layer:",L);
            print("   Layer co 'cong/gieng/caodo':")
            for x in sorted(have):
                if any(k in x.lower() for k in ("cong","ieng","caodo","day","doc")): print("    -",x)
            sys.exit("=> Sua ten layer trong CAU HINH roi chay lai.")
    def txt(l): return [(e.dxf.insert.x,e.dxf.text.strip()) for e in msp if e.dxf.layer==l and e.dxftype()=="TEXT"]
    def nums(l):
        r=[]
        for x,t in txt(l):
            try:r.append((x,float(t.replace(",","."))))
            except:pass
        return r
    def nr(x,a):
        b=None;bd=1e18
        for xx,v in a:
            if abs(x-xx)<bd:bd=abs(x-xx);b=v
        return b
    md=nums(LAYER_TU_NHIEN);dc=nums(LAYER_DAY_CONG);nap=sorted(nums(LAYER_NAP))
    dia=[]
    for x,t in txt(LAYER_DUONGKINH):
        m=re.match(r'%%[cC](\d+)',t)
        if m:dia.append((x,int(m.group(1))))
    lens=sorted((x,float(t.replace(",","."))) for x,t in txt(LAYER_CHIEUDAI)
                if not t.endswith("%") and re.match(r'^[\d\.,]+$',t))
    G=[dict(x=x,ten="HG%02d"%(i+1),nap=h,tn=nr(x,md),day=nr(x,dc)) for i,(x,h) in enumerate(nap)]
    Gx=[g["x"] for g in G]
    def bracket(xm):
        for k in range(len(Gx)-1):
            if Gx[k]<=xm<=Gx[k+1]:return k,k+1
        return (0,1) if xm<Gx[0] else (len(Gx)-2,len(Gx)-1)
    def split(C):
        n4=int(C//4);r=C-4*n4;n3=n2=n1=0
        if r<0.5:pass
        elif r<1.5:n1=1
        elif r<2.5:n2=1
        elif r<3.5:n3=1
        else:n4+=1
        return n4,n3,n2,n1
    doan=[]
    for xm,L in lens:
        j,k=bracket(xm);O=nr(xm,dia) if nr(xm,dia) in(400,600,800) else 600
        doan.append(dict(dau=G[j],sau=G[k],L=L,O=O))
    N=len(doan)

    wb=openpyxl.load_workbook(MAU)
    thin=Side(style="thin");BOX=Border(thin,thin,thin,thin)
    TNR=Font(name="Times New Roman",size=11);TNRB=Font(name="Times New Roman",size=11,bold=True)
    CEN=Alignment("center","center",wrap_text=True)
    def fit(ws,ncol,base):
        extra=N-base;old=DSTART+base
        def cps(s,d):
            ws.row_dimensions[d].height=ws.row_dimensions[s].height
            for c in range(1,ncol+1):
                a=ws.cell(s,c);b=ws.cell(d,c)
                b.font=copy.copy(a.font);b.fill=copy.copy(a.fill);b.border=copy.copy(a.border)
                b.alignment=copy.copy(a.alignment);b.number_format=a.number_format
        if extra>0:
            ws.insert_rows(old,extra)
            for rr in range(old,old+extra):cps(DSTART,rr)
        elif extra<0:
            ws.delete_rows(DSTART+N,-extra)
        return DSTART+N
    def norm(ws,ncol,r2):
        for r in range(DSTART,r2+1):
            for c in range(1,ncol+1):
                cell=ws.cell(r,c)
                try:
                    cell.font=TNRB if r==r2 else TNR;cell.alignment=CEN;cell.border=BOX
                except (AttributeError,TypeError):pass
    def VL(dk,idx): return f"VLOOKUP({dk},{DH},{idx},FALSE)"

    # --- Dao dap cong (20 cot) ---
    ws=wb["Dao dap cong"];tong=fit(ws,20,27)
    for i,d in enumerate(doan):
        r=DSTART+i;a=d["dau"];b=d["sau"];H=f"H{r}/1000"
        ws.cell(r,1).value=i+1;ws.cell(r,2).value=a["ten"];ws.cell(r,3).value=b["ten"];ws.cell(r,4).value=round(d["L"],2)
        ws.cell(r,5).value=round(a["nap"],2);ws.cell(r,6).value=round(b["nap"],2);ws.cell(r,7).value=f"=(E{r}+F{r})/2"
        ws.cell(r,8).value=d["O"];ws.cell(r,8).number_format="\\Ø0"
        ws.cell(r,9).value=round(a["day"],2);ws.cell(r,10).value=round(b["day"],2);ws.cell(r,11).value=f"=(I{r}+J{r})/2"
        ws.cell(r,12).value=round(a["tn"],2);ws.cell(r,13).value=round(b["tn"],2)
        ws.cell(r,14).value=f"={VL(H,13)}"
        ws.cell(r,15).value=f"=K{r}-({VL(H,17)}-H{r}/1000)/2-{VL(H,2)}-{VL(H,3)}"
        ws.cell(r,16).value=f"=(L{r}+M{r})/2-O{r}"
        ws.cell(r,17).value=f"=N{r}+0.5*P{r}"
        ws.cell(r,18).value=f"=P{r}*Q{r}*D{r}"
        ws.cell(r,19).value=f"=({VL(H,14)}+{VL(H,6)}+{VL(H,5)})*D{r}"
        ws.cell(r,20).value=f"=R{r}-S{r}"
    ws.cell(tong,1).value="TỔNG"
    for c in (4,18,19,20):
        cl=get_column_letter(c);ws.cell(tong,c).value=f"=SUM({cl}{DSTART}:{cl}{tong-1})"
    norm(ws,20,tong)

    # --- Moi noi-goi cong (17 cot) ---
    ws2=wb["Moi noi-goi cong"];tong2=fit(ws2,17,27)
    for i,d in enumerate(doan):
        r=DSTART+i;O=d["O"];C=d["L"];n4,n3,n2,n1=split(C);B=f"B{r}/1000"
        ws2.cell(r,1).value=i+1;ws2.cell(r,2).value=O;ws2.cell(r,3).value=round(C,2)
        ws2.cell(r,4).value=n4;ws2.cell(r,5).value=n3;ws2.cell(r,6).value=n2;ws2.cell(r,7).value=n1
        ws2.cell(r,8).value=f"=MAX(D{r}+E{r}+F{r}+G{r}-1,0)"
        ws2.cell(r,9).value=f"=2*(D{r}+E{r}+F{r}+G{r})"
        ws2.cell(r,10).value=f"=H{r}*{VL(B,7)}"
        ws2.cell(r,11).value=f"=H{r}*{VL(B,9)}"
        ws2.cell(r,12).value=f"=I{r}*{VL(B,11)}"
        ws2.cell(r,13).value=f"=D{r}*4+E{r}*3+F{r}*2+G{r}"
        ws2.cell(r,14).value=f"={VL(B,5)}*C{r}"
        ws2.cell(r,15).value=f"=2*{VL(B,8)}*C{r}"
        ws2.cell(r,16).value=f"={VL(B,6)}*C{r}"
        ws2.cell(r,17).value=f"=I{r}*{VL(B,16)}*{TS}!$B$17"
    ws2.cell(tong2,1).value="TỔNG"
    for c in range(4,18):
        cl=get_column_letter(c);ws2.cell(tong2,c).value=f"=SUM({cl}{DSTART}:{cl}{tong2-1})"
    norm(ws2,17,tong2)

    os.makedirs(os.path.dirname(OUT),exist_ok=True)
    try:
        wb.save(OUT);print("XONG. So doan =",N,"| File:",OUT)
    except PermissionError:
        print("!! File dang mo trong Excel. Dong roi chay lai, hoac doi ten OUT.")

if __name__=="__main__":
    main()
