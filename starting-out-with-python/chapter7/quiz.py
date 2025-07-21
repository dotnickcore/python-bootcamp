"""
    The local driver's license office has asked you to create an application that grades the written
    portion of the driver's license exam. The exam has 20 multiple-choice questions. Here
    are the correct answers:
    1. A
    2. C
    3. A
    4. A
    5. D
    6. B
    7. C
    8. A
    9. C
    10. B
    11. A
    12. D
    13. C
    14. A
    15. D
    16. C
    17. B
    18. B
    19. D
    20. A
    Your program should store these correct answers in a list. The program should read the
    student's answers for each of the 20 questions from a text file and store the answers in
    another list. (Create your own text file to test the application.) After the student's answers
    have been read from the file, the program should display a message indicating whether the
    student passed or failed the exam. (A student must correctly answer 15 of the 20 questions
    to pass the exam.) It should then display the total number of correctly answered questions,
    the total number of incorrectly answered questions, and a list showing the question numbers
    of the incorrectly answered questions.
"""

def main():
    users_answers = return_answers_by_user()
    valid_answers = return_quiz_answers_from_txt_file()
    print("Users", users_answers)
    print("Valid", valid_answers)
    total_answers_correct = assess_quiz_answers(users_answers, valid_answers)
    hasStudentPassed = has_student_passed(total_answers_correct)

    message = ""

    if (hasStudentPassed):
        message = "Passed"
    else:
        message = "Failed"

    print()
    print(f"Student Has Scored {total_answers_correct} out of 20")
    print(f"Student Has {message}")
    print()

def return_quiz_answers_from_txt_file():
    # Open a file for reading.
    infile = open('quiz_answers.txt', 'r')

    # Read the contents of the file into a list.
    quiz_answers = infile.readlines()

    # Close the file.
    infile.close()

    # Strip the \n from each element.
    index = 0
    while index < len(quiz_answers):
        quiz_answers[index] = quiz_answers[index].lower().rstrip('\n')
        index += 1

    # Print the contents of the list.
    return quiz_answers

def assess_quiz_answers(user_answers_list, valid_answers_list):
    total_correct_answers = 0
    
    for user_answer, correct_answer in zip(user_answers_list, valid_answers_list):
        if user_answer == correct_answer:
            total_correct_answers += 1
    
    return total_correct_answers

def return_answers_by_user():
    user_answers = []

    for x in range(20):
        while True:
            user_input = input(f"Enter your choice for Question {x+1} (A, B, C, or D): ").strip().lower()
            
            match user_input:
                case "a" | "b" | "c" | "d":
                    user_answers.append(user_input)
                    break
                case _:
                    print("Invalid Input: Enter A, B, C, or D")

    return user_answers

def has_student_passed(answers_correct):
    return 15 <= answers_correct <= 20

main()