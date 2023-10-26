from PyDictionary import PyDictionary
from rich import print
from rich.console import Console
dictionary = PyDictionary()
console = Console(width=65)


class GameSession():  # Manages the game state and logic
  def __init__(self, wordle_word):
    self.wordle_word = wordle_word
    self.guessed_words = []  # Initialize an empty list to store guessed words
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
      return 'That was your last attempt sorry :('
    else:
      self.attempts_left -= 1
      return "Incorrect guess. Try again."

  def is_game_over(self):
    # if attempts left reaches 0
    if self.attempts_left <= 0:
      print('Oh no! You have ran out of guesses :(')
      return True
    # if player guesses correctly
    if self.wordle_word in self.guessed_words:
      return True
    return False

  def is_game_won(self):
    return self.wordle_word in self.guessed_words


class GameRound:  # Handles displaying information and taking input from the user.
  def __init__(self, wordle_word, game_session):
    self.wordle_word = wordle_word
    self.guesses = []
    self.game_session = game_session  # Store a reference to the GameSession instance

  def display_game_state(self, game):
    if game.guessed_words:
      for i, guess in enumerate(game.guessed_words, start=1):
        formatted_guess_text = []

        for wordle_char, guessed_char in zip(game.wordle_word, guess):
          if guessed_char == wordle_char:
            formatted_guess_text.append(f"[bold green]{guessed_char}[/]")
          elif guessed_char in game.wordle_word:
            formatted_guess_text.append(f"[bold orange3]{guessed_char}[/]")
          else:
            formatted_guess_text.append(f"[bold grey62]{guessed_char}[/]")
        # Join the colored characters with spaces
        formatted_guess_text = " ".join(formatted_guess_text)
        # Print the styled text with center alignment
        console.print(formatted_guess_text, justify="center")
      print(f"Guesses left: {game.attempts_left}")  # display attempts left

      # TODO:
      # fix: padded characters are not showing up with correct styles, and they are print in different lines

  def get_player_guess(self):
    player_guess = input(str('Enter word: ')).upper()

    # check if word is 5 characters long
    if len(player_guess) != 5:
      print('Please enter a five-letter word!')
      return self.get_player_guess()

    # check if word is in the dictionary
    is_in_dictionary = bool(dictionary.meaning(player_guess))
    if not is_in_dictionary:
      print(f'Could not find the word "{
            player_guess}" in the dictionary. Try again.')
      return self.get_player_guess()
    else:
      return player_guess

  def display_guesses(self, guessed_words):
    for i, guess in enumerate(guessed_words, start=1):
      formatted_guess_text = []

      for wordle_char, guessed_char in zip(self.wordle_word, guess):
        if guessed_char == wordle_char:
          formatted_guess_text.append(f"[bold green]{guessed_char}[/]")
        elif guessed_char in self.wordle_word:
          formatted_guess_text.append(f"[bold orange3]{guessed_char}[/]")
        else:
          formatted_guess_text.append(f"[bold grey62]{guessed_char}[/]")

      # Join the colored characters with spaces
      formatted_guess_text = " ".join(formatted_guess_text)

      # Print the styled text with center alignment
      console.print(formatted_guess_text, justify="center")

  def display_outcome(self, game):
    # Display all 6 guesses to the user
    self.display_guesses(game.guessed_words)

    # Determine if the game is won using the is_game_won method from GameSession
    is_win = self.game_session.is_game_won()

    # Check if it's a win or a loss
    if is_win:
      print(f'\n\nCongratulations! You correctly guessed the word: {game.wordle_word}!\n\n')
    else:
      print("Oh no! You've run out of guesses. The word was:", self.wordle_word)
