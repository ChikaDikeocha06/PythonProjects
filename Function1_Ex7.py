#Example of a function with condition + Early return
def check_age(age):
    if age < 0:              # (8) condition
        return "Invalid" 
    return "Valid"    # (6) early return
print(check_age(18))
print(check_age(-18))
#def= keyword to define function
#check_age+ the function variable
#age is the parameter
#if is the keyword to conditions
#age < 0:= the condition
#return= stores value and returns when called
