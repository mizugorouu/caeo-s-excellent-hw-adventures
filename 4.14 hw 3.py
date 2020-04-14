# 4.14 hw numero tres
# quadratic equation...
# I had to relearn quadratic formula in the time I did this problem. :I
# 14 April 2020

import math
print("This script will solve the quadratic formula for you.")

check = True

while check:
    A = input("Enter value for A as an integer: ")
    try:
        A = int(A)
        break
    except ValueError:
        print("Your input \"{}\" is not a number. Try again. \n".format(A))
        continue

while check:
    B = input("Enter value for B as an integer: ")
    try:
        B = int(B)
        break
    except ValueError:
        print("Your input \"{}\" is not a number. Try again. \n".format(B))
        continue

while check:
    C = input("Enter value for C as an integer: ")
    try:
        C = int(C)
        break
    except ValueError:
        print("Your input \"{}\" is not a number. Try again. \n".format(C))
        continue

discriminant = B**2 - 4*A*C
xpos = int((-B + math.sqrt(discriminant))/2*A)
xneg = int((-B - math.sqrt(discriminant))/2*A)

if discriminant < 0:
    print("There are no real solutions X.")
elif discriminant == 0 or xpos == xneg:
    print("There is one real number solution X.")
    print("x = " + str(xpos))
else:
    print("There are two real number solutions X.")
    print("x = " + str(xpos) + "," + str(xneg))