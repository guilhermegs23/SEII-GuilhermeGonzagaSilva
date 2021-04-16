#GUilherme GOnzaga SIlva
#11621EMT021

import socket
import select

HEADER_LENGTH = 10

IP = "127.0.0.1" #Define o IP
PORT = 1234 #DEfine a porta

#cria o socket, define como ipv4 e TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# permite reconectar
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# informa ao SO que iremos usar os respectivos IP e porta.
server_socket.bind((IP, PORT))

# faz com que servidor permita novas conexões
server_socket.listen()

# lista de sockets
sockets_list = [server_socket]

# cria um lista vazia para os clientes conectados
clients = {}

print(f'Listening for connections on {IP}:{PORT}...')

# define uma função que irá  receber as mensagens e depois distribui-la para os client's conectadosd
def receive_message(client_socket):

    try:

        # Contem o tamanho da mensagem
        message_header = client_socket.recv(HEADER_LENGTH)

        # se não receber dados, a conexão eh fechada
        if not len(message_header):
            return False

        # converte o header da mensagem para inteiro
        message_length = int(message_header.decode('utf-8').strip())

        # Retorna um objeto de menseagens tipo header e data.
        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
        #alguma coisa errada
        return False

#loop para receber as mensagens para todos os sockets dos clientes e enviar todas as mensagens para todos
while True:
    #o retorno dessa função é um subconjunto das lista de entrada onde o subconjunto é uma lista dos sockets que estão prontos
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)


    # iterar o sockets com dados a serem lidos
    for notified_socket in read_sockets:
        # se o socket notificado for o socket do servidor, temos uma nova conexão.
        if notified_socket == server_socket:
            # aceita uma nova conexão
            client_socket, client_address = server_socket.accept()
            # cliente deve dar o seu nome
            user = receive_message(client_socket)
            # se falso, cliente desconectou
            if user is False:
                continue

            # Adiciona o socket para select.select() list
            sockets_list.append(client_socket)

            # salva seu username e seu cabeçalho
            clients[client_socket] = user

            print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))

        # se o socket notificado não for um socket de servidor, temos uma mensagem para ler 
        else:
            # recebe a mensagem
            message = receive_message(notified_socket)
            # verficiando se realmente existe uma mensage, se o cliente desconectar, a mensagem estará vazia
            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
                # remove da lista de socket.socket()
                sockets_list.remove(notified_socket)
                # remove da lista de usuarios
                del clients[notified_socket]
                continue

            #supondo que não foi uma desconexão
            user = clients[notified_socket]

            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            # agora transmitindo para todos os clientes
            for client_socket in clients:
                # não mandar para o cliente que o enviou
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    # não eh necessário, mas irá lidar com problemas de sockets (exceçoes)
    for notified_socket in exception_sockets:
        # remove da lsita socket.socket()
        sockets_list.remove(notified_socket)
        # Remove da lista de users
        del clients[notified_socket]