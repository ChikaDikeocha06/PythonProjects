#Example of a break loop with user input
while True:
    command = input("Enter command: ")

    if command == "exit":
        print("Goodbye")
        break

    print("You typed:", command)
#while keyword to start looping
#True boolean to start while loop and infinite looping
#command is a variable that holds user input
#if is a condition checker
#condition is the variable and uses == as a comparision operator
#break exits the loop