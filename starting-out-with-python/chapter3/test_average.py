# This program gets three test scores and displays
# their average. It congratulates the user if the
# average is a high score.

# The HIGH_SCORE named constant holds the value that is
# considered a high score.

HIGH_SCORE = 95

score_1 = int(input("Enter Score 1: "))
score_2 = int(input("Enter Score 2: "))
score_3 = int(input("Enter Score 3: "))

total = score_1 + score_2 + score_3

average = total // 3

if average > 95:
    print("Congratuations!")
else:
    print("Better luck next time scrub!")