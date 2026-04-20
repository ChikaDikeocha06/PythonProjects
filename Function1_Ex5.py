#Example of a function without return value (returns none)
def add_bad(x, y):
    total = x + y
    print(total)             # (2) only prints

result = add_bad(3, 5)
print(result)                # prints None
#without return total the function will only print 
#with no return function prints None