
import random
availablechoices = ["Rock", "Paper", "Scissors"]
AI = random.choice(availablechoices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors?").capitalize()
    ## Conditions of Rock,Paper and Scissors
    if player == AI:
        print("Tie!")
    elif player == "Rock":
        if AI == "Paper":
            print("Better luck next time", AI, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", AI)
            player_score+=1
    elif player == "Paper":
        if AI == "Scissors":
            print("Better try next timetr", AI, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", AI)
            player_score+=1
    elif player == "Scissors":
        if AI == "Rock":
            print("You lose...", AI, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", AI)
            player_score+=1
    elif player=='End':
        print("Result:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break