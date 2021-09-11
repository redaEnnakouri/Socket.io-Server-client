import socket

host, port = ('localhost',6001)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("le serveur est demare")

while True :
    socket.listen(5)
    conn,adress =socket.accept()
    print("Client connecter")
    
    data = conn.recv(1024)
    data = data.decode("utf8")
    print(data)

conn.close()
socket.close()