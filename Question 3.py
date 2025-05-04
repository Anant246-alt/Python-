def fib_number(n):
    fib = [0,1]
    while fib[-1] + fib[-2] <= n:
        fib.append(fib[-1] + fib[-2])
    return fib if n >= 1 else [0]

print(fib_number(18))   
    

