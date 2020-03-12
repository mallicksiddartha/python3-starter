import socket
import time
import threading
from queue import Queue

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
q = Queue()

print(skt)

server = 'pythonprogramming.net'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

#request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

#skt.connect((server, port))
#skt.send(request.encode())
#result = skt.recv(512)

#print(result)

#while (len(result) > 0):
    #print(result)
    #result = skt.recv(512)

def portScanner(port1):
    try:
        connection = skt.connect((server, port1))
        print('Port', port1, 'is open!!')
        connection.close()
    except:
        pass

portScannerTimeStart = time.time()

for x in range(1, 500):
    portScanner(x)
print('Done, time needed without thread',(time.time() - portScannerTimeStart),"\n\n\n\n")


print_lock = threading.Lock()


threadedPortScannerStart = time.time()
def portScannerWithThread(port2):
    sktThread = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = sktThread.connect((server, port2))
        with print_lock:
            print('Threaded!! Port', port2, 'is open!!')
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portScannerWithThread(worker)
        q.task_done()

for y in range(50):
    t = threading.Thread(target=threader)
    t.deamon = True
    t.start()

for work in range(1,501):
    q.put(work)

q.join()

print('Done, time needed with thread',(time.time() - threadedPortScannerStart))
