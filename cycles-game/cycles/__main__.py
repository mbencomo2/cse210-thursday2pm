import constants

from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.player import Player
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.grow_player_tails_action import GrowPlayerTrailsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.handle_reset_action import HandleResetAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("players", Player(1))
    cast.add_actor("scores", Score(1))
    cast.add_actor("players", Player(2))
    cast.add_actor("scores", Score(2))

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    
    game_over = Actor()
    position = Point(x, y)
    game_over.set_position(position)
    cast.add_actor("messages", game_over)

    play_again = Actor()
    position = Point(x, y + 2 * constants.CELL_SIZE,)
    play_again.set_position(position)
    cast.add_actor('messages', play_again)
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("input", HandleResetAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", GrowPlayerTrailsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()