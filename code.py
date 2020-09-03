# socketpk-
# this is socket program using Python it reterives the website data by connecting it with the socket. it basically retrive http severs
import socket
url = input('Enter: ')
pk = url.split('/')
host = pk[2]

mypk= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mypk.connect((host, 80))
mypk.send(('GET '+url+' HTTP/1.0\r\n').encode())

while True:
    data = mypk.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(), end='')

mysock.close()
