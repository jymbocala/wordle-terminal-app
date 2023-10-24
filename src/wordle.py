from PyDictionary import PyDictionary
dictionary = PyDictionary()


class GameSession():
  def __init__(self, wordle_word):
    self.wordle_word = wordle_word
    self.guessed_words = []  # Initialize an empty list to store guessed words.
    self.attempts_left = 6 # Max number of attempts

  # make a guess
  def make_guess(self, word_guess):
    print('The user has guessed the word ' + word_guess)

    if word_guess == self.wordle_word:
      print(f'You guessed the correct word: {self.wordle_word}')
    else:
      self.attempts_left -= 1
      return "Incorrect guess. Try again."


  def is_game_over(self):
    False


class GameRound():
  # def __init__(self, wordle):
  #   self.wordle = wordle

  def display_game_state():
    # display how many attempts the player has made
    # display previous player guesses
    pass

  def get_player_guess(self):
    player_guess = input(str('Guess 1/6: '))

    # check if word is 5 characters long
    if len(player_guess) != 5:
      print('Please enter a five-letter word!')
      return self.get_player_word()

    # check if word is in the dictionary
    is_in_dictionary = bool(dictionary.meaning(player_guess))
    if not is_in_dictionary:
      print(f'Could not find the word "{
            player_guess}" in the dictionary. Try again.')
      return self.get_player_guess()
    else:
      print(f'"{player_guess}" is in the dictionary!')

    return player_guess
