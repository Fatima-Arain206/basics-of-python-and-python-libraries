#input() A Function that prompt the user to enter data
# return the data to variable as string


# input() # it is also possible it doesn't need of variable
# input(" Enter your age ")# the give number is string
# a = input()
# print(type(a))#proved
name = input(" Enter your name ")
age = input("how old are you ")
# age+=1 #not possible
age = int(age)
age +=1
print(age)
print(f"Hi  {name}")
print(f"you are {age} years old")

# more use full
a = int(input("enter your money     "))
print(type(a))