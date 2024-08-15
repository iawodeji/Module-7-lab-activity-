#Idris Awodeji
#8.13.2024

#Problem 1
# Import the math module to use mathematical functions and constants
import math

def areaOfCircle(r):
    # Formula for the area of a circle is π * r^2
    area = math.pi * r ** 2
    return area
#example
print(areaOfCircle(1))



#Problem 2
def CheckRange(x):
    # Define the range from 1 to 10
    if x in range(1, 11):
        print(f"The number {x} is in the range 1 to 10.")
    else:
        print(f"The number {x} is not in the range 1 to 10.")
#example
CheckRange(2)   # print that the number 2 is in the range
CheckRange(20)  # print that the number 20 is not in the range



#Problem 3
def Multiplynum(list):
    product = 1
    #Iterate through list and multiply each number to the product
    for numbers in list:
        product *= numbers
    
    return product
#example
list = [5, 2, 7, -1]
result = Multiplynum(list)
print(f"The product of the numbers in the list is {result}")



#Problem 4
def UniqueElements(list):
    # Initialize an empty list to store unique elements
    uniquelist = []
    # Iterate through each number in input list
    for number in list:
        # If number is not in uniquelist, append it
        if number not in uniquelist:
            uniquelist.append(number)
    
    return uniquelist
#example 
numberslist = [1, 3, 3, 3, 6, 2, 3, 5]
uniquenumbers = UniqueElements(numberslist)
print(f"The unique elements in the list are: {uniquenumbers}")



#Problem 5
import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square with side length sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

# Set up the window and turtle
wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

# Draw the first square at the starting position
drawSquare(alex, 15)
# Move the turtle without drawing
alex.penup()          # Lifts  pen so it doesn't draw
alex.goto(-5, -5)   # Moves turtle to the new position 
alex.pendown()        # Puts pen down to start drawing again

# Draw the second square at the new position
drawSquare(alex, 25)
# Move the turtle to a new position for the third square
alex.penup()
alex.goto(-10, -10)   
alex.pendown()

# Draw the third square at the new position
drawSquare(alex, 35)
# Move the turtle to a new position for the fourth square
alex.penup()
alex.goto(-15, -15)   
alex.pendown()

# Draw the fourth square at the new position
drawSquare(alex, 45)
# Move the turtle to a new position for the fifth square
alex.penup()
alex.goto(-20, -20)   
alex.pendown()

# Draw the fifth square at the new position
drawSquare(alex, 55)

# Close the window when clicked
wn.exitonclick()



#Problem 6
#In a python class, an attribute is a variable storing data, while a method
#is a function that defines behavior or actions the object can perform.

class car:
    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color + ' ' + self.type + ' ' + self.manufacturer


car1 = car("Sports", 2012, "Blue", "Model S", "Tesla")
car2 = car ("Sedan", 2020, "Black", "Camry", "Toyota")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())

