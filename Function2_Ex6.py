#Example of Positional vs Keyword Mixing
def book_flight(origin, destination, date):
    print(origin, destination, date)

book_flight("NYC", destination="LAX", date="2024-03-15")  # valid