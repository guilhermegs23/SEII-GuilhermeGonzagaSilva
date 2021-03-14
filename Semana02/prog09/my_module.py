#Guilherme Gonzaga Silva 11621EMT021 
#prog09.py

#1)
print('Imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1