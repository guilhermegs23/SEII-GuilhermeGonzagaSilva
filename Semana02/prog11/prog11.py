#Guilherme Gonzaga Silva 11621EMT021 
#prog11.py

#1)
#f = open('teste.txt', 'r')

#print(f.name)
# print(f.mode)

#f.close()

#2)
#with open('teste.txt', 'r') as f:
    # f_contents = f.read()
    # print(f_contents)
    
    # f_contents = f.readlines()
    # print(f_contents)

    # f_contents = f.readline() #imprime a primeira linha
    # print(f_contents)
    # f_contents = f.readline() #imprime a segunda linha
    # print(f_contents)
    
    # f_contents = f.readline()
    # print(f_contents, end='') #imprime sem a linha extra entre as linhas
    # f_contents = f.readline()
    # print(f_contents, end='') #imprime sem a linha extra entre as linhas

    # for line in f:
    #     print(line, end='')

    # f_contents = f.read(100) #le as 100 primeiras caracteres
    # print(f_contents, end='')
    # f_contents = f.read(100) #le + 100 caracteres
    # print(f_contents, end='')
    # f_contents = f.read(100) #le + 100 caracteres, porém ja deu 200 caracteres
    # print(f_contents, end='')

    # size_to_read = 10
    # f_contents = f.read(size_to_read)
    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read)

    # size_to_read = 10
    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')
    # f.seek(0) #agora começa do inicio
    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')
    # # print(f.tell()) #10

#3)   
# with open('test2.txt','w') as f:
#     pass
#     f.write('Test')
#     f.seek(0)
#     f.write('R')

#4
# with open('teste.txt', 'r') as rf:
#     with open('teste_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

#5
#  with open('imagem.jpg', 'rb') as rf:
#     with open('imagem_copy.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

#6
  with open('imagem.jpg', 'rb') as rf:
     with open('imagem_copy.jpg', 'wb') as wf:
         imagem_size = 4096
         rf_imagem = rf.read(imagem_size)
         while len(rf_imagem) > 0:
             wf.write(rf_imagem)
             rf_imagem = rf.read(imagem_size)