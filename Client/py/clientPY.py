import socket

host, port = ('localhost',6001)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((host, port))
    print("client connct")

    data = "Hi my name is Reda"
    data = data.encode("utf8")
    socket.sendall(data)


except ConnectionRefusedError:
    print('lose connction')

finally:
    socket.close()
