import subprocess
from subprocess import STARTUPINFO, STARTF_USESHOWWINDOW

def _silent(command: str):
    """Executa comandos em segundo plano sem janelas"""
    startupinfo = STARTUPINFO()
    startupinfo.dwFlags |= STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = 0  # SW_HIDE

    subprocess.Popen(
        command,
        shell=True,
        startupinfo=startupinfo,
        creationflags=subprocess.CREATE_NO_WINDOW
    )

def run_ravenguard():
    """Ravenguard Security Scan - Versão melhorada do MRT"""
    _silent("mrt /Q")  # Executa MRT silenciosamente

def run_sfc():
    """System File Checker - Verifica e repara arquivos do sistema"""
    _silent("sfc /scannow")

def run_dism():
    """DISM - Repara a imagem do Windows"""
    _silent("DISM /Online /Cleanup-Image /RestoreHealth /Quiet /NoRestart")