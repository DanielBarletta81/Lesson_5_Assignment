#Objective:
#The aim of this assignment is to analyze a set of grades and provide statistics.

# Task 1: Code a function to calculate the average grade.


grades = [98, 67, 45, 77, 84, 83, 72, 91, 60, 71, 80]

class_average = round((sum(grades) / len(grades)))
print(f"The average score for this class was : {class_average}" )


# Task 2: Implement a function to find the highest and lowest grade.
def highest_lowest(grades):

    lowest_grade = min(grades)

    highest_grade = max(grades)

    print(f"The lowest grade in the class was: {lowest_grade}, and the highest score was: {highest_grade}")

highest_lowest(grades)


# Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).

def letter_grades(grades):
    for grade in grades:
        if grade >= 90:
            print(f" You scored a {grade}, your letter grade is: A")
        elif grade >= 80:
             print(f" You scored a {grade}, your letter grade is: B")
        elif grade >= 70:
             print(f" You scored a {grade}, your letter grade is: C")
        elif grade >= 60:
             print(f" You scored a {grade}, your letter grade is: D")
        else:
             print(f" You scored a {grade}, your letter grade is: F")

letter_grades(grades)


