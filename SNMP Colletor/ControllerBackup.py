from  OtherFunctions import CheckPort, ConnectSSH, CreateFolder
from CiscoFunctions import showCommands

def startBackup(login, password, listDevices):
    for device in listDevices:
        netconnect = ConnectSSH.conectar(login, password, device, "cisco_ios")
        deviceHostname = showCommands.getHostname(netconnect)
        pathBackup = f"Backup/{deviceHostname} - {device}"
        CreateFolder.folder(pathBackup)



    