import math
import Creature
import pyxel


# the bullet class gets atributes from the creature class.
class Bullet(Creature.Creature):
    def __init__(self, height: int, width: int, x: int, y: int, sprite_image: int,
                 sprite_position_x: int, sprite_position_y: int, velocity: int, direction=int):
        super().__init__(height, width, x, y, sprite_image, sprite_position_x, sprite_position_y)

        self.velocity = velocity
        self.direction = direction

    @property
    def velocity(self):
        return self.__velocity

    # Velocity just needs to be an int.
    @velocity.setter
    def velocity(self, velocity):
        if type(velocity) != int:
            raise TypeError("The velocity needs to be a int.")
        else:
            self.__velocity = velocity

    @property
    def direction(self):
        return self.__direction

    # In the setter of the direction we make sure the input is an angle
    @direction.setter
    def direction(self, d):
        if type(d) != int:
            raise TypeError("Direction needs to be an int")
        else:
            self.__direction = d

    # in the update we will change the position using trigonometry, and the direction given in angles, so the
    # bullets can move in diagonal.
    def update(self):
        self.position_x = self.position_x + int(self.velocity * math.cos(math.radians(self.direction)))
        self.position_y = self.position_y - int(self.velocity * math.sin(math.radians(self.direction)))

    def draw(self):
        super(Bullet, self).draw()
