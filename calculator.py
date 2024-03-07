#function to add 2 numbers
def add(x, y):
    return x+y

#function to subtract 2 numbers
def subtract(x, y):
    return x-y

#function to multiply 2 numbers
def multiply(x, y):
    return x*y

#function to divide 2 numbers
def divide(x, y):
    return x/y

print("select operation")
print("1. add")
print("2. subtract")
print("3. divide")
print("4. multiply")

while True:
    #input from the user
    choice = input("enter choice (1/2/3/4): ")

    #check if the options are valid
    if choice in ('1', '2','3','4'):
        try:
            num1 = float(input("enter first number: "))
            num2 = float(input("enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        #checks if the user want to carry on
        #breaks the while loop
            next_calculation = input("lets do another calculation? (yes/no): ")
            if next_calculation == "no":
                break
        else:
            print("invalid input")
        

