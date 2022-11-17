import constants
from game.casting.player import Player
from game.scripting.action import Action
from game.services.keyboard_service import KeyboardService

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the player collides
    with its segments, the other player's segements, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self) -> None:
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
        else:
            self._handle_game_over(cast)
    
    def _handle_segment_collision(self, cast) -> None:
        """Sets the game over flag if the player collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        players = cast.get_actors("players")
        scores = cast.get_actors("scores")
        heads = []
        segments = []
        for player in players:
            heads.append(player.get_segments()[0])
            for segment in player.get_segments()[1:]:
                segments.append(segment)
        
        for head in heads:
            for segment in segments:
                if head.get_position().equals(segment.get_position()):
                    self._is_game_over = True
                    if head.get_color() == constants.RED:
                        scores[1].add_points(1)
                    elif head.get_color() == constants.GREEN:
                        scores[0].add_points(1)

        
    def _handle_game_over(self, cast) -> None:
        """Shows the 'game over' message and turns the player and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            players = cast.get_actors("players")
            segments = []
            for player in players:
                for segment in player.get_segments():
                    segments.append(segment)

            message = cast.get_first_actor("messages")
            message.set_text("Game Over!")

            reset_message = cast.get_actors('messages')
            reset_message[-1].set_text('Play Again?\n    Y/N')

            for segment in segments:
                segment.set_color(constants.WHITE)

    def get_is_game_over(self) -> bool:
        '''
        Returns the game over state when checking to reset the game.
        
        Args:
            self (Action): An instance of HandleCollisionsAction
        '''
        return self._is_game_over

    def set_is_game_over(self, state: bool = False) -> None:
        '''
        Sets the game over state when resetting the game

        Args:
            self (Action): An instance of HandleCollisionsAction
        '''
        self._is_game_over = state
