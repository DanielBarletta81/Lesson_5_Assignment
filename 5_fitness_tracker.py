#The aim of this assignment is to create a program that tracks fitness activities and calories burned.

#Task 1: Develop a function to log different fitness activities and their duration.
#For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] and 
#duration = [10, 20, 15] where Dancing corresponds to 10 minutes, 
#Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.

activities = ['Kayaking', 'Hiking', 'Aerobics', 'Tennis', 'Jogging']

duration = [45, 95, 30, 60, 35]

#Task 2: Write a simple function that estimates calories burned based on the activity and duration. 
#For instance, Total calories burned = Duration (in minutes)*3.5

def estimate_calories_burned(activities, duration):
    for i in range(len(activities)):
        calories_burned = duration[i] * 5
        print(f"You were {activities[i]} for {duration[i]} min, and you burned {calories_burned} calories.")
        

estimate_calories_burned(activities, duration)


#Task 3: Create a summary function that provides a report of all activities and 
#total calories burned for the day.

def days_activities(duration):
    total_calorie_burn = sum(duration) * 5
    print(f"You had a very active day today, you went {activities[1]}, {activities[0]}, played a game of {activities[3]}, did {activities[2]}, and at the end of the day, you went {activities[4]}. After all of these activities, you burned a total of {total_calorie_burn} calories!")

days_activities(duration)
