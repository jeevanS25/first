def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("=" * 30)
    print("      Simple Calculator       ")
    print("=" * 30)
    print("Select an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    print("=" * 30)

    while True:
        choice = input("\nEnter choice (1-5): ").strip()

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid selection. Please choose a number from 1 to 5.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result, str):                                                                                                                  
                print(result)
            else:
                print(f"Result: {num1} / {num2} = {result}")

if __name__ == "__main__":
    main()
