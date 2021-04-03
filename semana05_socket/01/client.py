#Guilherme GOnzaga
# 11621EMT021

import socket
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 13246
s.connect((host,port))
print("Conectado com sucesso!")

nome_do_arquivo_destino = input(str("Digite o nome do arquivo destino: "))
filename = 'file_client %s %d %s.txt' % (ip, port, nome_do_arquivo_destino)
file = open(filename, 'wb')
dados = s.recv(1024)
file.write(dados)
file.close()
print("Arquivos recebidos!")