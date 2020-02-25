# Example 01_05: example01_05.py
# Displaying an object's location, type and value.

# prompt the user for input
integer1 = input( "Enter first integer:\n" )  # read a string
print("integer1: ", id( integer1 ), type( integer1 ), integer1 )

integer1 = int( integer1 )   # convert the string to an integer
print("integer1: ", id( integer1 ), type( integer1 ), integer1)

integer2 = input( "Enter second integer:\n" ) # read a string
print("integer2: ", id( integer2 ), type( integer2 ), integer2)
integer2 = int( integer2 )   # convert the string to an integer
print ("integer2: ", id( integer2 ), type( integer2 ), integer2)

sum = integer1 + integer2    # assignment of sum
print ("sum: ", id( sum ), type( sum ), sum)

