from math import *
def simpleiterusingfor(a):
    x = a
    for loops in range (1,101):
        #using a for loop without any accuracy set
        x_new = sqrt((3+5*x)/5)
        print(loops, x_new)
        if abs(x_new - x) < 0.0000001 :
            break
        else:
            x = x_new
    print(f"The number of iteration is {loops} and the root is {x_new}")

simpleiterusingfor(100000)
