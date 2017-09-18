import socket

target_host = 'www.google.com'
target_port = 80

#Create a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Let Client connect
client.connect((target_host,target_port))

#send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#recv some data
response = client.recv(4096)

print response
