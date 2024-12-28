def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [5,'Hello',False]
values_dict = {'a':5,'b':'Trust','c':[10,23,1]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [66,['c','d','e']]

print_params(*values_list_2, 42) # почему 42 интерпретируется как параметр a, а не c?
                                    # хотя выводится на месте с


