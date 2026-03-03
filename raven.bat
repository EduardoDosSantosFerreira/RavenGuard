@echo off
title Compilador RAVENGUARD
color 0D
cls

echo ========================================
echo    COMPILADOR RAVENGUARD v2.0
echo ========================================
echo.

REM Verifica se o PyInstaller está instalado
where pyinstaller >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERRO] PyInstaller nao encontrado!
    echo.
    echo Instale com: pip install pyinstaller
    echo.
    pause
    exit /b 1
)

echo [1/5] Verificando arquivos necessarios...
echo.

REM Verifica se o main.py existe
if not exist "main.py" (
    echo [ERRO] Arquivo main.py nao encontrado!
    echo.
    pause
    exit /b 1
)

REM Verifica se o ícone existe
if not exist "ravenguard.ico" (
    echo [AVISO] Arquivo ravenguard.ico nao encontrado!
    echo O programa sera compilado sem icone.
    echo.
    set "ICON_OPTION="
) else (
    set "ICON_OPTION=--icon ravenguard.ico"
)

REM Verifica se a imagem existe
if not exist "ravenguard.png" (
    echo [AVISO] Arquivo ravenguard.png nao encontrado!
    echo A imagem nao sera incluida no executavel.
    echo.
    set "DATA_OPTION="
) else (
    set "DATA_OPTION=--add-data ravenguard.png;."
)

REM Verifica se o UPX existe
if exist "B:\WorkStation\ravenguard\upx-5.1.0-win64\upx-5.1.0-win64\upx.exe" (
    echo [OK] UPX encontrado - Otimizacao ativada
    set "UPX_OPTION=--upx-dir "B:\WorkStation\ravenguard\upx-5.1.0-win64\upx-5.1.0-win64""
) else (
    echo [AVISO] UPX nao encontrado - Compilacao sem otimizacao
    set "UPX_OPTION="
)

echo.
echo [2/5] Limpando compilacoes anteriores...
echo.

REM Remove pastas antigas
if exist "build" (
    rmdir /s /q build
    echo   - Pasta build removida
)

if exist "dist" (
    rmdir /s /q dist
    echo   - Pasta dist removida
)

if exist "*.spec" (
    del /q *.spec
    echo   - Arquivos .spec removidos
)

echo.
echo [3/5] Iniciando compilacao...
echo.

REM Comando de compilacao
echo Comando: pyinstaller --onefile --noconsole --clean --name ravenguard %ICON_OPTION% %DATA_OPTION% %UPX_OPTION% main.py
echo.
echo Aguarde... Isso pode levar alguns minutos.
echo.

pyinstaller --onefile --noconsole --clean --name ravenguard %ICON_OPTION% %DATA_OPTION% %UPX_OPTION% main.py

if %errorlevel% neq 0 (
    echo.
    echo [ERRO] Falha na compilacao!
    echo.
    pause
    exit /b 1
)

echo.
echo [4/5] Compilacao concluida com sucesso!
echo.

REM Verifica se o executavel foi criado
if exist "dist\ravenguard.exe" (
    echo [5/5] Executavel gerado: dist\ravenguard.exe
    
    REM Mostra informacoes do arquivo
    for %%A in ("dist\ravenguard.exe") do (
        echo.
        echo ========================================
        echo    INFORMACOES DO ARQUIVO
        echo ========================================
        echo Nome: ravenguard.exe
        echo Tamanho: %%~zA bytes
        echo Data: %%~tA
        echo Local: %%~dpA
    )
) else (
    echo [ERRO] Executavel nao encontrado!
)

echo.
echo ========================================
echo    COMPILACAO FINALIZADA!
echo ========================================
echo.
echo Pressione qualquer tecla para abrir a pasta dist...
pause >nul

REM Abre a pasta dist
if exist "dist" (
    explorer dist
) else (
    explorer .
)