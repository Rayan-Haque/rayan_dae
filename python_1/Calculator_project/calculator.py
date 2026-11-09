
# Keep running the calculator until the user chooses to exit
while True:

    # Display the calculator menu
    print("\n--- SIMPLE CALCULATOR ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    # Ask the user to choose an operation
    choice = input("Choose an operation (1-5): ")

    # Exit the program if the user chooses 5
    if choice == "5":
        print("Thank you for using the calculator!")
        break

    # Check if the user entered a valid choice
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please try again.")
        continue

    try:
        # Ask the user to enter two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Add the two numbers
        if choice == "1":
            result = num1 + num2
            print("Result:", result)

        # Subtract the second number from the first
        elif choice == "2":
            result = num1 - num2
            print("Result:", result)

        # Multiply the two numbers
        elif choice == "3":
            result = num1 * num2
            print("Result:", result)

        # Divide the first number by the second
        elif choice == "4":

            # Check that the second number is not zero
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print("Result:", result)

    # Show an error if the user enters something that is not a number
    except ValueError:
        print("Invalid input. Please enter numbers.")
