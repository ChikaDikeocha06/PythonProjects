# example of a reusable Function Example
def calculate_circle_area(radius):   # (4) parameter
    area = 3.14159 * radius * radius # (2) calculation
    return area                      # (6) return

print(calculate_circle_area(5))      # (3)(5)
#must put return to give value back when function is called
#Without it, the result stays trapped inside the function