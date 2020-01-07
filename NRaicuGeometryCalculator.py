#20200106
#Geometry Calculator by Naomi Raicu

import math

#The information that pops up when you first open the calculator
print("Hello! Welcome to the Geometry Calculator. Use the menu \
and enter in a given input to continue.")
#This function prints the list of options you can choose from for the calculator
def callMenu():
    """Prints the menu when called"""
    print("Menu: \
    \n Area of a triangle (enter 'triangleArea') \
    \n Area of a square (enter 'squareArea') \
    \n Area of a parallelogram (enter 'paraArea') \
    \n Area of an ellipse (enter 'ellipseArea')\
    \n Area of a circle (enter 'circleArea')\
    \n Circumference of a circle (enter 'circleCirc')\
    \n Enter 'quit' to quit.\
    \n Enter 'menu' to show the menu again.")

callMenu()


#The list of functions:
functionlist = ['triangleArea', 'squareArea', 'paraArea', \
'ellipseArea', 'circleArea', 'circleCirc']

#A bunch of functions for each type of geometric calculation
def triangleArea(base, height):
    """Calculates the area of a triangle based on user inputs"""
    base = float(base)
    height = float(height)
    area = 0.5*base*height
    return area
    
def squareArea(sidelength):
    """Calculates the area of a square"""
    sidelength = float(sidelength)
    return sidelength**2
    
def paraArea(base, height):
    """Calculates the area of a parallelogram"""
    base = float(base)
    height = float(height)
    return base*height
    
def ellipseArea(semiMajor, semiMinor):
    """Calculates the area of an ellipse"""
    semiMajor = float(semiMajor)
    semiMinor = float(semiMinor)
    return math.pi*semiMajor*semiMinor

def circleArea(radius):
    """Calculates the area of a circle"""
    radius = float(radius)
    return math.pi*(radius**2)

def circleCirc(radius):
    """Calculates the circumference of a circle"""
    radius = float(radius)
    return 2*math.pi*radius

#This loop keeps the calculator open for as long as the user wants.
while True:
    answer = input("Enter here: ")

    #The if statements that determine what happens based on the user input
    if answer == 'triangleArea':
        base = input("Enter the magnitude of the base: ")
        height = input("Enter the magnitude of the height: ")
        print("The area of the triangle is " + str(triangleArea(base, height)))
    elif answer == 'squareArea':
        sidelength = input("Enter the magnitude of the square's side: ")
        print("The area of the square is " + str(squareArea(sidelength)))
    elif answer == 'paraArea':
        base = input("Enter the magnitude of the base: ")
        height = input("Enter the magnitude of the height: ")
        print("The area of the parallelogram is " + str(paraArea(base, height)))
    elif answer == 'ellipseArea':
        semiMajor = input("Enter the magnitude of the semi-major axis: ")
        semiMinor = input("Enter the magnitude of the semi-minor axis: ")
        print("The area of the ellipse is " + str(ellipseArea(semiMajor, semiMinor)))
    elif answer == 'circleArea':
        radius = input("Enter the radius of the circle: ")
        print("The area of the circle is " + str(circleArea(radius)))
    elif answer == 'circleCirc':
        radius = input("Enter the radius of the circle: ")
        print("The circumference of the circle is " + str(circleCirc(radius)))
    #allows user to quit
    elif answer == 'quit':
        break
    elif answer == 'menu':
        callMenu()
    else:
        print("That's not a valid input. Please try again.")
        
    