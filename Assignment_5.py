# Task 1: Create a Dictionary of Student Marks

dict1={"Rajesh" :40,"Avinash":50,"Tara" :35,"Cannur":26}
Name=input("Enter the student name : ")
if Name in dict1:
    print(f"{Name}'s marks : {dict1[Name]}")
else:
    print("Looks like the student's Marks are not found")


# Task 2: Demonstrate List Slicing

l1=[i for i in range(1,11)]
print(f"Original List : {l1}")
print(f"Extracted first five elements : {l1[0:5]}")
l2=l1[0:5]
l2.reverse()
print(f"Reversed extracted elements : {l2}")