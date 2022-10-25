from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
  '''
  A mysterious object that the robot can interact with. Can either be a random object or the kitten.

  The purpose of the Artifact is to provide a message about itself.

  Actor (class): Inherits the Actor class

  Attributes:
    _message (str): A short description of the Artifact
  '''
  def __init__(self):
    '''
    Initialize the class.

    Args:
      self: Reference to the Artifact class
    '''
    self._message = 'Secret Message'
  
  def set_message(self, message):
    '''
    Sets the artifacts message to display in the banner.

    Args: 
      self: Reference to the Artifact class
      message: the Artifact's message
    '''
    self._message = message

  def get_message(self) -> str:
    '''
    Returns the Artififact's message.

    Args:
      self: Reference to the Artifact class
    Return:
      str: self._message
    '''
    return self._message