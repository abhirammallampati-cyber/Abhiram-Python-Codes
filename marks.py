#create and assign values to variables
Math= int(input("Please Enter Your Marks For Math:"))
English=int(input("Please Enter Your Marks for English:"))
Science = int(input("Please Enter Your Marks For Science:"))
SocialStudies=int(input("Please Enter Your Marks Social Studies:"))
Telugu= int(input("Please Enter Your Marks For Telugu:"))

#find the total, average, and percentage
total= Math+English+Science+SocialStudies+Telugu
avg=total/5
percentage=total/500*100

#print total, average, and percentage
print("Total:", total)
print("Average:", avg)
print("Percentage:", percentage)