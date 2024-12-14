immutable_var = 5, 6, 'd', 'f'
print('Immutable tuple:',immutable_var)
#immutable_var[0] = 500
# Объект типа кортеж не поддерживает изменения элементов

mutable_list = [5, 6, 'd', 'f']
mutable_list = mutable_list + [4]
mutable_list[4] = 'Modified'
print('Mutable list:',mutable_list)
