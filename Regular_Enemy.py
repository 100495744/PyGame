import math

import pyxel
import Bullets
import Creature
import Bullet_manager
import Colision_System
import random
import time


class Regular_Enemy(Creature.Creature):
    def __init__(self, height: int, width: int, x: int, y: int, sprite_image: int,
                 sprite_position_x: int, sprite_position_y: int, velocity: int, playerx=0, playery=0, health: int = 1):
        super().__init__(height, width, x, y, sprite_image, sprite_position_x, sprite_position_y, )

        self.velocity = velocity
        self.health = health
        self.Turn = False
        # parameters for time
        self.time_last_frame = time.time()
        self.dt = 0
        # parameters for firing at the player
        self.player_position_x = playerx
        self.player_position_y = playery
        self.Bull_Manager = Bullet_manager.Bullet_manager()
        # parameters for turning
        self.direction = random.randint(0, 1)
        self.turn = False
        self.turned = False
        self.initial_y = 0

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

    @property
    def player_position_x(self):
        return self.__player_position_x

    @player_position_x.setter
    def player_position_x(self, x):
        if type(x) != int:
            raise TypeError("The position needs to be an int")
        else:
            self.__player_position_x = x

    @property
    def player_position_y(self):
        return self.__player_position_y

    @player_position_y.setter
    def player_position_y(self, y):
        if type(y) != int:
            raise TypeError("The position y needs to be an int")
        else:
            self.__player_position_y = y

    def update(self):
        # Here we get the delta time for when it starts to turns
        time_this_frame = time.time()
        self.dt = time_this_frame - self.time_last_frame
        # We check that it is not turning and that it has not turned before
        if self.turn == False and self.turned == False:
            if self.position_y > 120:
                # We just create a little probability so the planes doesn´t turn all at the same time.
                if random.randint(0, 15) == 3:
                    self.turn = True
                    self.initial_y = self.position_y
                    self.time_last_frame = time.time()
                    self.dt = time_this_frame - self.time_last_frame
        # we call the function turning each time it is turning
        if self.turn == True:

            radious = 2
            self.turning(radious, self.direction, self.dt, self.initial_y)
        # If it is not turning it will just move down normally
        elif self.turned == False:
            self.position_y += self.velocity
        # If it has turned the direction will change to up.
        else:
            self.position_y -= self.velocity

        # Just Shooting at random intervals
        if random.randint(0, 80) == 3:
            self.shooting()
        self.Bull_Manager.update()

    def draw(self):
        super(Regular_Enemy, self).draw()
        self.Bull_Manager.draw()

    def turning(self, radious, direction, time, initial_y):
        # To the left: we use the physics formulas for MCU.
        if direction == 0:
            angle = math.pi
            angular_velocity = self.velocity / radious
            new_angle = angle + (angular_velocity * time * time / 2)
            # we change the position depending on the radious and the velocity
            self.position_x = self.position_x + int(radious + (self.velocity * math.cos(new_angle)))
            self.position_y = self.position_y + int(radious + (self.velocity * math.sin(new_angle)))
            # we finish turning when we reach certain angle
            if new_angle >= (1 + math.pi):
                self.turn = False
                self.turned = True
        # To the right,
        elif direction == 1:
            angle = math.pi
            angular_velocity = self.velocity / radious

            new_angle = angle + (angular_velocity * time * time / 2)
            # we change the position depending on the angular velocity and the radious
            self.position_x = self.position_x - int(radious + (self.velocity * math.cos(new_angle)))
            self.position_y = self.position_y + int(radious + (self.velocity * math.sin(new_angle)))
            # We finish turning when we reach certain angle
            if new_angle >= (1 + math.pi):
                self.turn = False
                self.turned = True

    # method for shooting
    def shooting(self):
        # We get the angle between the player and the enemy by using trigonometry and vectors.
        direction = int(math.degrees(((self.player_position_y * self.position_y) +
                                      (self.player_position_x * self.position_y))) / (math.sqrt((self.position_x ^ 2)
                                                                                                + (
                                                                                                            self.position_y ^ 2)) * math.sqrt(
            (self.player_position_y ^ 2) +
            (self.player_position_x ^ 2))))
        # we append the bullet to the bullet list of the bullet manager
        Bullet_ = Bullets.Bullet(4, 4, self.position_x, self.position_y + 1, 2, 74, 89, 5, direction)
        self.Bull_Manager.list_bullets_player.append(Bullet_)
