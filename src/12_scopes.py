# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

"""
A local variable can be accessed only locally, a variable defined inside a function is accessible to that function only and can't be used outside the function.
"""

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    global x #declare a global function
    x = 99 # can now be referenced in the global scope

change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(x)

# This nested function has a similar problem.

def outer(): 
    y = 120 # variable defines in outer function

    def inner():
        y = 999
        print (y) # able to access the variable in the outer function
    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)


outer()
