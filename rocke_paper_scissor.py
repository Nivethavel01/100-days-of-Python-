rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
userinput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
rps = [rock, paper, scissors]
if userinput <0 or userinput>=3:
  print("You typed an invalid number, you lose!")
else:
    print(rps[userinput])
    print("Computer chose:")
    computerinput=random.randint(0,2)
    print(rps[computerinput])
    if userinput==0 and computerinput==2:
        print("You Win")
    elif userinput==2 and computerinput ==1:
        print("You Win")
    elif userinput==1 and computerinput==0:
        print("You Win")
    elif userinput==computerinput:
        print("Match draw")
    else:
        print("You lose")


