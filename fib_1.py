cache = {}

def fib(n):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    result = fib(n-1) + fib(n-2)
    cache[n] = result
    return result
print(fib(10))
print(fib(1))
print(cache)