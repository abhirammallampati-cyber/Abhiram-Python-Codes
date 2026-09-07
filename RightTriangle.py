print("=== Right Angle Triangle ===")
n = int(input("Enter an Integer:"))
for i in range(n):
    for j in range(i+1):
     print("*", end = "")
    print()

rows = int(input("Please enter the total number of rows: "))
number = 1 

print("Floyd's Triangle")
for i in range(1, rows + 1):
  for j in range(1, i + 1):
    print(number, end = '  ')
    number += 1
  print()