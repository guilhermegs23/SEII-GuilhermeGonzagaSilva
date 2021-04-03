#Guilherme GOnzaga
# 11621EMT021

import socket
s = socket.socket()
host = socket.gethostname()
port = 13246
s.connect((host,port))
print("Conectado com sucesso!")

filename = 'file_client.txt'
file = open(filename, 'wb')
dados = s.recv(1024)
file.write(dados)
file.close()
print("Arquivos recebidos!")