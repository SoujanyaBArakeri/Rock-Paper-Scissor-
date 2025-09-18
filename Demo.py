import random
rock='''
     .-------,
----'   ______)
       (_______)
       (_______)
       (______)
----.__(____)
       
'''
paper='''
     .-------,
----'   ______)______
              _______)
                ________)
              ________)
----._____________)
'''
Scissor='''
     .-------,
----'   ______)______
              _______)
           ____________)
       (______)
----.__(____)
'''
game_images=[rock,paper,Scissor]
user_choice = int(input("Enter your choice: 0  for Rock,1 for Paper,2 for Scissor. "))
if user_choice < 0 or user_choice >= 3:
    print("You entered invalid number,you lose")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose")
    print(game_images[computer_choice])
    if computer_choice == user_choice:
        print("Its a Draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice == 2 and user_choice == 0:
        print("You win")
    elif computer_choice > user_choice:
        print("You lose")
    elif computer_choice < user_choice:
        print("You win")
