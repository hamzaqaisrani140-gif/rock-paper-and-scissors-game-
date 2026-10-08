win1 = 0
win2 = 0

player1 = input("Player 1 Do you want to play: ")
player2 = input("Player 2 Do you want to play: ")

while player1 == "yes" and player2 == "yes":
    p1 = input("P1 Rock, Paper or Scissors? ")
    p2 = input("P2 Rock, Paper or Scissors? ")

    
    choices = ["rock", "paper", "scissors"]

    
    if p1 not in choices or p2 not in choices:
        print("Invalid choice! Please type only rock, paper or scissors")
    elif p1 == p2:
        print("It's a Tie!")
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "paper" and p2 == "rock") or \
         (p1 == "scissors" and p2 == "paper"):
        print("Player 1 Win!")
        win1 += 1
    else:
        print("Player 2 Win!")
        win2 += 1

    player1 = input("Player 1 Do you want to play: ")
    player2 = input("Player 2 Do you want to play: ")
print(f"Player 1: {win1}")
print(f"Player 2: {win2}")
if win1 > win2:
    print("Player 1 Won the game!!!")
elif win1 < win2:
    print("Player 2 Won the game!!!")
else:
    print("It's a Draw!")