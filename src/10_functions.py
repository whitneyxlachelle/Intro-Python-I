# Write a function is_even that will return true if the passed-in number is even.

def is_even():

# Read a number from the keyboard
# remember to indent to show what's inside the function

    num = input("Enter a number: ")
    num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

    if num % 2 == 0:
        print(num, "Even!")
    else:
        print(num, "Odd")

is_even()