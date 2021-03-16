#Guilherme Gonzaga Silva 11621EMT021 
#prog20.py

# try:
#     f = open('test_file.txt')
#     var = bad_var
# except FileNotFoundError:
# # except FileNotFoundError as e:
#     print('Esse arquivo nao existe!')
#     # print(e)
# except Exception:
# except Exception as e:
    # print('Alguma coisa esta errada!')
    # print(e)
# else:
    # print(f.read())
    # f.close()
 # finally:
    # print("Excecutando")


try:
    f = open('currupt_file.txt')
    # if f.name == 'currupt_file.txt':
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error')
else:
    print(f.read())
    f.close()
finally:
    print("Excecutando")