'''
Created on 25-May-2021

@author: Dinesh Thilagar
'''
import socket

sock= socket.socket()
host=socket.gethostname()

ONE_CONNECTION_ONLY = (True)

filename = "NewFile.xml"



sock.bind((host, 1218))
sock.listen(10)
print("File server started")

while True:
    conn,addr =sock.accept()
    print(f"Accepted connection from {addr}")
    data = conn.recv(1024)
    print(f"server recevied {data}")
    with open (filename, "rb") as file:
        data = file.read(1024)
        while data:
            conn.send(data)
            print(f"sent {data!r}")
            data=file.read(1024)
            
    print("File sent completed")
    conn.close()
    if(ONE_CONNECTION_ONLY):
        break
sock.shutdown(1)
sock.close()



