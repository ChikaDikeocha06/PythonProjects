#Example return with multiple parameters 
def greet(name="Guest"):     # (2) default parameter
    print(f"Hello, {name}")

greet("Alice")               # overrides default
greet()                      # uses default
#def= keyword to define function
#greet= the function variable
#name= "Guest"= the parameter (name) and the defualt value ("Guest")
#greet()+ will print the defualt value "Guest"