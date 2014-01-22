import socket
import sys 
try:
	import thread 
except ImportError:
	import _thread as thread

HOST = '' # Symbolic name meaning all available interfaces 
PORT = 8888 # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print ('Socket created')
try:
	s.bind((HOST, PORT)) #Bind socket to local host and port
except socket.error:
	msg = str(socket.error)
	print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]) 
	sys.exit()
print ('Socket bind complete')
s.listen(10) #Start listening on socket 
print ('Socket now listening')

def clientthread(conn): #Function for handling connections. This will be used to create threads 
	#Sending message to connected client
	conn.send('Welcome to the server. Type something and hit enter\n') 
	while True: #infinite loop so that function do not terminate and thread do not end.
		data = conn.recv(1024) #Receiving from client 
		reply = ' <OK ... ' + data + ' > '
		if not data:
			break
		conn.sendall(reply)
	conn.close()

while 1: #now keep talking with the client
	conn, addr = s.accept() #wait to accept a connection - blocking call
	print ('Connected with ' + addr[0] + ':' + str(addr[1]))
	#start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
	thread.start_new_thread(clientthread ,(conn,)) 

s.close()