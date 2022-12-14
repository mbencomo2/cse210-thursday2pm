# TODO Implement the gem class, inheriting the actor class
from random import randint
from game.casting.actor import Actor
from game.shared.point import Point

class Gem(Actor):
    '''
    An object falls from the crumbling cliff face above! It can either be a shining gem or a dangerous rock (wouldn't both hurt?). 
    Try and catch the gems and avoid the rocks!

    The purpose of a gem is to move down the screen, and cause the player's score to change when colliding. Also, reset it's position and 
    velocity when exiting the screen.

    Attributes:
      _points: The number of points the Gem is worth
    '''

    def __init__(self) -> None:
        '''
        Constructs the Gem

        Arguments:
          self: A reference to the Gem class
        '''
        self._points = 0
    
    def set_points(self, points: int) -> None:
      '''
      Set the _points attribute to the given value.

      Arguments:
        points (int): The points value of the Gem
      '''
      self._points = points

    def get_points(self) -> int:
      '''
      Gets the value of the _points attribute.

      Arguments:
        self (Gem): reference to the Gem class
      '''
      return self._points

    def reset(self, max_x: int) -> None:
      '''
      The Gems home is the starting position, this function
      resets it to a different position and velocity when exiting the screen.

      Arguments:
        self (Gem): A reference to the Gem class
        max_x (int): The largest x value of the window
        max_y (int): The largest Y value of the window
        scale (int): The size of the cells used to scale the point
      '''
      # type = 1: Gem
      # type = 2: Rock
      type = randint(1,2)
      speed = randint(1,2)

      if type == 1:
        super().set_text('*')
        self._points = 1
      else:
        super().set_text('O')
        self._points = -1

      # If the speed is two then the points value is doubled.
      self._points *= 2 if speed == 2 else 1

        
      #We need the Gem to appear at the top of the screen in a random column
      home = Point(randint(1, max_x), 0).scale(super().get_font_size())
      velocity = Point(0, speed).scale(super().get_font_size())
      super().set_position(home)
      super().set_velocity(velocity)
