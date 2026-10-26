# Random Fun Calculator

# PART 1: Import random and math modules
import random
import math

print("===== AMUSING MATH & LUCK MACHINE =====")

# PART 2: Generate a random lucky number using randrange()
lucky_number = random.randrange(1, 11)  # Generates 1 to 10
print("Your daily fortune number is:", lucky_number)

# PART 3: Turn a random number into a random choice
snack_choices = ["Crunchy apple", "Sweet cookie", "Salty popcorn", "Dark chocolate"]
random_snack = random.choice(snack_choices)
print("Recommended snack for today:", random_snack)

# PART 4: Number guessing game
print("\nGuess the mystery number from 1 to 5!")
secret_number = random.randint(1, 5)

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Spot on! You found the right number.")
        break
    else:
        print("Not quite. Give it another shot!")

# PART 5: Use math module functions
decimal_number = float(input("\nEnter a decimal number: "))

print("Rounded up (Ceiling):", math.ceil(decimal_number))
print("Truncated (Decimal dropped):", math.trunc(decimal_number))

# PART 6: Use copysign()
a = 15
b = -3
print("Signed combination result:", math.copysign(a, b))

# PART 7: Use fabs()
negative_number = float(input("Enter any positive or negative number: "))
print("Absolute distance from zero:", math.fabs(negative_number))

# PART 8: Use lcm()
num1 = int(input("Enter first number for LCM: "))
num2 = int(input("Enter second number for LCM: "))

print("LCM (Least Common Multiple) is:", math.lcm(num1, num2))

# PART 9: Print final summary
print("\n===== FINAL RESULTS SUMMARY =====")
print("Fortune Number:", lucky_number)
print("Suggested Snack:", random_snack)
print("Mystery Number:", secret_number)
print("==================================")
