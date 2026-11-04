@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ==========================================================
echo   BOC KHOI LUONG TONG HOP: THOAT NUOC + GIAO THONG
echo   (Sua duong dan DXF / CSV / OUT trong file:
echo    python\boc-tong-hop-thoat-nuoc-giao-thong.py  truoc khi chay)
echo ==========================================================
python -I "python\boc-tong-hop-thoat-nuoc-giao-thong.py"
echo.
pause
