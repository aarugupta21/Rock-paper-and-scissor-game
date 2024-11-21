import random
rock='''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images=[rock,paper,scissor]
user = int(input("What do you want to choose? Type 1 for rock, 2 for paper and 3 for scissors"))
if user>=0 and user<=2:
    print("You choose:")
    print(images[user])
computer = random.randint(0,2)
print("Computer chooses:")
print(images[computer])
if user>=3 or user<0:
    print("You typed an invalid number.")
elif user==computer:
    print("Match is draw")
elif user==0 and computer==2:
    print("You win")
elif user==2 and computer==0:
    print("Computer wins")
elif computer>user:
    print("Computer wins")
elif user>computer:
    print("You win")

