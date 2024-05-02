a = {0: 0, 1:1}
def fibonacci(n):
    if n in a.keys():
        return a[n]
    a[n] = fibonacci(n-2)+fibonacci(n-1)
    return a[n]

            
print(fibonacci(50))
