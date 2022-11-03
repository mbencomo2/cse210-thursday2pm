# TODO Implement the gem class, inheriting the actor class
from random import randint
from game.casting.actor import Actor
from game.shared.point import Point

class Gem(Actor):
    '''
    An object falls from the crumbling cliff face above! It can either be a shining gem or a dangerous rock (wouldn't both hurt?). 
    Try and catch the gems and avoid the rocks!

    The purpose of a Object is to move down the screen, and cause the player's score to change when colliding. Also, reset it's position and 
    velocity when exiting the screen.

    Attributes:
      _points: The number of points the Gem is worth
    '''

    def __init__(self) -> None:
        '''
        Constructs the Object

        Arguments:
          self: A reference to the Object class
        '''
        self._points = 0
    
    def set_points(self, points: int) -> None:
      '''
      Set the _points attribute to the given value.

      Arguments:
        points (int): The points value of the object
      '''
      self._points = points

    def get_points(self) -> int:
      '''
      Gets the value of the _points attribute.

      Arguments:
        self (Object): reference to the Object class
      '''
      return self._points

    def reset(self, max_y: int) -> None:
      '''
      The objects home is the starting position, this function
      resets it to a different position and velocity when exiting the screen.

      Arguments:
        self (Object): A reference to the Object class
        max_x (int): The largest x value of the window
        max_y (int): The largest Y value of the window
        scale (int): The size of the cells used to scale the point
      '''
      #We need the object to appear at the top of the screen in a random column
      home = Point(randint(1, max_y), 0).scale(super().get_font_size())
      velocity = Point(0, randint(1, 2)).scale(super().get_font_size())
      super().set_position(home)
      super().set_velocity(velocity)
