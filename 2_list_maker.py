#Objective:
#The aim of this assignment is to create a program that helps users make a shopping list.

#Task 1: Write a function that lets the user add items to a list.
#Task 2: Include a feature to remove items from the list.
#Task 3: Add a function that prints out the entire list in a formatted way.

user_shopping_list = []


def add_items():

    while True:
        items = input('Enter item to add to your shopping list: ')
        if items == 'Done':
            items_to_remove = input(f"What item(s) would you like to remove from the list? {user_shopping_list}" )
            
            if items_to_remove == 'None' or 0 or "":
                 print('Your list is complete!')
                 break
            else:
                user_shopping_list.remove(items_to_remove)
                print(f"{items_to_remove} removed from list, list complete!")
                break
        else:
   
            user_shopping_list.append(items)
            print(f"You added {items} to your list, your current shopping list is: {user_shopping_list}")

            
add_items()



def display_list(user_shopping_list):
        for i in range(len(user_shopping_list)):
    

  
            print(f" Item # {i + 1}. {user_shopping_list[i]}")



display_list(user_shopping_list)
