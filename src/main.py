# IMPORTS
import os
from wonderwords import RandomWord
import wordle
from rich import print
from rich.console import Console
console = Console(width=65)

# MAIN
if __name__ == "__main__":
  os.system('clear' if os.name == 'posix' else 'cls')
  # Introduction
  print('''
 _     _  _______  ___      _______  _______  __   __  _______    _______  _______    _     _  _______  ______    ______   ___      _______  __  
| | _ | ||       ||   |    |       ||       ||  |_|  ||       |  |       ||       |  | | _ | ||       ||    _ |  |      | |   |    |       ||  | 
| || || ||    ___||   |    |       ||   _   ||       ||    ___|  |_     _||   _   |  | || || ||   _   ||   | ||  |  _    ||   |    |    ___||  | 
|       ||   |___ |   |    |       ||  | |  ||       ||   |___     |   |  |  | |  |  |       ||  | |  ||   |_||_ | | |   ||   |    |   |___ |  | 
|       ||    ___||   |___ |      _||  |_|  ||       ||    ___|    |   |  |  |_|  |  |       ||  |_|  ||    __  || |_|   ||   |___ |    ___||__| 
|   _   ||   |___ |       ||     |_ |       || ||_|| ||   |___     |   |  |       |  |   _   ||       ||   |  | ||       ||       ||   |___  __  
|__| |__||_______||_______||_______||_______||_|   |_||_______|    |___|  |_______|  |__| |__||_______||___|  |_||______| |_______||_______||__| 
  ''')
  print('\n\n👋 Hello there! I\'m your Wordle companion. Before we dive into the word-guessing fun, may I know your name? Please type it below, and we\'ll get started:')
  name = input(str('\n\n\nEnter your name:  '))

  os.system('clear' if os.name == 'posix' else 'cls')

  console.print(f'Great! 👋Hi, {name}!')
  console.print("🧩 Wordle is a word-guessing game. Try to guess a secret [bold cyan]five-letter word[/] in [bold magenta]six attempts[/].")
  console.print("After each guess, I'll provide feedback using color indicators:")
  console.print("1. [bold green]Green[/] means the letter is correct and in the right position.")
  console.print("2. [bold orange3]Orange[/] means the letter is correct but in the wrong position.")
  console.print("3. [bold grey62]Grey[/] means the letter is not in the word.")
  console.print("Your goal is to guess the word as quickly as possible.\n\n\n")


  # Initiate a new random 5-letter word
  wordle_word = RandomWord().word(word_min_length=5, word_max_length=5).upper()
  print(f'Wordle_word: {wordle_word}')
  # Create an instance of the GameSession with the word set to wordle_word variable
  game = wordle.GameSession(wordle_word)
  game_round = wordle.GameRound(wordle_word, game)

  # === GAME SEQUENCE ====
  print('Please type a five-letter word to make your first guess.')

  # this while loop will run as long as game is not over
  while not game.is_game_over():
    game_round.display_game_state(game) # displays progression of the game
    # user inputs a guess
    player_guess = game_round.get_player_guess()
    # give feedback to the user about their guess
    feedback = game.make_guess(player_guess)
    print(feedback)

  game_round.display_outcome(game)

  



  # make display method work




# CODE FOR ADDING HELP EXPLAINATION AT THE START
  # ask_if_player_is_ready()

  # def user_help():
  #   # print some helpful information about how the game works
  #   pass

  # def ask_if_player_is_ready():
  #   q = input(
  #     str('Type \'YES\' to begin or \'HELP\' if you\'d like more instructions: '))
  #   if q == 'YES' or q == 'yes':
  #     print('Starting new game...')

  #   elif q == 'HELP' or q == 'help':
  #     user_help()
  #   else:
  #     print('Oops! Please enter "YES" or "HELP".')
  #     ask_if_player_is_ready()