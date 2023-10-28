for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# n = 5 
# def prime(n):
#     if n % 2 == 0:
#         print(n,'is not prime')

#     else:
#         print(n, 'is prime')

# prime(n)


