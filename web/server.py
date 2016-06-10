import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
conn.settimeout(60)

print('Connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        print("No data")
        break
    conn.send(data.upper())

conn.close()
