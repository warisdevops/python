import socket
s= socket.socket()  #socket created(has ipv4 and tcp by default)
print('socket created')
s.bind(("localhost", 9999)) # ipaddress, and port number on server listening
s.listen(0) # server listening for 5 connections
print('waiting for connections')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('connected with', addr, name)
    c.send(bytes('welcome to telusko', 'utf-8'))
    c.close()