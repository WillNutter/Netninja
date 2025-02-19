@echo off
Title Digital Clock
Color 0a
@mode con cols=20 lines=5
:main
cls
echo.
echo Time: %time%
echo.
echo Date: %date%
echo.
ping -n 2 0.0.0.0>nul
goto main
