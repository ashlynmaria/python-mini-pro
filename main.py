# Task 1 - Variables

name = "Ashlyn"
age = 21
height = 5.3 # I am NOT this tall :)

print(f"Hi there, my name is {name}! I’m {age} years old and {height} feet tall. Great to meet you, future bestie! 😄👋")

# Task 2 - Operators

num1 = 12
num2 = 6

# Let's add some math :)
print() # extra space

# Adding num1 and num2
print("The sum of", num1, "and", num2, "is", num1 + num2)

# Subtracting num2 from num1
print("The difference when we subtract", num2, "from", num1, "is", num1 - num2)

# Multiplying both numbers
print("Multiplying", num1, "and", num2, "gives us", num1 * num2)

# Dividing num1 by num2
print("And dividing", num1, "by", num2, "? That's", num1 / num2, "— the math is mathing ✨")

# Task 3 - Conditional Statements

number = int(input("Enter your number!")) 

 
# In the case that the number is positive
if number > 0:
    print("This number is positive. Awesome!")
# In the case that the number is negative
elif number < 0:
    print("This number is negative. Better luck next time!")
# In the case that the number is zero
else:
    print("This number is zero. A perfect balance!")
