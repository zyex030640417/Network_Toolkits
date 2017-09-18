import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

#start listening and at most can take 5 connection
server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

#Make up the thread to deal with client
def handle_client(client_socket):

    #display the data from client
    request = client_socket.recv(1024)

    print "[*] Received: %s" % request

    #Return a package
    client_socket.send("Server send U a package")
    
    #Close the session
    client_socket.close()

while True:
    client,addr = server.accept()

    print "[*] Accepted connection from : %s:%d" % (addr[0],addr[1])

    if(client==None):
        print "NO CONNECTION"

    #Active client thread to deal with the data from client
    client_handler = threading.Thread(target=handler_client,args=(client,))
    client_handler.start()

