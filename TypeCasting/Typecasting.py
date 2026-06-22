# typing casting is a process to converting a variable to
# str(), int(), float(),bool()
name = ''# str type
age = 30
gpa = 3.56
is_student = True
#there is a function type() to know the data type of variable
print(type(name))
print(type(age))
print(type(gpa))
print(id(gpa))
print(type(is_student))
# lets type cast
gpa = int(gpa)# now this will be integer a new object
print(gpa)
print(id(gpa))# it is useful when takes input and data is coming from another site
# example
gp = 7#input()
   #sum = gp+gpa# it will give error
# the gp is ans str it cannot be add
sum = int(gp)+gpa
print(sum)
print(type(gp))
name = bool(name)

print(name) # if the string is empty it gives false other wise give true

Name = input(" Enter Your Name ")
if bool(Name):
    print(f"you entered {Name}")
else:
    print("you did not enter any name")


agee = input()
#user input is always a string