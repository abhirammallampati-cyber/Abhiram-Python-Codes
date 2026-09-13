# Loop Art Designer (Modified Edition)
 
# PART 1: Inverted Star triangle pattern
print("===== INVERTED STAR PATTERN =====")
 
rows = int(input("Enter number of rows for star pattern: "))
 
# Modified to count backwards to invert the triangle
for i in range(rows, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()
 
 
# PART 2: Repeating Row Grid pattern
print("\n===== REPEATING ROW TRIANGLE =====")
 
rows = int(input("Enter number of rows for Triangle: "))
 
# Modified so each row resets its starting number to match the row index
for i in range(1, rows + 1):
    number = i
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
    print()
 
 
# PART 3: Textured Border Diamond pattern
print("\n===== TEXTURED DIAMOND PATTERN =====")
 
row_size = int(input("Enter number of rows for diamond pattern: "))
 
if row_size % 2 == 0:
    half_rows = row_size // 2
else:
    half_rows = row_size // 2 + 1
 
space = half_rows - 1
 
# Upper half of diamond
for i in range(1, half_rows + 1):
    for j in range(1, space + 1):
        print(" ", end="")
 
    space -= 1
 
    # Modified to alternate between '+' and '-' to create a textured pattern
    for j in range(2 * i - 1):
        if j % 2 == 0:
            print("+", end="")
        else:
            print("-", end="")
 
    print()
 
# Lower half of diamond
space = 1
 
for i in range(1, half_rows):
    for j in range(1, space + 1):
        print(" ", end="")
 
    space += 1
 
    # Modified to maintain the alternating textured pattern in the bottom half
    for j in range(1, 2 * (half_rows - i)):
        if j % 2 == 0:
            print("+", end="")
        else:
            print("-", end="")
 
    print()
 
 
# PART 4: Final message
print("\n===== LOOP ART DESIGN COMPLETE =====")
print("You created inverted, grid, and textured diamond patterns using nested loops!")
