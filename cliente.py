import socket
import json
import time
HOST = '157.230.169.186'    # The remote host
PORT = 4500       
conta=1       # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        conta=conta+1
        data = json.dumps({"temp": str(conta), "hum": str(conta)})
        if not data: break
        time.sleep(1.25)
        print(data)
        s.sendall(data.encode())