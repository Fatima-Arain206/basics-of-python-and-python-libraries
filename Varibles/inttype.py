# python is dynamically typed the variable will not created in memory 
#until it is initialized unlike int a;
# this is not possible in java but there is way a = none
# memory allocation python interpreter check the value of variable and then assign in memory like
#if x =9 interP check 9 is integer allocate 4 bytes
x=8
y=9
sum=x+y
print(x-3)
print("sum is",sum)
print(y-8)
x=89
print(x)
sub = x-y
print(sub)
print(y)
pro= y*sum
print("product is ",pro)
div = x/y # floating value
div = x//y # answer in
print(div)
# just declare in python we cannot declare a variable directly
# because python allocate memory by it value
f = None
# print(x+f) this will give error
f = 87
print(f)
f= "hi"
print(f)
print ("x "+f)# now x is a str so it can not be perform addition


# float
a = 5.5
print(f"you run {a} meters")