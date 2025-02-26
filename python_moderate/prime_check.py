def prime(n):
    if n <= 1:
        return "not prime"
    for i in range(2,n):
         if n % i == 0:
             return "not prime"

    return "prime"


n = [1,2,3,79,119,1,7,8,9,11,4,13,227,349,401]
for num in n:
    print(f'{num} :{prime(num)}')