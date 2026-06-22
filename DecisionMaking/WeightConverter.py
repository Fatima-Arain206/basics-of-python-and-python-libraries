# weight converter


weight = float(input("Please enter your weight: "))
unit = input("Please enter your unit: \n Kilograms or Pounds (K or L)")
if unit == 'K':
    weight = weight * 2.205
    unit = "LBS"
    print(f" your weight is {weight} in {unit} ")
elif unit == "P":
    weight = weight /2.205
    unit = "KGs"
    print(f" your weight is {weight} in {unit} ")
else:
    print("invalid input")

