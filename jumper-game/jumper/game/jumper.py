class Jumper:
    """The Person jumping with the skydieve.

    The responsibility of the 
    jumper is to control the parachute 
    on the skydiver
    
    Attributes:
        _parachute (string): The parachute for the jumper
        _man (string): The man skydieving
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
            "  o"
        ]
        self._man = [
            " /|\\",
            " / \\",
            "^^^^^^^^"
        ]

    def _get_skydiever(self):
        """Gets the jumper"
        Args:
            self (Jumper): An instance of Jumper.
        """
        for line in self._parachute:
            print(line)
        for line in self._man:
            print(line)

    def _set_skydiever(self):
        """Draws the jumper"
        Args:
            self (Jumper): An instance of Jumper.
        """
        self.jumper = self._get_skydiever()

    def _cut_line(self):
        pass

    def _is_fallen(self):
        pass
    


# Test the drawings
jump = Jumper()
jump._set_skydiever()