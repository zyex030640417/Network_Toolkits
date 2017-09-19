import sys
import socket
import getopt
import threading
import subprocess

#Define some global variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    print "BHP Net Tool"
    print
    print "Usage : bhnet.py -t target_host -p port"
    print "-l --listen    -[host]:[port] listening to get in connection"
    print "-e --execute=file_to_run   -execute specify file while connection"
    print "-c --command   -active shell"
    print "-u --upload=destination   -write out [destination] and upload file when get in connection"
    print
    print
    print "example : "
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
    print "echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135"
    sys.exit(0)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target
