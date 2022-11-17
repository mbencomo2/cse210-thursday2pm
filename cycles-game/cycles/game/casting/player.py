import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Player(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, player: int = 1):
        super().__init__()
        self._segments = []
        self._player = player
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            color = constants.RED if self._player == 1 else constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        if self._player == 1:
            position = .25
            color = constants.RED
        elif self._player == 2:
            position = .75
            color = constants.GREEN

        x = int(constants.MAX_X * position)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.CYCLES_LENGTH):
            position = Point(x, y + i * constants.CELL_SIZE)
            velocity = Point(0, 0)
            text = "@" if i == 0 else "#"

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    def get_player(self):
        return self._player