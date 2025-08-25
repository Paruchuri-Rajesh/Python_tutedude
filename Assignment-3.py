import math

a=int(input("Enter a Number : "))

def factorial(a):
    if a==1 or a==0:
        return a
    else:
        return a*factorial(a-1)

def Math_mo(a):
    print(f"Square root : {math.sqrt(a)}")
    print(f"Sine : {math.sin(a)}")
    print(f"Logarithm  : {math.log(a)}")


print(f"Factorial of {a} is : {factorial(a)}")
Math_mo(a)