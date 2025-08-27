
try:
    i = 1
    # Try opening the file in read mode
    with open('sample.txt', "r+") as file:
        print("Reading file content : ")
        for line in file:
            print(f"Line {i} : {line.strip()}")  # strip() removes newline characters
            i+=1
except FileNotFoundError:
        print(f"Error: The file '{"sample.txt"}' was not found.")



g=input("Enter text to write to the file : ")
with open("output.txt","w") as file1:
    file1.write(g + '\n')
    print("Data successfully written to output.txt")

a=input("Enter additional text to append : ")
with open("output.txt",'a') as file2:
    file2.write(a)
    print("Data Successfully appended.")

print("Final content of output.txt : ")
with open ("output.txt",'r') as file3:
    content=file3.read()
    print(content)






