import os

from game.scripting.action import Action
from game.casting.player import Player


class HandleResetAction(Action):
  '''
  An input that controls restarting the game after a game over.
  '''
  
  def __init__(self, keyboardservice) -> None:
    self._keyboard_service = keyboardservice

  def execute(self, cast, script) -> None:
    '''
    Resets the game if the game is over the player confirms.
    '''
    scripts = script.get_actions('update')
    messages = cast.get_actors('messages')
    players = cast.get_actors('players')
    handleCollisions = scripts[1]

    if self._keyboard_service.is_key_down('y') and handleCollisions.get_is_game_over():
        for player in players:
            cast.remove_actor('players', player)
        
        for message in messages:
          message.set_text('')

        cast.add_actor('players', Player(1))
        cast.add_actor('players', Player(2))

        script.get_actions('input')[0].reset_velocities()
        
        handleCollisions.set_is_game_over(False)
    elif self._keyboard_service.is_key_down('n') and handleCollisions.get_is_game_over():
      os._exit(os.EX_OK)
    return