cache = {}
def fib_func(i) :
    if i in cache :
        return cache[i]
    elif i == 1 or i == 2 :
        return 1
    elif i > 2 :
        fib_value = fib_func(i-1) + fib_func(i-2)
        cache[i] = fib_value
        return fib_value
# cache = {}
print(fib_func(100))