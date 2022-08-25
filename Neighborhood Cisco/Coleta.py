from msilib import text
from operator import ne
from queue import Empty
from netmiko import ConnectHandler
from CiscoFunctions import hostname, interface, neigbordhood
from OtherFunctions import CheckPort

def conectar(username,password, host):
    cisco = {
    "device_type": "cisco_ios",
    "host": host,
    "username": username,
    "password": password,
    "secret": password,
    }
    net_connect = ConnectHandler(**cisco)
    return net_connect

def InicarColeta(username,password, listDevices):

    listConnected = []
    listOutputDevices = []
    while True:
        deviceConnect = str(listDevices.pop())
        if deviceConnect not in listConnected:
            listConnected.append(deviceConnect)
            host = deviceConnect.split(";")[0]
            if CheckPort.checkPortStatus(host, 22):
                netconnect = conectar(username,password, host)
                netconnect.enable()
                deviceHostname = hostname.getHostname(netconnect)
                listInterfaces = interface.listTrunkConnected(netconnect)
                listNeigbordhood =  neigbordhood.neighbordResume(netconnect, listInterfaces)
                print(listNeigbordhood)
                ipsNeigbords = ""
                for lineNeigbord in listNeigbordhood:
                    lineNeigbord = str(lineNeigbord)
                    typeDevice = lineNeigbord.split(";")[3]
                    if "Switch" in typeDevice:
                        ipNeigbord = lineNeigbord.split(";")[2]
                        ipsNeigbords += ipNeigbord + " - "
                        if ipNeigbord not in listConnected:
                            listDevices.append(ipNeigbord)

                listOutputDevices.append(f"Hostname:{deviceHostname} IP:{deviceConnect} Vizinhos: {ipsNeigbords}")
                netconnect.disconnect()
        if listDevices.__len__() == 0:
            break

    for line in listOutputDevices:
        print (line)
