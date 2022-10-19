from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.word import Word


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        jumper (Jumper): The game's skydiver.
        is_playing (boolean): Whether or not to keep playing.
        word (Word): The game's secret word.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._word = Word()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._do_outputs()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

        if not self._jumper.get_safety():
            self._terminal_service.write_text(self._jumper.land_safely()) #land_safely prints a congratulatory message
        else:
            self._terminal_service.write_text(f'R.I.P. - The secret word was: "{self._word.get_word()}"')

    def _get_inputs(self):
        """obtains inputs from the player

        Args:
            self (Director): An instance of Director.
        """
        if not self._is_playing:
            return

        self._guess = self._terminal_service.read_text("\nGuess a letter[a-z]: ")
        
    def _do_updates(self):
        """Updates the jumper's parachute and checks if we have guessed the secret word

        Args:
            self (Director): An instance of Director.
        """

        if not self._is_playing:
            return

        # Check if our guess is in the secret word, otherwise we remove a part of the parachute
        if self._guess in self._word.get_word():
            self._word.set_guess(self._guess)
        else: 
            self._jumper._cut_line()

        # Check if our guesses up to this point match the secret word, otherwise check the safety of the jumper
        if self._word.get_guess() == self._word.get_word():
            self._is_playing = False
        elif self._jumper._get_safety(): #get_safety returns whether the parachute has broken or not
            self._is_playing = False
        
    def _do_outputs(self):
        """Creates the display and passes it to the terminal service

        Args:
            self (Director): An instance of Director.
        """
        #get_guess returns our guesses as a string, get_parachute returns our jumper with parachute as a string
        display = f'\n{self._word.get_guess()}\n\n{self._jumper._get_Parachute()}' 
        self._terminal_service.write_text(display)
