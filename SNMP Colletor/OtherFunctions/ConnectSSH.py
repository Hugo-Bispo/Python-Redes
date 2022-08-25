from netmiko import ConnectHandler

def conectar(username,password, host, device_type):
    cisco = {
    "device_type": device_type,
    "host": host,
    "username": username,
    "password": password,
    "secret": password,
    }
    net_connect = ConnectHandler(**cisco)
    return net_connect