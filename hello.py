# hello.py
#
# Hello world program in python to use to figure out how Github works
#
# Also learning python now so use it for anything I want to test out in python too.
# Remove the parenthesis from the print statement if using version 2.x....changed the way it worked in 3.x
#

var1 = "World"
var2 = "Hello "
nl = "\n"

print("hello", " ", var1)
print("hello " + var1 + "\n")
print("hello",var1,nl)
print(var2,var1,nl)
print("Hello World\n")

mystring = "Corky, you handsome devil you."
hw(mystring)
 # return 0 -- got an error that can not have a return outside of a function
 
def hw(strvar): # need to put a colon after function definitions and soem other stuff. Not exactly sure where all it goes yet.
  return print("Hello ", strvar) #must indent instead of using squiggly braces
  

