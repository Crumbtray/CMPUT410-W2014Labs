import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8888))
data = s.recv(1024)
print data
s.send("hello")
data = s.recv(1024)
s.close
print data