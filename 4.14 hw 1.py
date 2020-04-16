# 4.14 hw numero uno
# calculate third angle in a triangle
# 12 April 2020

print("This script will identify triangles for you.")

#defines retry
def checkAgain(this):
    continueOn = input("Check another integer? Y/N: ")
    if continueOn == "Y":
        this = True
    elif continueOn == "N":
        this = False
    else:
        print("Input \"" + continueOn + "\" not recognized. Try again.")
        checkAgain(this)
    return this

check = True

while check:
    angle_1 = input("Enter angle 1 in degrees: ")
    try:
        angle_1 = int(angle_1)
        if angle_1 < 0 or angle_1 > 180:
            print("Input must be and integer between 0 and 180. Try again: ")
            continue
        break
    except ValueError:
        print("Your input \"{}\" is not an integer. Try again. \n".format(angle_1))
        continue

while check:
    angle_2 = input("Enter angle 2 in degrees: ")
    try:
        angle_2 = int(angle_2)
        if angle_2 < 0:
            print("Input must be a positive integer. Try again: ")
            continue
        break
    except ValueError:
        print("Your input \"{}\" is not an integer. Try again. \n".format(angle_1))
        continue

anglesum = abs(sum([angle_1, angle_2, -180]))

print("Given " + str(angle_1) + "° and " + str(angle_2) + "°, the third angle is " + str(anglesum) + "°.")
if anglesum == "180":
    print("However, this is not a triangle.")
elif angle_1 == 60 and angle_2 == 60:
    print("This is an equilateral triangle.")
elif angle_1 == angle_2:
    print("This is an isosceles triangle.")
else:
    print("This is a scalene triangle.")
check = checkAgain(check)
