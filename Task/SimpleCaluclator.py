def simple_calulator():
    print("simple calulator")
    n1 = float(input(" enter a number"))
    n2 = float(input(" enter a number"))
    print("chose operation ")
    print("+ ,  - * % / " )
    
    op = input()
    match op:
        case '+':
            return n1+n2
       
        case '-':
            return n1-n2
        case '*':
            return n1*n2
        case '%':
            return n1%n2  
        case '/':
            return n1/n2
        case _:
            print(" enter again ")
op2 = input()
match op2:
        case '+':
            return n1+n2
       
        case '-':
            return n1-n2
        case '*':
            return n1*n2
        case '%':
            return n1%n2  
        case '/':
            return n1/n2
        case _:
            print(" enter again ")


print(simple_calulator())
#simple_calulator()
