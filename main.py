import random
R="rock"
P="paper"
S="scissors"
options=[R,P,S]

while True:
    user_input=input('Type rock,paper or scissors to play .').lower()
    if user_input not in options:
       print("Enter a valid option next time.")
       continue
    computer_pick =random.choice([R,P,S])
    print('Player', user_input,':' 'CPU', computer_pick, '.')

    if user_input==R and computer_pick==S:
       print('You won!')
    elif user_input==P and computer_pick==R:
       print('You won!')
    elif user_input==S and computer_pick==P:
        print("You won!")
    elif user_input==computer_pick:
        print("It's a tie. Try again.")
        continue
    else:
       print('CPU won!')  
    break
print('Goodbye! ')
