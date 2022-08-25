from operator import ne
from netmiko import ConnectHandler
from CiscoFunctions import interface
from CiscoFunctions import neigbordhood

def conectar(username,password, host):
    cisco = {
    "device_type": "cisco_ios",
    "host": host,
    "username": username,
    "password": password
    }
    net_connect = ConnectHandler(**cisco)
    return net_connect

net_connect = conectar("cisco", "cisco", "10.0.0.1")
net_connect.enable
listInterfaces = interface.listTrunkConnected(net_connect)
print(listInterfaces)
# print(neigbordhood.neighbordInterface(net_connect, listInterfaces))
# print(neigbordhood.neighbordCapabilities(net_connect, listInterfaces))
print(neigbordhood.neighbordResume(net_connect, listInterfaces))

