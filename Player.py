import Creature
import pyxel
import Bullets
import Bullet_manager
import time


class Player(Creature.Creature):
    def __init__(self, height: int, width: int, x: int, y: int, sprite_image: int,
                 sprite_position_x: int, sprite_position_y: int, velocity: int, health: int = 3):
        super().__init__(height, width, x, y, sprite_image, sprite_position_x, sprite_position_y)

        self.health = health
        self.velocity = velocity
        # we create a bull manager
        self.Bull_manager = Bullet_manager.Bullet_manager()
        self.time_last_frame = time.time()
        # parameters for time
        self.dt = 0
        self.last_time_shoot = 0
        # parameters for turning mecaninc
        self.last_time_turn = 0
        self.turns = 3
        self.turning = False
        self.hurt = False

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        if type(velocity) != int:
            raise TypeError("The velocity needs to be a int.")
        else:
            self.__velocity = velocity

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, h):
        if type(h) != int:
            raise TypeError("Health needs to be an int")
        else:
            self.__health = h

    def update(self):
        # all time calculations for the shooting time and the turning
        time_this_frame = time.time()
        self.dt = time_this_frame - self.time_last_frame
        self.time_last_frame = time_this_frame
        self.last_time_shoot += self.dt
        self.last_time_turn += self.dt
        self.Bull_manager.update()
        self.sprite_position_x = 4

        # movement of the player
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.position_x + 16 > 223:
                ""
            else:
                self.position_x += self.velocity
                # we change the position of the sprite so we give an animation
                self.sprite_position_x = 100

        elif pyxel.btn(pyxel.KEY_LEFT):
            if self.position_x < 1:
                ""
            else:
                self.position_x -= self.velocity
                # we change the position of the sprite so we give an animation
                self.sprite_position_x = 133
        if pyxel.btn(pyxel.KEY_UP):
            if self.position_y < 1:
                ""
            else:
                self.position_y -= self.velocity
        elif pyxel.btn(pyxel.KEY_DOWN):
            if self.position_y + 16 > 255:
                ""
            else:
                self.position_y += self.velocity

        # This checks if we are pressing the space key and that it has passed enough time since the last shot
        if pyxel.btn(pyxel.KEY_SPACE) and self.last_time_shoot >= 0.5:
            # we reset the timer of the shoot
            self.last_time_shoot = 0
            self.fire()
        # turning check
        if pyxel.btn(pyxel.KEY_X) and self.last_time_turn >= 1 and self.turns > 0:
            self.last_time_turn = 0
            self.turn()

        # we check if it is turning
        if self.turning == True:
            self.turn()

    # when we fire we create a bullet an append it to the list in the bull manager
    def fire(self):
        bullet_ = Bullets.Bullet(16, 16, self.position_x, self.position_y - 17, 0, 32, 0, 6, 90)
        self.Bull_manager.list_bullets_player.append(bullet_)

    # draw method plus we draw the bullets from the bull manager
    def draw(self):
        super(Player, self).draw()
        self.Bull_manager.draw()

    # function for the turning plane.
    def turn(self):
        self.turning = True
        # the turn last 2 secods, after that we reset the turn function
        if self.last_time_turn > 2:
            self.last_time_turn = 0
            self.turning = False
            self.turns -= 1
            self.sprite_position_x = 4
            self.sprite_position_y = 5
        # while turning we cannot be touched (See colision system) and we change our sprite
        else:
            self.turning = True
            self.sprite_position_x = 67
            self.sprite_position_y = 26
