import getpass
import Coleta

login = input("Login:")
password = getpass.getpass()

listDevices = []
fileDevices = open("DispositivosConhecidos.txt")
for line in fileDevices:
    line.replace("\n", "")
    listDevices.append(line)
    
Coleta.InicarColeta(login, password, listDevices)
