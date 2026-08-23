# Get input from the user
base = float(input("Enter the base number: "))
n = int(input("Enter the maximum power (n): "))

print(f"\nCalculating powers of {base} up to {n}:")

# Initialize result
current_power = 1

# Use a loop to calculate powers from 1 to n
for i in range(1, n + 1):
  current_power *= base
  print(f"{base}^{i} = {current_power}")
