#COP 1000C 
#Name: Elias Mandeville
#Desc: This program finds and displays the area, rectangle, etc of values entered by the user

def Intro():
    print("Welcome to my functions")
    print()
    print("Answer all questions ")
    

def GetLengthWidth():
    length = 0.0
    width = 0.0

    while True:
        try:
            length = float(input("Enter a Length: "))
            if length > 0:
                break
            else:
                print("Error, please enter a positive number.\n")
        except:
            print("Not valid, please enter a positive number.")

    while True:
        try:
            width = float(input("Enter a Width: "))
            if width > 0:
                break
            else:
                print("Error, please enter a positive number.\n")
        except:
            print("Not valid, please enter a positive number.")

    return length, width


def RectangleArea(l, w):
    return l * w


def RectanglePerimeter(l, w):
    return 2.0 * (l + w)


def GetRadius():
    radius = 0.0

    while True:
        try:
            radius = float(input("Enter radius: "))
            if radius > 0:
                break
            else:
                print("Error, please enter a positive number.\n")
        except:
            print("Not valid, please enter a positive number.")

    return radius


def CircleArea(r):
    return 3.14 * r * r


def CircleCircumference(r):
    return 2 * 3.14 * r


def PrintInfo(rectArea, rectPer, circArea, cirCum):
    print(f"Rectangle Area: {rectArea}")
    print(f"Rectangle Perimeter: {rectPer}")
    print(f"Circle Area: {circArea}")
    print(f"Circle Circumference: {cirCum}")


def main():
    mylength = 0.0
    mywidth = 0.0
    myradius = 0.0
    myrectarea = 0.0
    myrectper = 0.0
    mycircarea = 0.0
    mycircum = 0.0

    Intro()

    mylength, mywidth = GetLengthWidth()
    myradius = GetRadius()

    myrectarea = RectangleArea(mylength, mywidth)
    myrectper = RectanglePerimeter(mylength, mywidth)
    mycircarea = CircleArea(myradius)
    mycircum = CircleCircumference(myradius)

    PrintInfo(myrectarea, myrectper, mycircarea, mycircum)

    print()
    print("Rectangle with dimensions 10 x 15:", RectangleArea(10, 15))

    print()
    print("Circle with radius 8:", CircleArea(8))

    print(">" * 12, end="")
    print("My functions", end="")
    print("<" * 12)


main()

