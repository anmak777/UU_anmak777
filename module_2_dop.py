first_stone = input('Введите первое число: ')
elements = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
password = []

for i in range(len(elements)):
    for j in range(i+1,len(elements)):

        if int(first_stone) % (elements[i] + elements[j]) == 0:
            password.append(elements[i])
            password.append(elements[j])
        else:
            continue

print(''.join(str(el) for el in password))