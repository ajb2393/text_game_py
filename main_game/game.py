#Welcome to Greed Island

print("Escape from Greed Island -_-")
action_input = input("Where would you like to go?:\n")

if action_input == 'n':
    print("You're moving North")
elif action_input == 'e':
    print("You're moving East")
elif action_input == 's':
    print("You're moving South")
elif action_input == 'w':
    print("You're moving West") 
else: 
    print("The submitted direction is wrong; try again")


