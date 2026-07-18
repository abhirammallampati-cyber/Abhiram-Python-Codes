# Create marks variables
math = int(input("Enter Your Marks for Math:"))
english = int(input("Enter Your Marks for English:"))
science = int(input("Enter Your Marks for Science:"))
social_studies = int(input("Enter Your Marks for Social Studies:"))
hindi = int(input("Enter Your Marks for Hindi:"))

# find average for marks
total = math + english + science + social_studies + hindi
avg = total/5
print(total)
print(avg)

# marks range
validrange = range(0,101)

# if there is invalid range
if avg not in validrange:
   print("Invalid Input")

# marks grades based on range 
elif avg in range (91,101):
    print("Your Grade is A+")

elif avg in range (81,91):
    print("Your Grade is A-")

elif avg in range (71,81):
    print("Your Grade is B+")

elif avg in range (61,71):
    print("Your Grade is B-")

elif avg in range (51,61):
    print("Your Grade is C+")

elif avg in range (41,51):
    print("Your Grade is C-")

elif avg in range (31,41):
    print("Your Grade is D+")

elif avg in range (21,31):
    print("Your Grade is D-")

elif avg in range (11,21):
    print("Your Grade is E+")

elif avg in range (1,11):
    print("Your Grade is E-")

