# 4.14 hw numero dos
# grade based on absence
# 13 April 2020

print("What grade should I give this student?")

check = True

# inputs grade percentage into variable percentage
while check:
    percentage = input("Enter student grade percentage: ")
    try:
        percentage = float(percentage)
        break
    except ValueError:
        print("Your input \"{}f\" is not a number. Try again. \n".format(percentage))
        continue

# inputs number of absent days, integer
while check:
    absent = input("Enter numbers of absent days: ")
    try:
        absent = int(absent)
        break
    except ValueError:
        print("Your input \"{}\" is not an integer. Try again. \n".format(absent))
        continue

# 0 or 1 absent days
if absent in (0,1):
    if percentage >= 87:
        print("This student gets an A.")
    elif percentage >= 76 and percentage < 87:
        print("This student gets a B.")
    elif percentage >= 65 and percentage < 76:
        print("This student gets a C.")
    elif percentage >= 54 and percentage < 65:
        print("This student gets a D.")
    else:
        print("This student gets an F.")
# 2-4 absent days
elif absent in (2,3,4):
    if percentage >= 90:
        print("This student gets an A.")
    elif percentage >= 80 and percentage < 90:
        print("This student gets a B.")
    elif percentage >= 70 and percentage < 80:
        print("This student gets a C.")
    elif percentage >= 60 and percentage < 70:
        print("This student gets a D.")
    else:
        print("This student gets an F.")
# "anything else" absent days, basically < 0 or > 5
else:
    if percentage >= 92:
        print("This student gets an A.")
    elif percentage >= 83 and percentage < 92:
        print("This student gets a B.")
    elif percentage >= 74 and percentage < 83:
        print("This student gets a C.")
    elif percentage >= 65 and percentage < 74:
        print("This student gets a D.")
    else:
        print("This student gets an F.")



