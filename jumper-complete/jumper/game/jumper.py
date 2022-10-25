import random
from game.word import Word

class Jumper:
    """The person jumping with a parachute. 
    
    The responsibility of Jumper is to keep track of its parachute and safety status. 
    
    Attributes:
        _location (int): The location of the Jumper (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._parachute = ['  ___ ', ' /___\ ', ' \   / ', '  \ /', '   O']
        self._is_fallen = False
    
    def get_Parachute(self) -> str:
        """Gets the current parachute

        Args:
            self (Jumper): An instance of Jumper.
            draw_jumper (bool): If you want to avoid drawing the jumper's torso
        
        Returns:
            string: the current parachute
        """
        #create a string that contains our jumper's parachute
        parachute = '\n'.join(self._parachute)
        # Draw the jumper's torso unless specified
        parachute += '\n  /|\ \n  / \ \n\n^^^^^^^'
        return parachute

    def set_parachute(self,):
        """Removes a piece of the parachute if the guess was incorrect

        Args:
            self (Jumper): An instance of Jumper.
            
        Returns:
            nothing
        """
        # Remove the first element from the parachute list
        self._parachute.pop(0)
        
        # If we are at the jumper's head (last element), cut the line
        if len(self._parachute) <= 1:
            self.cut_line()

        
    def cut_line(self):
        """The jumper has lost his parachute and died.

        Args:
            self (Jumper): An instance of Jumper.
        """
        # Report that the jumper has died
        self._is_fallen = True
        # append the jumpers head after removing it
        self._parachute = []
        self._parachute.append('   x')

    def get_safety(self) -> bool:
        """Report the jumper's state of wellbeing.
        
        Args:
            self (Jumper): An instance of Jumper.
        """
        return self._is_fallen

    def land_safely(self) -> str:
        """The player guessed the word correctly and the jumper landed safely!
        
        Args:
            self (Jumper): An instance of Jumper
        """
        # Build the jumper using the current parachute and congratulate the player
        jumper = f'\n{self.get_Parachute()}\nCongrats! you landed safely!'
        return jumper