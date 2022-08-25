# Automação para gerar Backup de Configuração de Switches e Roteadores Cisco
import getpass
# import ControllerBackup
from OtherFunctions import CreateFolder

login = input("Login:")
password = getpass.getpass()

listDevices = []
fileDevices = open("Dispositivos.txt")
for line in fileDevices:
    line.replace("\n", "")
    listDevices.append(line)

CreateFolder.folder("Backup")
# ControllerBackup.startBackup(login, password, listDevices)
