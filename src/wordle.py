from PyDictionary import PyDictionary
from rich import print
from rich.console import Console
from options import Options
dictionary = PyDictionary()
console = Console(width=65)

# Create an Options instance
settings = Options()


class GameSession():  # Manages the game state and logic
    def __init__(self, wordle_word):
        self.wordle_word = wordle_word
        # Initialize an empty list to store guessed words
        self.guessed_words = []
        self.attempts_left = 6  # Max number of attempts

    # make a guess
    def make_guess(self, word_guess):
        # Clear the console or terminal screen
        import os
        os.system('clear' if os.name == 'posix' else 'cls')

        # add player guess to guessed_word list
        self.guessed_words.append(word_guess)

        if word_guess == self.wordle_word:
            return """
       __   __  _______  __   __    _     _  _______  __    _  __
      |  | |  ||       ||  | |  |  | | _ | ||       ||  |  | ||  |
      |  |_|  ||   _   ||  | |  |  | || || ||   _   ||   |_| ||  |
      |       ||  | |  ||  |_|  |  |       ||  | |  ||       ||  |
      |_     _||  |_|  ||       |  |       ||  |_|  ||  _    ||__|
        |   |  |       ||       |  |   _   ||       || | |   | __
        |___|  |_______||_______|  |__| |__||_______||_|  |__||__|
      """
        elif self.attempts_left == 1:
            self.attempts_left -= 1
            return '''
 __   __  __    _  ___      __   __  _______  ___   _  __   __      ___    ____
|  | |  ||  |  | ||   |    |  | |  ||       ||   | | ||  | |  |    |   |  |    |
|  | |  ||   |_| ||   |    |  | |  ||       ||   |_| ||  |_|  |    |___| |    _|
|  |_|  ||       ||   |    |  |_|  ||       ||      _||       |     ___  |   |
|       ||  _    ||   |___ |       ||      _||     |_ |_     _|    |   | |   |
|       || | |   ||       ||       ||     |_ |    _  |  |   |      |___| |   |_
|_______||_|  |__||_______||_______||_______||___| |_|  |___|             |____|
      '''
        else:
            self.attempts_left -= 1
            return '[center]Incorrect guess. Try again.\n\n[/center]'

    def is_game_over(self):
        # if attempts left reaches 0
        if self.attempts_left <= 0:
            return True
        # if player guesses correctly
        if self.wordle_word in self.guessed_words:
            return True
        return False

    def is_game_won(self):
        return self.wordle_word in self.guessed_words


class GameRound:  # Handles game state presentation and interaction.
    def __init__(self, wordle_word, game_session, settings):
        self.wordle_word = wordle_word
        # Store a reference to the GameSession instance
        self.game_session = game_session
        self.settings = settings

    def display_game_state(self, game):
        if game.guessed_words:
            for i, guess in enumerate(game.guessed_words, start=1):
                formatted_guess_text = []

                for wordle_char, guessed_char in zip(game.wordle_word, guess):
                    if guessed_char == wordle_char:
                        formatted_guess_text.append(
                            f"[bold green]{guessed_char}[/]")
                    elif guessed_char in game.wordle_word:
                        formatted_guess_text.append(
                            f"[bold orange3]{guessed_char}[/]")
                    else:
                        formatted_guess_text.append(
                            f"[bold grey62]{guessed_char}[/]")
                # Join the colored characters with spaces
                formatted_guess_text = " ".join(formatted_guess_text)
                # Print the styled text with center alignment
                console.print(formatted_guess_text, justify="center")
            print(game.guessed_words)
            print("GAME.GUESSED_WORDS above")
            #display keyboard
            self.display_keyboard(game)

            # display attempts left
            print(f"\n\nGuesses left: {game.attempts_left}\n\n")

    def get_player_guess(self):
        player_guess = input(str('\n\nEnter word: ')).upper()

        # check if the word is the correct length
        if len(player_guess) != self.settings.word_length:
            print(f'Please enter a {self.settings.word_length}-letter word!')
            return self.get_player_guess()

        # check if word is in the dictionary
        is_in_dictionary = bool(dictionary.meaning(player_guess))
        if not is_in_dictionary:
            print(f'Could not find the word {player_guess} '
            'in the dictionary. Try again.')
            return self.get_player_guess()
        else:
            return player_guess

    def display_guesses(self, guessed_words):
        for i, guess in enumerate(guessed_words, start=1):
            formatted_guess_text = []

            for wordle_char, guessed_char in zip(self.wordle_word, guess):
                if guessed_char == wordle_char:
                    formatted_guess_text.append(
                        f"[bold green]{guessed_char}[/]")
                elif guessed_char in self.wordle_word:
                    formatted_guess_text.append(
                        f"[bold orange3]{guessed_char}[/]")
                else:
                    formatted_guess_text.append(
                        f"[bold grey62]{guessed_char}[/]")

            # Join the colored characters with spaces
            formatted_guess_text = " ".join(formatted_guess_text)

            # Print the styled text with center alignment
            console.print(formatted_guess_text, justify="center")

    def display_keyboard(self, game):
        # Define the keyboard layout as a list of rows
        keyboard_layout = [
            'Q W E R T Y U I O P',
            ' A S D F G H J K L ',
            '   Z X C V B N M   '
        ]

        # Create a set of used letters from all guessed words
        used_letters = set()
        for guessed_word in game.guessed_words:
            used_letters.update(guessed_word)

        # Loop through each row and print it with the appropriate color
        for row in keyboard_layout:
            for letter in row:
                if letter.strip() in used_letters:
                    # If the letter is used in any guessed word, print it in "red3"
                    print(f'[dim]{letter}[/dim]', end="  ")
                else:
                    # If the letter is not used in any guessed word, print it in the default color
                    print(letter, end="  ")
            print()  # Move to the next line after printing a row

    def display_outcome(self, game):
        # Display all 6 guesses to the user
        self.display_guesses(game.guessed_words)

        # Determine if the game is won using the is_game_won
        is_win = self.game_session.is_game_won()

        # Check if it's a win or a loss
        if is_win:
            print('\n\nCongratulations! '
                f'You correctly guessed the word: [bold magenta]{
                    self.wordle_word}[/]!\n\n\n\n')
        else:
            print('\n\nOh no! You\'ve run out of guesses. '
                f'The word was [bold magenta]{
                    self.wordle_word}[/]!\n\n\n\n')
