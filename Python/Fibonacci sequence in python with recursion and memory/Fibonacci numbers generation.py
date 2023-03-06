# define a function togenerate the nth fibonacci number 
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)  # recursion

for i in range(10):
    print(f(i),end= ' ')

print()


# nth fibonacci number with recursion and memorizing
d = {0:0,1:1}               #set a initialized dictionary 
def fib(n):
    if n in d:              
        return d[n]
    d[n] = fib(n-1)+fib(n-2)    # calculate and assigne the value of f(n-1)+f(n-2) for the nth key 
    return d[n]

for i in range(10):
    print(fib(i),end = ' ' )



# try print f(100) and fib(100), you will see the obvious computation speed difference.

# hear the noise of your computer? Remember use Ctrl + C to stop 
