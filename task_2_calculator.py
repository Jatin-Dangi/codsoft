def calculator():
    while True:
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
        except ValueError:
            print("Error: Please enter numerical values.")
            continue
        
        print("Select an operation:")
        print("1: Addition +")
        print("2: Subtraction -")
        print("3: Multiplication *")
        print("4: Division / ")
        print("5: Exit")

        operation = input("Enter the number of the selected operation: ")

        if operation == '1':
            result = number1 + number2
            print(f"The result of {number1} + {number2} is: {result}")
        elif operation == '2':
            result = number1 - number2
            print(f"The result of {number1} - {number2} is: {result}")
        elif operation == '3':
            result = number1 * number2
            print(f"The result of {number1} * {number2} is: {result}")
        elif operation == '4':
            if number2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = number1 / number2
                print(f"The result of {number1} / {number2} is: {result}")
        elif operation == '5':
            print("Exiting the calculator")
            break
        else:
            print("Invalid operation choice. Please select a valid operation.")
        
        # Optionally, add a blank line for better readability between iterations
        print()

calculator()
