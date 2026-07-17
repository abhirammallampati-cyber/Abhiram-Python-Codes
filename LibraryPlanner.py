# --- Library Visit Guide ---

print("=== Library Visit Guide ===")
print("Answer 3 quick questions and I will check your library options!\n")

day_of_week = input("What day is it? (Monday to Sunday): ").strip().capitalize()
weather_now = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
has_return  = input("Do you have a book to return? (yes / no): ").strip().lower()

print()
print(f"=== Your Library Options for {day_of_week} ===")
print("." * 35)

# Topic 1 -- if-elif-else: classify the day
if day_of_week in ("Saturday", "Sunday"):
    print("Day details : Weekend - a great time for a relaxed library visit!")
elif day_of_week == "Monday":
    print("Day details : Start of the week. Review your reading list.")
elif day_of_week == "Friday":
    print("Day details : Last school day. Drop off books before the weekend.")
elif day_of_week in ("Tuesday", "Wednesday", "Thursday"):
    print("Day details : Regular school day. Plan a quick library visit.")
else:
    print("Day details : Day not found. Please check your spelling.")

# Topic 2 -- AND operator: sunny AND book due
if weather_now == "sunny" and has_return == "yes":
    print("Library tip : Fine weather! Return your book and find a new one.")

# Topic 3 -- OR operator: rainy OR cloudy
if weather_now == "rainy" or weather_now == "cloudy":
    print("Weather tip : Take an umbrella if you are going to the library.")

# Topic 4 -- NOT operator: book NOT due
if not (has_return == "yes"):
    print("Book status : No book return required today. You can look for new books.")

# Topic 5 -- Combining AND + OR + NOT together
if weather_now == "rainy" and has_return == "yes":
    print("Main plan   : Visit the library carefully and return your book on time.")
elif weather_now == "sunny" and has_return == "yes" and not (day_of_week in ("Saturday", "Sunday")):
    print("Main plan   : Stop by the library after school and return your book.")
elif day_of_week in ("Saturday", "Sunday") and weather_now == "sunny":
    print("Main plan   : Perfect day for a longer reading session at the library!")
else:
    print("Main plan   : Check your schedule and plan a basic library visit.")

print()
print("Library guide complete! Enjoy your reading!")
