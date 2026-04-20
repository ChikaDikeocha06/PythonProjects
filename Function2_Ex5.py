#Example of Keyword Arguments (Named Inputs)
def divide(dividend, divisor):
    return dividend / divisor

divide(dividend=10, divisor=2)     # (6) keyword arguments
divide(divisor=2, dividend=10)     # order doesn’t matter
#order doesnt matter when you write equal sign