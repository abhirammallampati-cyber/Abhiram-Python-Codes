# ================================
# FUNCTION CALCULATOR
# ================================

# ---------- PART 1: four functions ----------
# Write add(a, b), subtract(a, b), multiply(a, b) and divide(a, b).
# Each one should return its answer. Do not print inside the functions.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("FUNCTION CALCULATOR")

try:
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    
    operation = input("Operation (add, subtract, multiply, divide): ").strip().lower()
    
    if operation == "add":
        result = add(num1, num2)
        print(f"Result: {result}")
    elif operation == "subtract":
        result = subtract(num1, num2)
        print(f"Result: {result}")
    elif operation == "multiply":
        result = multiply(num1, num2)
        print(f"Result: {result}")
    elif operation == "divide":
        result = divide(num1, num2)
        print(f"Result: {result}")
    else:
        print("Unknown operation.")

except ValueError:
    print("Please type numbers only.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

finally:
    print("Thanks for using the calculator!")
