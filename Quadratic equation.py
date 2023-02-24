import math
print("if the quadratic equation is of the ax^2+bx+c")
a=int(input("Enter coefficient of x square i.e., x"))
b=int(input("Enter the coefficient of x i.e., b"))
c=int(input("Enter the constant c"))

if a==0:
    print("the coefficients do not form a quadratic equation")

discriminant=b**2-(4*a*c)

if discriminant==0:
    root1=root2=(-b)/(2*a)
    print(f"the roots are real and equal, the roots are {root1},{root2}")
elif discriminant > 0:
    root1= (-b+math.sqrt(discriminant))/(2*a)
    root2= (-b-math.sqrt(discriminant))/(2*a)
    print(f"the roots are {root1},{root2}")
else:
    real=-b/(2*a)
    imaginary= math.sqrt(-discriminant)/(2*a)
    print(f"the real part of the root is {real} and the imaginary part is {imaginary}")