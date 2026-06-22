# logical op
# or >>> one condition must true
# and >> all conditions must be true
# not >> inverts true into false,  false into true
tem = 25
is_raining = True
if tem > 35 or tem < 0 or is_raining:
    print("cancel outdoor plane")
else:
    print("continue to out going")