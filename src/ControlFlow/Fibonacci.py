def fib(n):
    
    """Write a Fibonacci series up to n"""
    a,b = 0,n
    while a < n :
         
         print(a, end='')
         a,b = b,a+b
    print()

    
fib(100)

 