a=int(input("Enter the number : "))
if a%2==0:
    print("Even Number")
else:
    print("odd Number ")


sum=0
for i in range(1,51):
    sum=sum+i

print(f"The sum of numbers from 1 to 50 is :  {sum}")