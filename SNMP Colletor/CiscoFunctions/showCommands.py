def getHostname(netconnect):
    hostname = str(netconnect.send_command("sh running-config partition common | i hostname"))
    hostname = hostname.split(" ")[1]
    return hostname

def getRunningConfig(netconnect):
    for line in netconnect.send_command("sh running-config partition"):
        print(line)