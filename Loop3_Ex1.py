#Example of a break loop
numbers = [5, 8, 3, -2, 10]

for num in numbers:
    if num < 0:
        print("Found negative:", num)
        break
    print(num, "is positive")

print("Done")
# numbers is the variable
# num is the loop variable
# for, in is the loop keywords for looping
# if is used to condition check
# < comparison operator 
#print() is a fuction is display output
#break stocks the loop immediately