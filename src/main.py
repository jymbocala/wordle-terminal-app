# IMPORTS
import os
from wonderwords import RandomWord
import wordle
from rich import print
from rich.console import Console

console = Console(width=65)

# function to display the game introduction
def display_introduction(name):
  console.print(f'Great! 👋Hi, {name}!\n\n')
  console.print("🧩 Wordle is a word-guessing game. Try to guess a secret [bold cyan]five-letter word[/] in [bold magenta]six attempts[/].")
  console.print("After each guess, I'll provide feedback using color indicators:")
  console.print("1. [bold green]Green[/] means the letter is correct and in the right position.")
  console.print("2. [bold orange3]Orange[/] means the letter is correct but in the wrong position.")
  console.print("3. [bold grey62]Grey[/] means the letter is not in the word.")
  console.print("Your goal is to guess the word as quickly as possible.\n\n\n")


# function to display the options menu
def options_menu():
  # clear the terminal diplay the options menu neater
  os.system('clear' if os.name == 'posix' else 'cls')

  while True:
    # Display available commands and ask for player input
    print("Available commands:")
    print("1. Adjust word length (e.g., 'length5')")
    print("2. Exit options menu with adjusted settings (type 'exit' or 'x')")

    choice = input("Type a command to change the setting: ")

    if choice.startswith("length"):
      # Parse the length from the command and adjust the game settings
      try:
        length = int(choice[6:])
        if 3 <= length <= 7:
          # Adjust the game settings with the new word length
          # Example: wordle_word = RandomWord().word(word_min_length=length, word_max_length=length).upper()
          wordle_word = RandomWord().word(word_min_length=5, word_max_length=5).upper()
          print(f"Word length set to {length}.")
        else:
          print("Invalid word length. Please enter a number between 3 and 7.")
      except ValueError:
        print("Invalid command format. Use 'length' followed by a number (e.g., 'length5').")

    elif choice.lower() == "exit" or choice.lower() == "x":
      print("Exiting the options menu.")
      break  # Exit the options menu loop

    else:
      print("Invalid command. Please choose a valid command from the list.")

# MAIN
if __name__ == "__main__":
  os.system('clear' if os.name == 'posix' else 'cls')
  
  # welcome banner
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

  wordle_word = RandomWord().word(word_min_length=5, word_max_length=5).upper()

  display_introduction(name)
  
  while True:
  # Prompt the player for the game options
    print('Type [bold][S]tart[/] to begin or [bold][O]ptions[/] to adjust game settings: ')
    choice = input()

    if choice == 'O' or choice == 'o':
      if options_menu():
        break
    elif choice == 'S' or choice == 's':
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
      break # this break will exit the main loop
    else:
      print('Invalid choice. Please type [bold]start[/] or [bold]options[/].')


    # === END GAME OPTIONS ====






