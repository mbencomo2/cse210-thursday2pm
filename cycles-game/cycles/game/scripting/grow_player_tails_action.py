from game.scripting.action import Action

class GrowPlayerTrailsAction(Action):
  '''
  Grows each player's trail when the game is live.
  '''
  def execute(self, cast, script):
    message = cast.get_first_actor("messages")
    if message.get_text() == "":
      for actor in cast.get_actors("players"):
        actor.grow_tail(1)
    return