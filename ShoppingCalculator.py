# ================================
# SHOPPING DISCOUNT CALCULATOR
# ================================

# ---------- PART 1: retry loop ----------
valid = False
# Start a while loop that runs while valid is False (while not valid).
while not valid:

    # ---------- PART 2: input and calculation ----------
    # Start a try block.
    try:
        # Ask for the bill, and turn it into a number with float().
        bill = float(input("Enter the total bill amount: $"))
        
        # Ask for the discount percent, and turn it into a number with float().
        discount_percent = float(input("Enter the discount percentage (e.g., 15): "))
        
        # Ask for the number of people, and turn it into a whole number with int().
        people = int(input("Enter the number of people splitting the bill: "))
        
        # Work out the discount amount, the final bill and what each person pays.
        discount_amount = bill * (discount_percent / 100)
        final_bill = bill - discount_amount
        per_person = final_bill / people

    # ---------- PART 3: handle errors ----------
    # except ValueError: print a message about typing numbers only.
    except ValueError:
        print(" Error: Please type valid numbers only.")
        
    # except ZeroDivisionError: print a message that people cannot be 0.
    except ZeroDivisionError:
        print(" Error: The number of people cannot be 0.")

    # ---------- PART 4: else and finally ----------
    # else: print the final bill and what each person pays, then set valid = True.
    else:
        print(f"\n--- Results ---")
        print(f"Discount Amount: ${discount_amount:.2f}")
        print(f"Final Bill: ${final_bill:.2f}")
        print(f"Each Person Pays: ${per_person:.2f}")
        valid = True
        
    # finally: print "Attempt finished."
    finally:
        print("Attempt finished.\n")
