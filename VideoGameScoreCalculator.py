# Videogame Score Calculator

# Store the scores achieved by 5 individual players
team1 = 120
team2 = 95
team3 = 140
team4 = 110
team5 = 85


# Calculate total and average scores
total = team1 + team2 + team3 + team4 + team5
average = total / 5

print("Total score :", total)
print("Average per player :", average)

# Each point grants 2 bonus experience points
stars_per_point = 2
reward_stars = total * stars_per_point

print("Total bonus EXP :", reward_stars)

# Floor Division (//) and Modulus (%) 
# Convert bonus EXP into skill badges (25 EXP each)
boxes = reward_stars // 25
leftover = reward_stars % 25

print("Skill badges earned :", boxes)
print("Remaining EXP :", leftover)

# Compare this round's score with the high score
last_week = 500

print("New high score? :", total > last_week)
print("Tied high score? :", total == last_week)
print("At least beaten the high score? :", total >= last_week)

# Hidden level bonus adds 30 points to the total
total += 30
print("After hidden level bonus :", total)

# 15 points are deducted for taking damage
total -= 15
print("After damage penalty :", total)

# Final badge count after all score adjustments
reward_stars = total * stars_per_point
boxes = reward_stars // 25
print("Final badges collected :", boxes)
