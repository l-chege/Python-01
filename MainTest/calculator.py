# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers, handling division by zero
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Main calculator function
def calculator():
    print("Simple Calculator")

    # Taking user input for the first and second numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Displaying available operations
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Taking user input for the desired operation
    choice = input("Select operation (1/2/3/4): ")

    # Checking the user's choice and performing the corresponding operation
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operation = '/'

        # Displaying the result of the operation
        print(f"{num1} {operation} {num2} = {result}")
    else:
        # Handling invalid user input
        print("Invalid input. Please select a valid operation.")

# Testing the calculator function
calculator()
