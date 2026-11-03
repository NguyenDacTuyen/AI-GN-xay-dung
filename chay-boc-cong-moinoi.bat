@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ==========================================================
echo   BOC KHOI LUONG DAO DAP CONG + MOI NOI/GOI CONG
echo   (Sua duong dan DXF / MAU / OUT + ten layer trong:
echo    python\boc-cong-moinoi-thoat-nuoc.py  truoc khi chay)
echo ==========================================================
python -I "python\boc-cong-moinoi-thoat-nuoc.py"
echo.
pause
