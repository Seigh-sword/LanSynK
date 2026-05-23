@echo off
title LanSynK Updater

echo Checking for updates...

set INSTALL_DIR=C:\Program Files\LanSynK

cd /d "%INSTALL_DIR%"

curl -L -o latest.zip https://github.com/Seigh-sword/LanSynK/archive/refs/heads/main.zip

powershell -command "Expand-Archive -Force latest.zip temp_update"

xcopy "temp_update\LanSynK-main\*" "%INSTALL_DIR%" /E /I /Y

rmdir /S /Q "temp_update"
del latest.zip

echo Update complete.
pause