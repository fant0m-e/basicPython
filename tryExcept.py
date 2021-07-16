try:
    answer = 10/0
    number = int(input("Enter a number: ")) # converts number to integer
    print(number)
except ZeroDivisionError as err: # will catch only a division by zero WITHIN the try:
    print(err)
except ValueError: # if an invalid character is input, prints this rather than throwing an error
    print("Invalid input.")
