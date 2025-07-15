import random
user_wins=0
computer_wins=0
options=["rock","paper","scissors"]

while True:
    user_input=input("Enter rock/paper/scissors or q to quit")
    if user_input=="q":
        break
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    #rock=0 paper=1 scissors=2
    computer_pick=options[random_number]
    print("computer picked ",computer_pick+".")
    if user_input=="rock" and computer_pick=="scissors":
      print("You Won")
      user_wins+=1
    elif user_input=="scissors" and computer_pick=="paper":
        print("You Won")
        user_wins+=1
    elif user_input=="paper" and computer_pick=="rock":
        print("You Won")
        user_wins+=1
    else:
        print("You lose")
        computer_wins+=1
if(user_wins!=0 or computer_wins!=0):
    print("Your score:",user_wins)
    print("Computer score:",computer_wins)
print("Good Bye")

