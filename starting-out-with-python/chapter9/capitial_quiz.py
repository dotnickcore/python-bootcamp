"""
    Write a program that creates a dictionary containing the U.S. states as keys, and their capitals
    as values. (Use the Internet to get a list of the states and their capitals.) The program
    should then randomly quiz the user by displaying the name of a state and asking the user
    to enter that state’s capital. The program should keep a count of the number of correct and
    incorrect responses. (As an alternative to the U.S. states, the program can use the names of
    countries and their capitals.)
"""

quiz = {
    "What is the capital of New South Wales?: ": "Sydney",
    "What is the capital of Victoria?: ": "Melbourne",
    "What is the capital of Queensland?: ": "Brisbane",
    "What is the capital of Western Australia?: ": "Perth",
    "What is the capital of South Australia?: ": "Adelaide",
    "What is the capital of Tasmania?: ": "Hobart",
    "What is the capital of Australia Capital Territory?: ": "Canberra",
    "What is the capital of Northern Territory?: ": "Darwin",
    "What is the capital of Jervis Bay Territory?: ": "Jervis Bay Village",
    "What is the capital of Norfolk Island?: ": "Kingston",
    "What is the capital of Christmas Island?: ": "Flying Fish Cove",
    "What is the capital of Cocos (Keeling) Islands?: ": "West Island"
}

def main():
    score = 0

    # Loop through the quiz dictionary
    for question, correct_answer in quiz.items():
        # Ask the question
        user_answer = input(question + " ")
    
        # Check the answer
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}")

    # Display final score
    print(f"\nYour final score is {score}/{len(quiz)}")

main()