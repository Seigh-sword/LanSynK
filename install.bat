@echo off
title LanSynK Installer

echo ==================================
echo        Installing LanSynK
echo ==================================
echo.

set INSTALL_DIR=C:\Program Files\LanSynK

echo Creating folder...
mkdir "%INSTALL_DIR%"

cd /d "%INSTALL_DIR%"

echo Downloading latest version...

curl -L -o lansynk.zip https://github.com/Seigh-sword/LanSynK/archive/refs/heads/main.zip

echo Extracting...

powershell -command "Expand-Archive -Force lansynk.zip ."

del lansynk.zip

echo Moving files...

xcopy "LanSynK-main\*" "%INSTALL_DIR%" /E /I /Y

rmdir /S /Q "LanSynK-main"

echo Installing Python requirements...

pip install -r requirements.txt

echo.
echo DONE.
echo Run: lansynk
pause