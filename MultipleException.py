try:
    number1 = int(input("Enter a number"))
    number2 = int(input("Enter a number")) 
    number = number1 // number2
    print("Result is", number)

except ZeroDivisionError: 
    print("Division by zero is error!")
except ValueError:
    print("Please enter valid whole numbers")
except:
    print("Wrong Input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")