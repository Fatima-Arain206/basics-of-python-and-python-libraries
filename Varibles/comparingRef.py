import Booleans as bl
#hence we know that from -5 to 256 these objects are already
# allocate in ram 
a = 9
b =9# the a and b have same address of 9 because 9 is object and created 
# once in RAm
#prove
print(id(a),"a")# this will print exact address of memory a has address 14070749 ...
print(id(b),"b")
#hence this is proved
# lets check with another builtin fun this will show address in hex decimal number
print(hex(id(a)),"a")
print(hex(id(a)),"b")
#another prove to compare like java has .equal fun to compare two str and == to compare
#two ref python has (is) fun 
print(a is b)# true
#now w understand about that python has not any variable
# concepts which can vary a value but it can vary address
#example
c = 789
print(id(c)) 
c=786
print(id(c),"c")
# here c's value is not changed but python create a new object
# c pointer set on the next val
d = 786
print(id(d),"d")
print (c is d)# why this is true? because these two lines are in same 
# block code thats why python did not make another object of same value
# but this will false in terminal
d = "f"
print (c is d)# now thi is false
print(bl.is_student
      )

