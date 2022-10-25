from random import choice

class Word():
    """The secret word being guessed
    
    The responsibility of a Word is to pick a random word from a list, and keep track of the current guesses.
    
    Attributes:
        location (int): The location of the Word (1-1000).
    """

    def __init__(self):
        """Constructs a new Word.

        Args:
            self (Word): An instance of Word.
        """
        self._word_list = ['absently', 'lukewarm', 'buffoon', 'tiptoeing', 'overexert']
        self._secret_word = choice(self._word_list)
        self._guess = []

        # Create our empty guesses that will be displayed to the user
        for i in range(len(self._secret_word)):
            self._guess.append('_')
       
    def get_word(self) -> str:
        """Gets the secret word (not so secret anymore).
        
        Args:
            self (Word): An instance of Word.
        """
        return self._secret_word
        
    def set_guess(self, letter: str):
        """Adds the latest guess to the list.

        Args:
            self (Word): An instance of Word.
            letter: a string that is the guess the player made
        """
        #Find how many times the letter appears in our secret word
        count = self._secret_word.count(letter)
        guess_index = 0
        last_index = len(self._secret_word)
        
        # Loop 'count' times, each time we increment the guess_index to ensure we 
        # find the next instance of the letter we are looking for
        for i in range(count):
            guess_index = self._secret_word.find(letter, guess_index, last_index)
            self._guess[guess_index] = letter
            guess_index += 1

    def get_guess(self) -> str:
        """Gets the guesses stored and returns

        Args:
            self (Word): an instance of Word.
        """
        current_guess = ''

        # Build a string of our current guesses
        for guess in self._guess:
            current_guess += f'{guess}'
        return current_guess