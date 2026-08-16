# City and Safari Holiday Planner
# Lesson: Nested Conditional Statements
 
print("====================================")
print("    Welcome to Holiday Planner!     ")
print("====================================")
print()
 
print("Step 1: Pick your holiday type")
print("  1 - City Break")
print("  2 - Safari Adventure")
print()
 
trip_choice = int(input("Enter 1 or 2: "))
print()
 
if trip_choice == 1:
    # Nested if-else - runs only when trip_choice is 1
    print("Step 2: Pick your city activity")
    print("  1 - Museum Tour")
    print("  2 - Shopping")
    print()
 
    city_activity = int(input("Enter 1 or 2: "))
    print()
 
    if city_activity == 1:
        print("You picked  : Museum Tour")
        print("Best time   : Morning")
        print("Remember    : Book your tickets online")
    else:
        print("You picked  : Shopping")
        print("Best time   : Afternoon")
        print("Remember    : Bring a reusable tote bag")
 
elif trip_choice == 2:
    # Nested if-else - runs only when trip_choice is 2
    print("Step 2: Pick your safari activity")
    print("  1 - Game Drive")
    print("  2 - Bird Watching")
    print()
 
    safari_activity = int(input("Enter 1 or 2: "))
    print()
 
    if safari_activity == 1:
        print("You picked  : Game Drive")
        print("Best for    : Seeing big cats")
        print("Remember    : Bring binoculars and camera")
    else:
        print("You picked  : Bird Watching")
        print("Best for    : Finding rare species")
        print("Remember    : Wear neutral-colored clothes")
 
else:
    print("That was not a valid choice.")
    print("Please enter 1 for City Break or 2 for Safari Adventure.")
 
print()
print("====================================")
print("   Your Holiday Plan Is Ready!      ")
print("   Enjoy Your Trip!                 ")
print("====================================")
