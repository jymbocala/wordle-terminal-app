from wordle import GameSession

def test_game_session_initialization():
    wordle_word = "CODER"
    game_session = GameSession(wordle_word)

    # Check if wordle_word is correctly set
    assert game_session.wordle_word == "CODER"

    # Check if guessed_words is an empty list
    assert game_session.guessed_words == []

    # Check if attempts_left is set to the maximum value, which is 6
    assert game_session.attempts_left == 6



def test_game_session_is_game_over():
    wordle_word = "ACADEMY"
    game_session = GameSession(wordle_word)

    # Initially, the game should not be over
    assert not game_session.is_game_over()

    # Make incorrect guesses until attempts run out
    for _ in range(game_session.attempts_left):
        game_session.make_guess("ACADEMY")

    # Now, the game should be over due to running out of attempts
    assert game_session.is_game_over()
