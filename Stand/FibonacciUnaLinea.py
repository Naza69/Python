fibo = lambda n: n if n <= 1 else fibo(n-1) + fibo(n-2)

"""def fibo(n):
    if n > 1:
        return fibo(n-1) + fibo(n-2)
    else:
        return n
    """

print(fibo(10))
