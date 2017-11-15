import socket
s= socket.socket()
s.bind(('10.1.2.44',554))
s.listen(5)
while True:
    c,addr=s.accept()
    print 'got connection from ',addr
    t = c.recv(1024)
    c.send('how are you')
    print t
    
    
