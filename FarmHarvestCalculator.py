#assign values
field1= 50
field2= 90
field3= 70
field4= 105
field5= 145
#average calaculation
total= field1+field2+field3+field4+field5
avg=total/5
#print calculation
print("Total Harvest:", total)
print("Average Harvest:", avg)
#earnings and price
price_per_kg= 20
earnings=total*price_per_kg
print("Total Earnings:Rs.", earnings)
#number of bags
bags= total//10
leftover=total%10
print("Full bags packed:", bags)
print("Leftover grain:", leftover,"kg")
#comparison to last year
last_year=250
print("Better than last year?:", total>last_year)
print("Same as last year?:", total==last_year)
print("At least as good?:", total>=last_year)
#bonus
total+=100
print("After Bonus Crop:",total, "kg")
#seeds saved for next year
total-=50
print("After seed reserve:",total, "kg")
#final bag count
bags=total//15
print("Total Bags:", bags)