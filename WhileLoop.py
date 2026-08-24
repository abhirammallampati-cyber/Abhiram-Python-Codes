# My Chore Checklist Countdown


# PART 1: Set today's total number of chores
total_chores = 4
original_count = total_chores


print(f"You have {original_count} chores to finish today!\n")


# PART 2: Counters
completed_count = 0
chore_num = 1


# PART 3: Repeat while there are chores left
while chore_num <= total_chores:


    # PART 4: Get the current chore
    if chore_num == 1:
        next_chore = "Make your bed"
    elif chore_num == 2:
        next_chore = "Feed the pet"
    elif chore_num == 3:
        next_chore = "Take out the trash"
    else:
        next_chore = "Wash the dishes"


    # Ask the user
    answer = input(f"Have you finished: {next_chore}? (yes/no): ").strip().lower()


    # PART 5: Check answer
    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("Great job! Chore completed!")
    else:
        print("Okay, finish it and check again!")


    # PART 6: Remaining chores
    print("Chores remaining:", total_chores - completed_count)
    print()


# PART 7: All chores completed
print("===== ALL CHORES COMPLETE! =====")
print("Great work finishing your entire checklist today!\n")


# PART 8: Safe infinite loop example
print("Now let's safely peek at an infinite loop...")


test_value = 0
safety_counter = 0


while test_value <= 0:
    print("This condition never changes, so this would run forever!")


    safety_counter += 1


    if safety_counter == 3:
        print("(Stopping here on purpose - a real infinite loop never stops on its own!)")
        break


# PART 9: Final summary
print("\n===== CHORE CHECKLIST SUMMARY =====")
print("Chores Assigned Today:", original_count)
print("Chores Completed:", completed_count)
print("Chores Remaining:", total_chores - completed_count)
print("======================================")
