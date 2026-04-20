#Example of Multiple Parameters
def make_sandwich(bread, meat, cheese):   # (1) header + (2) multiple parameters
    print(f"{meat} and {cheese} on {bread}")  # (3) body

make_sandwich("wheat", "turkey", "swiss")     # (4) arguments (order matters)
#def= keyword to define function
#"wheat", "turkey", "swiss" → arguments
#make_sandwich(...)=calls function
#("wheat", "turkey", "swiss")= are the values to the function parameter