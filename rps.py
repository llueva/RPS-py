from random import choice

player_wins = 0
computer_wins = 0
rounds_tied = 0

valid_choices = ["rock", "✊", "paper", "✋", "scissors", "✌"]

player_victory_ascii = """\

      .-=========-.
      \'-=======-'/
      _|   .=.   |_
     ((|  {{1}}  |))
      \|   /|\   |/
       \__ '`' __/
         _`) (`_
       _/_______\_
      /___________\
"""


computer_victory_ascii = """\

        |.-----.|
        ||x . x||
        ||_.-._||
        `--)-(--`
       __[=== o]___
      |:::::::::::|
      `-=========-`
"""

tie_art_ascii = """\

    ╔════════╗ ╔══╗ ╔═══════╗  ╔════╗
    ║████████║ ║██║ ║███████║  ║ ██ ║
    ╚══╗██╔══╝ ║██║ ║██╔════╝  ║ ██ ║
       ║██║    ║██║ ║█████╗    ╚════╝
       ║██║    ║██║ ║██╔══╝    ╔════╗
       ║██║    ║██║ ║███████╗  ║ ██ ║
       ╚══╝    ╚══╝ ╚═══════╝  ╚════╝
"""


print("\nWelcome to (RPS) / Rock, Paper, Scissors!")
print("\nYour valid choices are listed below.\n")



#FUNCTIONS:
def display_choices(player_choice, computer_choice):
    print(f"\n{player_name} chose: {player_choice}")
    print(f"The computer chose: {computer_choice}")


def round_winners(player_choice, computer_choice):
    #player_choice == player_choice.lower()
    #computer_choice == computer_choice.lower()
    if (
        player_choice == "rock" and computer_choice == "scissors" or
        player_choice == "paper" and computer_choice == "rock" or
        player_choice == "scissors" and computer_choice == "paper" or
        player_choice == "✊" and computer_choice == "✌" or
        player_choice == "✋" and computer_choice == "✊" or
        player_choice == "✌" and computer_choice == "✋" or
        player_choice == "scissors" and computer_choice == "✋" or
        player_choice == "rock" and computer_choice == "✌" or 
        player_choice == "paper" and computer_choice == "✊" or
        player_choice == "✊" and computer_choice == "scissors" or
        player_choice == "✋" and computer_choice == "rock" or
        player_choice == "✌" and computer_choice == "paper"
    
    ):
        return "Player"
    elif player_choice == computer_choice:
        return "Tie"
    elif (
        player_choice == "✊" and computer_choice == "rock" or
        player_choice == "✋" and computer_choice == "paper" or
        player_choice == "✌" and computer_choice == "scissors" or
        player_choice == "rock" and computer_choice == "✊" or
        player_choice == "paper" and computer_choice == "✋" or
        player_choice == "scissors" and computer_choice == "✌"

    ):
        return "Tie"
    else:
        return "Computer"


def display_game_winner(player_wins, computer_wins):
    if player_wins > computer_wins:
        print(f"{player_name} Wins The Game! Rounds Won: {player_wins}.")
        print(player_victory_ascii)

    elif computer_wins > player_wins:

        print(f"Computer Wins The Game! Rounds Won: {computer_wins}.")
        print(computer_victory_ascii)

    else:
        print("Player and Computer Tied!")
        print(tie_art_ascii)
#ENDOFFUNCTIONS                    


for valid_choice in valid_choices:
    print(valid_choice)

player_name = input("What is your name? ")

#GAMELOOP:
while True:

    player_choice = input("Rock, Paper, or Scissors? ").lower().strip()
    if player_choice not in valid_choices:
        print("Invalid option!")
        player_choice = input("Rock, Paper, or Scissors? ").lower().strip()
        computer_choice = choice(valid_choices)

    computer_choice = choice(valid_choices)

    display_choices(player_choice, computer_choice)
    round_winner = round_winners(player_choice, computer_choice)

    if round_winner == "Player":
        print(f"\n{player_name} wins this round!\n")
        player_wins += 1

    elif round_winner == "Computer":
        print("\nComputer wins this round!\n")
        computer_wins += 1

    elif round_winner == "Try again":
        print("\nThat was an invalid choice! Try again!\n")

    else:

        print("\nThis round was a tie!\n")

    continue_playing = input("Would you like to keep playing? (yes/no) ")

    if continue_playing != "yes":
        break
#ENDOFGAMELOOP
display_game_winner(player_wins, computer_wins)
print(f"Computer Won {computer_wins} Rounds.\n{player_name} Won {player_wins} Rounds.\n")