balance = 500

try:
   amount = int(input("Enter withdrawal amount: "))

   if amount <= 0:
      raise Exception("Insufficient balance")

   balance = balance - amount
   print("Withdrawal Successful!")
   print("Remaining balance:", balance)

except ValueError as e:
   print("Invalid amount", e)

except Exception as e:
   print("Transaction failed:", e)

finally:
   print("Thank you for using our ATM!")