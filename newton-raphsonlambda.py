def newton(a):
    x = 0
    x_new = a
    f1 = lambda X: 2*x**2 - 5*x + 3
    f2 = lambda x: 4*x - 5
    loops = 0
    while abs(x_new - x) > 0.000001:
        loops += 1
        print(loops, x_new)
        x = x_new
        x_new = x - f1(x)/f2(x)

    print(f"The number of iteration is {loops} and the root is {x_new}")

newton(100000)
