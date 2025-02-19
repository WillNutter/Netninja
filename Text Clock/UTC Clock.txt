@echo off
Title Digital Clock (UTC)
Color 0a
@mode con cols=40 lines=10

:main
cls
echo.
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "([datetime]::UtcNow).ToString('yyyy-MM-dd HH:mm:ss')"`) do set UTC_Time=%%i
echo UTC Time: %UTC_Time%
echo.
ping -n 2 0.0.0.0 > nul
goto main
