def fib(n):

    #Base Case
    if n == 0 or n == 1:
        return n
    
    #Recursive Case
    return fib(n - 1) + fib(n -2)

print(fib(4))