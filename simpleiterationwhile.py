from math import *
def simpleiterusingfor(a):
    x = 0
    x_new = a
    counter = 0
    while abs(x_new - x) > 0.000001:
        #using a while loop without any accuracy set
        x = x_new
        x_new = sqrt((3+5*x)/5)
        counter += 1
        print(counter, x_new)
    print(f"The number of iteration is {counter} and the root is {x_new}")

simpleiterusingfor(10)
