# define the funcations needed: add, sub, mul, div
# print options to user
#  ask for the values
# call the funcations
# while loop to continue the program until the user wants to exit


from secrets import choice


def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer)+ "\n")

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b)+ " = " + str(answer)+ "\n")

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer)+ "\n")

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b)+ " = " + str(answer)+ "\n")
    


print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")


choice = input("input your choice: ")

if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    add(a, b)

elif choice =="b" or choice == "B":
    print("Substructio")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    sub(a, b)

elif choice == "c" or choice == "C": 
    print("Multipication")
    a = int(input("Enter the first number: ")) 
    b = int(input("Enter the second number"))
    mul(a, b)
elif choice == "d" or choice == "D":
    print("Divivsion")
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    div(a, b)

elif choice =="e" or choice =="E": 
    print("Exit")
    quit()