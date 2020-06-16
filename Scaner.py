import socket
import threading


def scan_tcp_port(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(0.5)
	try:
		connect = sock.connect((ip, port))
		print('Port TCP :', port, ' opened')
	except:
		print('Port TCP :',  port, ' closed')
	finally:
		sock.close()

def scan_udp_port(ip, port):
	try: 
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.settimeout(0.5)
		conn = sock.connect((ip, port))
		try:
			if ports == "80":
				sock.sendto("GET HTTP/1.1  \r\n", (ip, port))
			else:
				sock.sendto(str.encode(" \r\n "), (ip, port))
			data = sock.recvfrom(1024)
			print('Port UDP :', port, ' ', bytes.decode(data))
		except:
			print('Port UDP :', port, "Unavailable")
	except:
		print('Port UDP :',  port, ' closed')
	finally:
		sock.close()

def scan_port(ip, port):
	scan_tcp_port(ip, port)
	scan_udp_port(ip, port)

if __name__ == "__main__":
	print("[ip]")
	ip = input()
	print("[от] [до]")
	x, y = map(int, input().split())
	for i in range(x, y+1):
		thread = threading.Thread(target=scan_port, args=(ip,i))
		thread.start()
