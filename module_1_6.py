my_dict = {'Sergey':1992,'Anton':1990, 'Dmitriy':1994, 'Aleksandr':1993}
print('Dict: ',my_dict)
print('Existing value: ',my_dict['Sergey'])
print('Not existing value: ',my_dict.get('Vlad'))
my_dict.update({'Vlad':1995,
                'Vera':1997})
print('Delete value: ',1995,',',1997)
del (my_dict['Sergey'])
print('Modified dictionary: ',my_dict)
print()
my_set = {1,2,2,3,'Home',5,5,5,1.5,2.5}
print('My SET:',my_set)
my_set = {1,2,2,3,'Home',5,5,5,1.5,2.5,0.5,'Number'}
(my_set.discard('Number'))
(my_set.remove('Home'))
print('My NEW SET:',my_set)