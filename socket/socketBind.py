import socket
import time
from queue import Queue
from _thread import *

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 5555

try:
    skt.bind((host, port))
except socket.error as e:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

skt.listen(5)
print('Waiting for connection...')

def threaded_client(conn):
    conn.send(str.encode('Ooooi, write something - \n'))

    receivedMessage = ""
    while True:
        data = conn.recv(2048)
        reply = data.decode('utf-8')
        if not data:
            break
        if "\n" in reply:
            conn.sendall(str.encode('Server output: ' + receivedMessage + '\n'))
            receivedMessage = ""
        else:
            receivedMessage += reply
        
    conn.close()


while True:
    con, addr = skt.accept()
    print('Connected to: ', addr[0],':',addr[1])

    start_new_thread(threaded_client, (con,))
