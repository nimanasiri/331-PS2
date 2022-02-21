from socket import *
from time import time

serverName = '172.31.123.220'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.settimeout(1)

for i in range(1, 11):
    start_time = time()

    msg = "PING " + "{} {}".format(i, start_time)
    clientSocket.sendto(msg.encode(), (serverName, serverPort))

    try:
        resp, serverAddress = clientSocket.recvfrom(2048)
        RTT_time = time() - start_time
        print( resp.decode() + ': RTT = {}, '.format(RTT_time))
    except:
        print('Request timed out')
    

    end_time = time()