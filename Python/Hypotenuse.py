# A Pythagorean theorem is the relationship between the three sides of a right triangle
# The hypotenuse is the longest side of the right triangle.

# Create a hypotenuse.py program that asks the user for two numbers, a and b, and then calculates the hypotenuse c.

a = int(input("Enter number sor side a: "))
b = int(input("Enter number sor side b: "))

# Also, the square root of something is the same thing as power to the 0.5. So you can actually figure out the square root of something using the exponent operator **: 

c = (a**2 + b**2)**0.5


print(c)