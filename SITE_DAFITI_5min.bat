@echo off
title ROBO AUTOMATION TESTE SITE DAFITI
goto main

:main
cls
echo TESTES PARA SITE DAFITI
echo 5 MINUTOS PARA INICIAR O TESTE...

For /f "tokens=1-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%b-%%a)
For /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a:%%b)


echo DATA %mydate%        HORA %mytime%


choice -c r -t 3 -d r >nul
goto startp

:startp
cls
echo INICIANDO O TESTE ...
choice -c r -t 300 -d r >nul
F:\Robo - Teste de Compra
start python botdafiti.py
tskill C:\Python27\python.exe
goto main