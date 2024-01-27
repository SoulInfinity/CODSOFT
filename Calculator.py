def add(x, y):

    return x + y
def sub(x, y):

    return x - y
def mul(x, y):

    return x * y
def div(x, y):

    if y == 0:
        return "Error: Cannot divide by 0!"
    else:
        return x / y
def calc():
    print("Simple Calculator")

    print("Operations:")

    print("1. Addition (+)")

    print("2. Subtraction (-)")

    print("3. Multiplication (*)")

    print("4. Division (/)")

    choice = input("Enter operation choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))

    num2 = float(input("Enter second number: "))

    if choice == '1':

        print("Result:", add(num1, num2))

    elif choice == '2':

        print("Result:", sub(num1, num2))

    elif choice == '3':

        print("Result:", mul(num1, num2))

    elif choice == '4':

        print("Result:", div(num1, num2))

    else:

        print("Invalid operation choice.")
calc()
