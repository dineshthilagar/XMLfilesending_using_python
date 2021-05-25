'''
Created on 25-May-2021

@author: Dinesh Thilagar
'''
import xml.etree.ElementTree as ET
import socket
sock= socket.socket()
host=socket.gethostname()
port=1218
sock.connect((host,port))
sock.send(b"Hello from client")


with open("D:\\readfile11.txt","wb") as file:
    print("file open")
    print("receiving data...")
    while True:
        data = sock.recv(1024)
        print(f"data={data}")
        if not data:
            break
        file.write(data)
print("got the file")

mytree = ET.parse("D:\\readfile11.txt")
myroot =mytree.getroot()
for x in myroot.findall('book'):
    item = x.find('title').text
    price=x.find('price').text
    print(item,"-" ,price)


sock.close()
print("connection is closed")
