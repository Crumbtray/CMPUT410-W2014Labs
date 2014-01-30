import socket
import sys 
try:
	import thread 
except ImportError:
	import _thread as thread
import curses

class Server:
	s = ''
	HOST = ''
	PORT = 0

	def __init__(self, host, port):
		self.screen = curses.initscr()
		self.HOST = host
		self.PORT = port
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print ('Socket created') 
		try:
			self.s.bind((self.HOST, self.PORT)) #Bind socket to local host and port
		except socket.error:
			msg = str(socket.error)
			print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]) 
			sys.exit()
		print ('Socket bind complete')
		self.s.listen(10) #Start listening on socket 
		print ('Socket now listening')
	
	def clientthread(self, conn): #Function for handling connections. This will be used to create threads 
		#Sending message to connected client
		conn.send('Welcome to the server. Type something and hit enter\n') 
		while True: #infinite loop so that function do not terminate and thread do not end.
			data = conn.recv(1024) #Receiving from client 
			reply = data + ' Clinton '
			if not data:
				break
			conn.sendall(reply)
		conn.close()

	def run(self):
		thread.start_new_thread(self.acceptConnection, ())
		while True:
			key = self.screen.getch()
			if key == 27:
				break
		self.s.close()

	def acceptConnection(self):
		while 1: #now keep talking with the client
			conn, addr = self.s.accept() #wait to accept a connection - blocking call
			print ('Connected with ' + addr[0] + ':' + str(addr[1]))
			#start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
			thread.start_new_thread(self.clientthread ,(conn,))


newServer = Server('', 8888)
newServer.run()