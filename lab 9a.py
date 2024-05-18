#NAMES
#Mingxuan Yue
# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)

class RockPaperScissors:
    choices = ['rock', 'paper', 'scissors']
    
    def __init__(self):
        self.results = {'wins': 0, 'losses': 0, 'ties': 0}

    def get_computer_choice(self):
        return random.choice(self.choices)

    def get_human_choice(self, player_number):
        while True:
            choice = input(f'Player {player_number}, pick one of rock, paper, or scissors: ').lower()
            if choice in self.choices:
                return choice
            print("Invalid choice. Please try again.")

    def determine_winner(self, p1_choice, p2_choice):
        if p1_choice == p2_choice:
            return 'tie'
        elif (p1_choice == 'rock' and p2_choice == 'scissors') or \
             (p1_choice == 'paper' and p2_choice == 'rock') or \
             (p1_choice == 'scissors' and p2_choice == 'paper'):
            return 'p1'
        else:
            return 'p2'

    def play_round(self, player_count):
        if player_count == 0:
            p1_choice = self.get_computer_choice()
            p2_choice = self.get_computer_choice()
        elif player_count == 1:
            p1_choice = self.get_human_choice(1)
            p2_choice = self.get_computer_choice()
        elif player_count == 2:
            p1_choice = self.get_human_choice(1)
            p2_choice = self.get_human_choice(2)
        else:
            raise ValueError("Invalid number of players.")

        print(f'Player 1 chose: {p1_choice}')
        print(f'Player 2 chose: {p2_choice}')

        winner = self.determine_winner(p1_choice, p2_choice)
        if winner == 'tie':
            print("It's a tie!")
            self.results['ties'] += 1
        elif winner == 'p1':
            print("Player 1 wins!")
            self.results['wins'] += 1
        else:
            print("Player 2 wins!")
            self.results['losses'] += 1

    def play_multiple_rounds(self, player_count, rounds):
        for _ in range(rounds):
            self.play_round(player_count)
            print(f"Current results: {self.results}")

    def get_results(self):
        return self.results

if __name__ == "__main__":
    game = RockPaperScissors()
    
    while True:
        player_count = int(input("Enter number of human players (0, 1, or 2): "))
        rounds = int(input("Enter number of rounds to play: "))
        game.play_multiple_rounds(player_count, rounds)
        
        print(f"Final results: {game.get_results()}")
        
        if input("Do you want to play again? (yes/no): ").lower() != 'yes':
            break
