

spam =0;
print(id(spam),spam)
spam = spam + 4# new object
print(id(spam),spam)
song = "fatima "* spam
print(song)
#this is called replication of string when python interpreter see
#there is one string operator and a number it simply change the string
# now the new string object is fatima fatima fatima fatima
n = 3
hi = " helo " * n # now the new hi should be helo helo helo
print(hi)
# this is only possible with * 
name = " ali"
result = name * 5
print(result)# copy paste