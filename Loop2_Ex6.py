#Example of a loop to validate age 
age = -1

while age < 0 or age > 120:      
    age = int(input("Enter age: "))   
# condition uses logical operator "or"
# keep asking until valid