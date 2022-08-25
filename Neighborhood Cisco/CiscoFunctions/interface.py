def listTrunk(netconnect):
    listInterfaces = []
    output = netconnect.send_command("sh interface status | i trunk")
    for line in output.splitlines():
        line = line[0:6]
        listInterfaces.append(line.replace(" ", ""))
    return listInterfaces

def listTrunkConnected(netconnect):
    listInterfaces = []
    output = netconnect.send_command("sh interface status | i trunk")
    for line in output.splitlines():
        if "connected" in line:
            line = line[0:6]
            listInterfaces.append(line.replace(" ", ""))
    return listInterfaces