import socket

#target's host and port
target_host = '127.0.0.1'
target_port = 80

#Create a socket objet
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Send the data
client.sendto('AABBCC',(target_host,target_port))
        
#recv some data
data, addr = client.recvfrom(4096)

print data
