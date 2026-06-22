def pattern(s):
     x = len(s) // 2
     first = s[:x]
     second = s[x:]

     if len(s) == 1:
          return True
     elif first == second:
         return True
     else:
         return False


print(pattern("ababab"))




def factors(num):
     factors = []
     for i in range(1, num+1):
         if num %i == 0:
             factors.append(i)
     return factors


print(factors(12))


def classify_num(num):
    even = []
    odd = []
    for i in num:
        if i % 2 == 0:
            even.append(i)
        if i % 2 != 0:
             odd.append(i)
    return even,odd


num = [2, 22,33, 55,64,75,87,96,155]

print(classify_num(num))


def prime_check(num):
    if num == 1:
       return "NOT prime"
    for i in range(2, num):
        if num % i == 0:
              return " not prime"
    else:
             return " prime"

num = [2,3,5,4,33,55,66,43,77]
for i in num:
   print(f'{i} is {prime_check(i)}')


def classify_num(num):
    even = []
    odd = []
    prime_numbers = []
    for i in num:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
        if prime(i)   :
            prime_numbers.append(i)

    return even,odd, prime_numbers


def prime(num):
    if num == 1:
       return False
    for i in range(2, num):
         if num % i == 0:
             return False
    else:
            return True

num = [1,2,3,5,4,33,55,66,43,77]
even,odd,prime_numbers = classify_num(num)
print(even)
print(odd)
print(prime_numbers)



n = "adilabaddistrict"
count = {}
for i in n:
     if i in count :
        count[i] += 1
     else:
        count[i] = 1

print(count)


def sum(a,b):
    add = a+ b
    return add

result = sum(2,3)
print(result)

print("hello world")

