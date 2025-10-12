import socket
serv = socket.socket(socket.AF_INET, socket.SOC_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)
while True:
	conn, addr = serv.accept()
	from client = ''
	while True:
		data = conn.recv(4096)
		if not data: break
		from_client += data.decode('utf_8')
		print(from_client)
		conn.sent("I am SERVER\n".encode())
	conn.close()
	print('client disconnected')
