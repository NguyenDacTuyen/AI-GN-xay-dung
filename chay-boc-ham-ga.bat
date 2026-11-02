@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ==========================================================
echo   BOC KHOI LUONG DAO DAP HAM GA TU BAN VE TRAC DOC
echo   (Sua duong dan DXF / MAU / OUT trong file:
echo    python\boc-ham-ga-thoat-nuoc.py  truoc khi chay)
echo ==========================================================
python -I "python\boc-ham-ga-thoat-nuoc.py"
echo.
pause
