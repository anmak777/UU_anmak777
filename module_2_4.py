numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = [2]
not_primes = []
is_prime = True
for i in range(len(numbers)):
    if numbers[i] > 2:
        for j in range(2,numbers[i]):
            if numbers[i] % j == 0:
                is_prime = False
                not_primes.append(numbers[i])
                break
            elif j > numbers[i]//2:
                is_prime = True
                primes.append(numbers[i])
                break
print('Primes:',primes)
print('Not Primes:',not_primes)