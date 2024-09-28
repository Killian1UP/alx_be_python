def perform_operation(num1, num2, operation):
    if operation == '+':
        sum = num1 + num2
        return sum
    elif operation == '-':
        sum = num1 - num2
        return sum
    elif operation == '*':
        sum = num1 * num2
        return sum
    elif operation == '/':
        if num2 != 0:
            sum = num1 / num2
            return sum
        else:
            print("Error! You divided with zero.")
    else:
        print("You did not use the correct operation sign.")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ")

result = perform_operation(num1, num2, operation)
print(f"Result: {result}")
