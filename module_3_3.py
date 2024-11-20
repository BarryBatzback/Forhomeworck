
def print_params (a = 1, b = 'string', c = True):
    print (a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [20, 'Tupe', False]
values_dict = {'a':5, 'b':'init', 'c':True}

print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

def append_to_list(item, list_my=None):

    if list_my is None:

        list_my = []

        list_my.append(item)

        print(list_my)

append_to_list(1)
append_to_list(5)
append_to_list(True)