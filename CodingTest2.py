def add(a,b):
    return(a,b)

def subtract(a,b):
    return a-b

def multiply (a,b):
    return a*b

def divide(a, b):
    
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")
    return a / b

def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))


        print(f"Addition: {add(num1, num2)}")
        print(f"Subtraction: {subtract(num1, num2)}")
        print(f"Multiplication: {multiply(num1, num2)}")

        print(f"Division: {divide(num1, num2)}")
    except ZeroDivisionError as e:
            print(e)
            
    except ValueError:
        print("Error: Invalid input! Please enter valid numeric values.")

if __name__ == "__main__":
    main()



