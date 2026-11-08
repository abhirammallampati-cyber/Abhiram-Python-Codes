# Create an empty list
empty_list = []
print(empty_list)

# PART 1: Create a list of product prices
prices = [45, 12, 90, 33, 78]
print("Product Prices:", prices)

# PART 2: Use * operator to repeat a sample prices list
sample_prices = [5, 10, 15] * 2
print("Repeated Sample Prices:", sample_prices)

# PART 3: Find the length of the prices list
print("Number of items:", len(prices))

# PART 4: Access items using indexing
print("First price:", prices[0])
print("Last price:", prices[-1])

# PART 5: Access a range using slicing
first_three_prices = prices[0:3]
print("First three prices:", first_three_prices)

# PART 6: Reverse the prices list using slicing
reversed_prices = prices[::-1]
print("Reversed Prices:", reversed_prices)

# PART 7: Function to find prices that start and end with same digit
def match_prices(price_list):
    count = 0
    matched_prices = []
    
    for price in price_list:
        price_text = str(price)
        
        if len(price_text) > 1 and price_text[0] == price_text[-1]:
            count += 1
            matched_prices.append(price)
            
    print("Prices with first and last digit same:", matched_prices)
    return count

same_digit_count = match_prices([55, 12, 99, 34, 88])
print("Number of matching prices:", same_digit_count)

# PART 8: Iterate through the list to find sum and average
total = 0

for price in prices:
    total += price

average = total / len(prices)

print("Sum of prices:", total)
print("Average price:", average)

# PART 9: Sort the list to find smallest and largest prices
prices.sort()

print("Smallest price is:", prices[0])
print("Largest price is:", prices[-1])

# PART 10: Print the final product inventory summary
print("")
print("===== PRODUCT INVENTORY ANALYZER =====")
print("Sorted Prices:", prices)
print("Total Inventory Value:", total)
print("Average Product Price:", average)
print("Cheapest Item:", prices[0])
print("Most Expensive Item:", prices[-1])
print("======================================")
