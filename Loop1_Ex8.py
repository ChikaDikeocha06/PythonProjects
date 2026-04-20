#Example of looping with range(len()) function
fruits = ["apple", "banana", "orange"]

for i in range(len(fruits)):  # loop using index
    print(i, fruits[i])  # index + value  
#fruits is the variable that holds the value of a list
#for, in is the keywords for looping
#len() is used to get the number of items in the list
# range(len()) is used to create a sequence of index numbers
#       -if the list has 3 items the range is 0-2 or range(0,3)
# i is the loop variable and it stores the value of index of each value in the list
# fruits[i] accesses the item at that index
# print displays the output to the user