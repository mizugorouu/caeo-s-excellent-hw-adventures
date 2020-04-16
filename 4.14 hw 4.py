# 4.14 hw numero quatro
# area of a triangle!
# 14 April 2020

import math

print("This script can find the area of one of three shapes.")

check = True

def A():
    while check:
        height = input("Enter value for height: ")
        try:
            height = float(height)
            break
        except ValueError:
            print("Your input \"{}\" is not a number. Try again. \n".format(height))
            continue
    while check:
        base = input("Enter value for base: ")
        try:
            base = float(base)
            break
        except ValueError:
            print("Your input \"{}\" is not a number. Try again. \n".format(base))
            continue
    print("The area of this right triangle is: " + str(float(0.5*height*base)))

def B():
    while check:
        base1 = input("Enter value for base 1: ")
        try:
            base1 = float(base1)
            break
        except ValueError:
            print("Your input \"{}\" is not a number. Try again. \n".format(base1))
            continue
    while check:
        base2 = input("Enter value for base 2: ")
        try:
            base2 = float(base2)
            break
        except ValueError:
            print("Your input \"{}\" is not a number. Try again. \n".format(base2))
            continue
    while check:
        height = input("Enter value for height: ")
        try:
            height = float(height)
            break
        except ValueError:
            print("Your input \"{}\" is not a number. Try again. \n".format(height))
    print("The area of this trapezoid is: " + str(float(((base1+base2)/2)*height)))

# heron's formula for the area of a triangle is actually incorrect: it should be A = sqrt(s(s-a)(s-b)(s-c))
def C():
    while check:
        A = input("Enter value for side A: ")
        try:
            A = float(A)
            break
        except ValueError:
            print("Your input \"{}\" is not a number. Try again. \n".format(A))
            continue
    while check:
        B = input("Enter value for side B: ")
        try:
            B = float(B)
            break
        except ValueError:
            print("Your input \"{}\" is not a number. Try again. \n".format(B))
            continue
    while check:
        C = input("Enter value for side C: ")
        try:
            C = float(C)
            break
        except ValueError:
            print("Your input \"{}\" is not a number. Try again. \n".format(C))
    S = sum([A,B,C])/2
    print("The area of this triangle is: " + str(math.sqrt((S*(S-A)*(S-B)*(S-C)))))

def shape():
    shape = input("What shape would you like to find the area of today? \n (A=right triangle, B=trapezoid, C=non-right triangle): ")
    if shape == "A":
        A()
    elif shape == "B":
        B()
    elif shape == "C":
        C()
    else:
        print("Enter valid input:")
        shape()
shape()