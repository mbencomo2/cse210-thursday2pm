from game.casting.actor import Actor
from game.shared.point import Point
import constants


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
        _player (int): A number representing the player who owns the score
        _reset (bool): Keeps track of whether the player wants to reset the game
    """
    def __init__(self, player: int = 1) -> None:
        super().__init__()
        self._points = 0
        self._player = "One" if player == 1 else "Two"
        self._position = Point(0, 0).scale(constants.CELL_SIZE) if player == 1 else Point(constants.MAX_X - 10, 0).scale(constants.CELL_SIZE)
        self.add_points(0)

    def add_points(self, points: int = 1) -> None:
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Player {self._player}: {self._points}")