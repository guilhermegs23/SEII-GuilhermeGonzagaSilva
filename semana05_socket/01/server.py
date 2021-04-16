#Guilherme GOnzaga
# 11621EMT021

import socket

s = socket.socket()
host = socket.gethostname()
port = 13246
s.bind((host,port))
s.listen(1)

print("Esperando Conexões para o servidor!")
connect_client, addreess = s.accept()
print("Cliente conectado")

file = open('file_server.txt', 'rb')
dados = file.read(1024)
connect_client.send(dados)
print("Dados enviados!")