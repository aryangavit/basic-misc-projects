#Simple caluclator in python

def add(num1,num2):
    return num1 + num2

def subract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1 * num2

def division(num1,num2):
    return num1 / num2

print("Select the operaton you want to perform:\n"\
    "1. Add\n" \
    "2. Subract\n" \
    "3. Multiply\n" \
    "4. Divide\n" )

usr_input = int(input("Select operations from 1,2,3,4:"))
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

if usr_input == 1:
    print("Result of addition is: ",add(num_1,num_2))

elif usr_input == 2:
    print("Result of Subraction is:",subract(num_1,num_2))

elif usr_input == 3:
    print("Result of multiplication is:",multiply(num_1,num_2))

elif usr_input == 4:
    print("Result of division is:",division(num_1,num_2))

else:
    print("Invalid input")