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

#all of the above but also demonstrating accountability for capital letters 

if action_input == 'n' or action_input == 'N':
    print("You're going North, Soldier")
elif action_input == 'e' or action_input == 'E':
    print("You're going East, Soldier")
elif action_input == 's' or action_input == 'S': 
    print("You're going South, Soldier")
elif action_input == 'w' or action_input == 'W':
    print("You're going West, Soldier")
else: 
    print("You're going nowhere at all")



