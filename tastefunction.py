# Read through the code below. Even if you don't understand it, try to make 
# a guess about what it does. What do you think will happen when you press 
# "Test Run"? Once you have a prediction, press "Test Run" and compare what 
# happens to what you predicted.

def say_hello(name):
    greeting = "Hello " + name + "!"
    return greeting


def sum(firstnumber, secondnumber):
    return firstnumber + secondnumber


print sum(5,7)

# say_hello is a function. Or, as Dave would call it, a procedure.
# This procedure isn't particularly interesting because it only does
# one thing. 

# Continue to the next example to see a more interesting version of say_hello.


# Once again, say_hello is a function (AKA procedure). But this time, it DOESN'T
# do the same thing every time. 
#
# Read through the code and try to predict what the output will be when 
# you press "Test Run"



print say_hello("Miriam")
print say_hello("Andy")
