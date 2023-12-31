# IMPORTS
import os
import sys
from rich import print
from rich.console import Console
import wordle
from options import Options

console = Console(width=65)
settings = Options() # Create an Options instance

# Display a welcome message and gather the player's name.
def display_introduction(name) -> None:
    clear_screen()

    console.print(f'Great! 👋 Hi, {name}!\n\n')
    console.print(
        '🧩 Wordle is a word-guessing game.'
        'Try to guess a secret [bold cyan]five-letter word[/]'
        ' in [bold magenta]six attempts[/].\n')
    console.print(
        'After each guess, I\'ll provide feedback using color indicators:')
    console.print(
        '1. [bold green]Green[/] '
        'means the letter is correct and in the right position.')
    console.print(
        '2. [bold orange3]Orange[/] '
        'means the letter is correct but in the wrong position.')
    console.print(
        '3. [bold grey62]Grey[/] means the letter is not in the word.')
    console.print(
        'Your goal is to guess the word as quickly as possible.\n\n\n')

def display_welcome():
    clear_screen()

    # Welcome banner
    print('''
 _     _  _______  ___      _______  _______  __   __  _______    _______  _______    _     _  _______  ______    ______   ___      _______  __  
| | _ | ||       ||   |    |       ||       ||  |_|  ||       |  |       ||       |  | | _ | ||       ||    _ |  |      | |   |    |       ||  | 
| || || ||    ___||   |    |       ||   _   ||       ||    ___|  |_     _||   _   |  | || || ||   _   ||   | ||  |  _    ||   |    |    ___||  | 
|       ||   |___ |   |    |       ||  | |  ||       ||   |___     |   |  |  | |  |  |       ||  | |  ||   |_||_ | | |   ||   |    |   |___ |  | 
|       ||    ___||   |___ |      _||  |_|  ||       ||    ___|    |   |  |  |_|  |  |       ||  |_|  ||    __  || |_|   ||   |___ |    ___||__| 
|   _   ||   |___ |       ||     |_ |       || ||_|| ||   |___     |   |  |       |  |   _   ||       ||   |  | ||       ||       ||   |___  __  
|__| |__||_______||_______||_______||_______||_|   |_||_______|    |___|  |_______|  |__| |__||_______||___|  |_||______| |_______||_______||__| 
  ''')

    print('\n\n👋 Hello there! I\'m your Wordle companion. '
        'Before we dive into the word-guessing fun, may I know your name? '
        'Please type it below, and we\'ll get started: ')
    name = input(str('\n\n\nEnter your name:  '))

    display_introduction(name)

def start_game(settings):
    # Generate wordle_word based on word_length setting
    wordle_word = settings.generate_wordle_word()
    print(f'Wordle_word: {wordle_word}')
    # Create an instance of the GameSession with the word set to wordle_word variable
    game = wordle.GameSession(wordle_word)
    game_round = wordle.GameRound(wordle_word, game, settings)

    # === GAME ====
    print(f'Please type a {
        settings.word_length}-letter word to make your first guess.')

    # This while loop will run as long as game is not over
    while not game.is_game_over():
        # Displays progression of the game
        game_round.display_game_state(game)
        # User inputs a guess
        player_guess = game_round.get_player_guess()
        # Give feedback to the user about their guess
        feedback = game.make_guess(player_guess)
        print(feedback)

    game_round.display_outcome(game)

# Display post-game options menu for starting a new game, adjusting settings, or exiting.
def end_game_options(settings):
    while True:
        print('[bold cyan]GG! 🤝[/bold cyan]\n')
        print('1. [bold magenta]s[/] - Start a new game')
        print('2. [bold magenta]o[/] - Go to options menu')
        print('3. [bold magenta]x[/] - Exit the game')

        end_game_choice = input('\nType a command: ')

        # Execute the chosen action based on user input.
        if end_game_choice.lower() == 's':
            os.system('clear' if os.name == 'posix' else 'cls')
            print('Starting a new game...\n')
            start_game(settings)
        elif end_game_choice.lower() == 'o':
            os.system('clear' if os.name == 'posix' else 'cls')
            settings.display_options()
            start_game(settings)
        elif end_game_choice.lower() == 'x':
            clear_screen()
            print('Thanks for playing Wordle 🫶. Goodbye!\n')
            sys.exit()
        else:
            clear_screen()
            print('[bold red]Invalid command.[/bold red] '
                'Please choose a valid option (s, o, or x).\n')

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# MAIN
def main():
    while True:
        # Prompt the player for the game options
        print(
            'Type [bold][S]tart[/] to begin or [bold][O]ptions[/] to adjust game settings: ')
        choice = input()

        if choice == 'O' or choice == 'o':
            # Use the Options class to adjust word length
            settings.display_options()
            start_game(settings)
            break  # This break will exit the main loop

        # If the player hasn't adjusted the settings, allow them to start the game
        elif choice == 'S' or choice == 's':
            start_game(settings)
            break  # This break will exit the main loop

        else:
            print(
                'Invalid choice. Please type [bold]start[/] or [bold]options[/].')

    end_game_options(settings)


if __name__ == '__main__':
    # Display the welcome message and initiate the main game loop.
    display_welcome()
    main()
