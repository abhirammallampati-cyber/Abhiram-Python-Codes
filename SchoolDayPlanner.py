#questions and inputs
print("=== School Day Planner ===")
print("Answer some questions to plan your day!\n")

day=input("What Day of the week is it?").strip().capitalize()
weather=input("What is the weather outside").strip().lower()
homework= input("Did you do your homework?").strip().lower()

print()
print(f"Your Plan For {day}")
print("-" * 35)

#if-elif-else statements
if day in ("Saturday","Sunday"):
   print("Day type : Weekend - Enjoy Your Free Time")
elif day == "Monday":
   print("Day type : First day of the week! Get ready and plan everything for the week.")
elif day == "Friday":
   print("Day type : Last School Day! Finish your assignments and Homework!")
elif day in ("Tuesday,", "Wednesday", "Thursday"):
   print("Day type : Normal School Day. Work Hard and Stay Focused!")
else:
   print("Day type : Day not recognized. Please check the spelling.")

#operators(and,not,or)
if weather == "rainy" or weather == "cloudy":
   print("Pack your umbrella- it may rain outside!")
if not (homework == "yes"):
   print("Homework : Not done yet. Finish it before going outside!")
if weather == "rainy" and (homework == "yes"):
   print("The best plan is to stay home, do your homework, and watch TV.")
