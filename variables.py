# Python syntax, statements

print('Variables are containers for storing data values.')
print("Python has no command for declaring a variable.A variable is created the moment you first assign a value to it.")
 
a=1
print(a)
b='two'
print(b)


print('====================')
# casting
print("Casting")

a = "One"
a = 1
print(str(a))
print(float(a))
a = "String"

print('====================')
print("You can get the data type of a variable with the type() function.")
a = 1
b = 'String'
print(type(a))
print(type(b))







# Variables naming
print('====================')
print('Python varible naming rules')
print('A variable name must start with a letter or the underscore character')
print('A variable name cannot start with a number')
print('A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )')
print('Variable names are case-sensitive (age, Age and AGE are three different variables)')
print('A variable name cannot be any of the Python keywords.')


print('====================')
print('variables naming strategies')
print('1) camelCase -Each word, except the first, starts with a capital letter')
print('firstName="Lucky"')


print('2) PascalCase -Each word starts with a capital letter')
print('FirstName="Lucky"')


print('3) snake_case -Each word is separated by an underscore character')
print('first_Name="Lucky"')



# Python Variables - Assign Multiple Values
print('====================')
# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)



print('====================')
# Output Variables
print('The print() function is often used to output variables.')
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print('====================')
print(x+y+z)

print('In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:')
print('====================')

# Global Variables
print('====================')
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

print('====================')
print('local variable')
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
print('====================')

# Global variable
print('====================')
print('To create a global variable inside a function, you can use the global keyword.')
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
print('====================')
print('====================')
print('====================')
print('Hello', 'World')

