# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

score = int(input("Enter your test score: "))

print("Your Score:", score)

if score >= 90:
    print("Your grade is A.")
elif score >= 80:
    print("Your grade is B.")
elif score >= 70:
    print("Your grade is C.")
elif score >= 60:
    print("Your grade is D.")
else:
    print("Your grade is E.")