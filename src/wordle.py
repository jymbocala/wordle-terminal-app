from PyDictionary import PyDictionary
dictionary = PyDictionary()


class GameSession():
  def __init__(self, wordle_word):
    self.wordle_word = wordle_word

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
      print(f'Could not find the word "{player_guess}" in the dictionary. Try again.')
      return self.get_player_guess()
    else:
      print(f'"{player_guess}" is in the dictionary!')

    return player_guess



  # make a guess
  def make_guess(word_guess):
    print('The user has guessed the word ' + word_guess)
  # loop over guess word characters and check if it matches wordle_word characters
