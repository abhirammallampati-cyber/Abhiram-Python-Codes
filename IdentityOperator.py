x = 100

if (type(x)is int):
    print("true")
else:
    print("false")

x = 150.5

if (type(x)is not float):
  print("true")
else:
   print("false")

x = 100

y = 100

if (x is y):
 print("X and Y has the same identity")

y = 150 
if (x is not y):
 print("Both have different identity")
