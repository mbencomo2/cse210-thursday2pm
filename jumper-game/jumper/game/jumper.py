class Jumper:
    """The Person jumping with the parachute.

    The responsibility of the 
    jumper is to control the parachute 
    on the skydiver
    
    Attributes:
        _parachute (string): The parachute for the jumper
        _man (string): The man skydiving
    """

    def __init__(self):
        """Constructs a new Jumper.
        
        Args:
            self(Jumper): An instance of Jumper
        """
        self._parachute = [
            " ___",
            "/___\\",
            "\   /",
            " \ /",
            "  o",
            " /|\\",
            " / \\",
            "^^^^^"
        ]

    def get_Parachute(self) -> str:
        """Gets the jumper
        Args:
            self (Jumper): An instance of Jumper.
        """
        return "\n".join(self._parachute)

    def cut_line(self):
        """Cuts the first line in the parachute.
        Args:
            self(Jumper): An instance of Jumper"""
        self._parachute.pop(0)

    def get_safety(self) -> bool:
        """Returns whether the parachute has broken or not
        Args:
            self(Jumper): An instance of Jumper
        """
        if len(self._parachute) <= 4:
            return True
        else:
            return False
    
    def land_safely(self) -> str:
        """land_safely prints a congratulatory message
        Args:
            self (Jumper): An instance of Jumper.
        """
        return "Congratulations! You have guessed the word"

    def switch_head(self):
        """switches the skydiver's head by an x
        Args:
            self (Jumper): An instance of Jumper.
        """
        self._parachute[0] ="  x"