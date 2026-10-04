# Bill & Seating Helper 

# PART 1: Define a function using positional arguments 
def total_bill(bill_amount, tip_perc): 
    # Calculate tip amount and add it to the bill
    tip_amount = bill_amount * (tip_perc / 100)
    total = round(bill_amount + tip_amount, 2)
    print(f"Your total bill is: ${total}") 
    return total 

# PART 2: Call the function with positional arguments 
total_bill(120, 15) 

# PART 3: Define a recursive function with a docstring 
def seating_arrangements(guests): 
    '''Calculates total possible seating arrangements for a given number of guests recursively.''' 
    # Base case: 0 or 1 guest has only 1 way to sit
    if guests <= 1: 
        return 1 
    # Recursive case 
    else: 
        return guests * seating_arrangements(guests - 1) 

# PART 4: Access and print the docstring 
print("Function Purpose:", seating_arrangements.__doc__) 

# PART 5: Display seating arrangement results 
print("Arrangements for 1 guest:", seating_arrangements(1)) 
print("Arrangements for 2 guests:", seating_arrangements(2)) 
print("Arrangements for 4 guests:", seating_arrangements(4)) 
print("Arrangements for 6 guests:", seating_arrangements(6)) 
