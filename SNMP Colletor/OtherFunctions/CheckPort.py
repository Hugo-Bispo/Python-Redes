import socket

def checkPortStatus(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    if result == 0:
        print("Port is open")
        sock.close()
        return True
    else:
        print("Port is not open")
        sock.close()
        return False
