@echo off
rem ============================================================================
rem  CHAY DU TOAN - chay lan luot 3 chuong trinh cho mot du an:
rem    1. chuyen_f1_ve_mau.py    : file F1 xuat ra -> du toan hang muc theo mau cong ty
rem    2. tong_hop_du_toan.py    : cac hang muc -> bang tong hop du toan
rem    3. thuyet_minh_du_toan.py : bang tong hop -> thuyet minh du toan (Word)
rem
rem  CACH DUNG:
rem    - Chep file nay vao THU MUC DU AN, cung cho voi file khai-bao-du-an.ini
rem      va cac file Excel xuat tu F1.
rem    - Nhap dup vao file nay. Ket qua ghi vao chinh thu muc du an.
rem    - Chuong trinh khong ghi de file ket qua da co: muon lap lai thi xoa
rem      (hoac doi ten) file ket qua cu truoc.
rem
rem  Cac chuong trinh va file mau nam trong thu muc AI_Cad_K1 (dong "CT" ben duoi).
rem  Doi may hoac doi cho thu muc AI_Cad_K1 thi sua dong "CT".
rem ============================================================================

set "CT=D:\SOFTWARE\15. AI\15.4 Claude\15.4.1 Lop hoc Cesslobal\02. AI_Xay Dung\AI_Cad_K1\python"
set "KB=khai-bao-du-an.ini"

rem Hien dung tieng Viet co dau trong thong bao cua chuong trinh
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
rem Tat cac canh bao ky thuat (tieng Anh) cua thu vien doc Excel, khong anh huong ket qua
set PYTHONWARNINGS=ignore

rem Dung o thu muc chua file .bat nay (thu muc du an)
cd /d "%~dp0"
echo Thu muc du an: %CD%
echo.

if not exist "%KB%" (
    echo [LOI] Khong thay file %KB% trong thu muc du an.
    echo       Chep file mau "%CT%\mau-khai-bao-du-an.ini" vao day,
    echo       doi ten thanh %KB% roi dien thong tin.
    goto ket_thuc
)
if not exist "%CT%\chuyen_f1_ve_mau.py" (
    echo [LOI] Khong thay chuong trinh trong thu muc:
    echo       %CT%
    echo       Sua dong "CT" trong file .bat nay cho dung cho thu muc AI_Cad_K1\python.
    goto ket_thuc
)

echo ===== BUOC 1/3: Lap du toan hang muc theo mau cong ty =====
python "%CT%\chuyen_f1_ve_mau.py" "%KB%"
if errorlevel 1 goto loi
echo.

echo ===== BUOC 2/3: Lap bang tong hop du toan =====
python "%CT%\tong_hop_du_toan.py" "%KB%"
if errorlevel 1 goto loi
echo.

echo ===== BUOC 3/3: Viet thuyet minh du toan =====
python "%CT%\thuyet_minh_du_toan.py" "%KB%"
if errorlevel 1 goto loi
echo.

echo ===== XONG CA 3 BUOC. Ket qua nam trong thu muc du an. =====
goto ket_thuc

:loi
echo.
echo [DUNG LAI] Buoc vua roi bao loi (doc dong thong bao phia tren).
echo Thuong gap: file ket qua da co (xoa hoac doi ten file cu), file dang mo trong
echo Excel/Word (dong lai), ten file F1 trong file khai bao go sai.

:ket_thuc
echo.
pause
