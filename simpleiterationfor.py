def simpleiterusingfor(a):
    x = a
    for loops in range (1,101):
        #using a for loop without any accuracy set
        x_new = (2*x**2 + 3)/5
        print(loops, x_new)
        if abs(x_new - x) <0.00001:
            break
        else:
            x = x_new
    print(f"The number of iteration is {loops} and the root is {x_new}")

simpleiterusingfor(0)
