actual_cost=float(input("Enter the Actual Cost:"))
sale_profit=float(input("Enter the Profit After Sale:"))
amount=sale_profit-actual_cost
if (actual_cost > sale_profit):
    print("This is a Loss by", amount,"Rupees")

else:
    print("This is a Profit", amount, "Rupees") 