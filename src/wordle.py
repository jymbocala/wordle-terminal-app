from PyDictionary import PyDictionary
dictionary = PyDictionary()


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
    
    self.guessed_words.append(word_guess)
    print('Current guessed_words: ')
    print(self.guessed_words)

    if word_guess == self.wordle_word:
      return f'Congratulations! You have correctly guessed the word: {
          word_guess}'
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


class GameRound():  # Handles displaying information and taking input from the user.
  def display_game_state(self, game):
    # display previous guesses
    # if game.guessed_words:
    #   print('Previous guesses:')
    #   for word in game.guessed_words:
    #     print(word)

    if game.guessed_words:
      print('Previous guesses:')
      for i, guess in enumerate(game.guessed_words, start=1):
          formatted_guess = ""
          for wordle_char, guessed_char in zip(game.wordle_word, guess):
              if guessed_char == wordle_char:
                  formatted_guess += guessed_char.lower()
              else:
                  formatted_guess += guessed_char.upper()
          print(f"Guess {i}: {formatted_guess}")

    # display attempts left
    print(f"Guesses left: {game.attempts_left}")

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
