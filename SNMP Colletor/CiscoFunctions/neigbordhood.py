def neighbordInterface(netconnect, listInterfaces):
    listNeighbord = []
    for interface in listInterfaces:
        output = netconnect.send_command("sh cdp neighbors " + str(interface))
        listNeighbord.append(output)
    return listNeighbord

def neighbordCapabilities(netconnect, listInterfaces):
    listNeighbord = []
    for interface in listInterfaces:
        output = netconnect.send_command("sh cdp neighbors " + str(interface) + " detail | i Capabilities: ")
        capabilities = str(output)
        capabilities = capabilities.split("Capabilities: ")[1]
        listNeighbord.append(interface + ";Capabilities:" + capabilities)
    return listNeighbord

def neighbordResume(netconnect, listInterfaces):
    listNeighbord = []
    for interface in listInterfaces:
        output = str(netconnect.send_command("sh cdp neighbors " + str(interface) + " detail | i (IP address: | Capabilities: |Device ID|Total cdp entries displayed : )"))
        if "Total cdp entries displayed : 1" in output:
            deviceID = output.split("\n")[0].split("Device ID: ")[1]
            ip = output.split("\n")[1].split("IP address: ")[1]
            capabilities = output.split("\n")[2].split("Capabilities: ")[1]
            listNeighbord.append(interface + ";" + deviceID + ";" + ip + ";" + capabilities)
        else:
            listNeighbord.append(interface + ";" + "unknown")
    return listNeighbord