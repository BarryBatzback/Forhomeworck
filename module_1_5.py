immutable_var = ([17,11], 'data', True) #Кортеж не может быть назначен значением во второй раз, что делает его "read-only" списком, то есть значения внуnри кортежа неизменяемы, и назначаются единожды.
print('Immutable tuple: ', end= '')
print(immutable_var)
mutable_lis = [1, 2, 3, 4, 5, 6]
mutable_lis[0] = 10
mutable_lis[1] = 20
mutable_lis[2] = 30
mutable_lis[3] = 40
mutable_lis[4] = 50
mutable_lis[5] = 60
print('Mutable list: ', end= '')
print(mutable_lis)