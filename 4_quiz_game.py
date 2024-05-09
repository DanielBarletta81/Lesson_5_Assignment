#Objective:
#The aim of this assignment is to create a quiz game that asks questions and checks answers.

#Task 1: Develop a list of questions and answers.

questions = [("What is the capitol of Rhode Island? ", "Providence"), 
             ("Which NBA team plays home games in Oklahoma City? ", "Thunder"),
             ("Who was the 4th President of the United States? ", "Madison"),
             ("Which Ocean is the largest in the world? ", "Pacific"),
             ("Who created the current Periodic Table of Elements? ", "Mendeleev")
             ]

correct_answers = []
#Task 2: Write a function that quizzes the user and takes their answers.
def quiz_user(questions):
   
    global correct_answers

    for question, right_answer in questions:
        answer = input(f"{question}")
        if answer == right_answer:
            correct_answers.append(answer)
            print(f"Correct! You answered: {right_answer}")
        else:
            print(f"{answer} is incorrect. The right answer was: {right_answer}")


    

quiz_user(questions)
#Task 3: Score the quiz and give the user feedback on their performance.

def score_quiz():
     
    final_score = len(correct_answers) / len(questions) * 100

    if final_score <= 20:
        print(f"Your final score was {final_score}! You really need to study the material more!")
    elif 20 < final_score <= 60:
        print(f"Your final score was {final_score}! You can do better with a little more effort.")
    elif 60 < final_score <= 80:
        print(f"Your final score was {final_score}! Solid work, you know your stuff pretty well.")
    else:
         print(f"Your final score was {final_score}! Fantastic, you aced this quiz, hot shot!")


score_quiz()