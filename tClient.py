import socket
s = socket.socket()
s.connect(('10.1.2.43',536))
s.send('Hello, Who are you?')
t = s.recv(1024)
print t
s.close()
