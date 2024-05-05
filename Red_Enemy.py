import math

import pyxel
import Bullets
import Creature
import Bullet_manager
import Colision_System
import random
import time
import Regular_Enemy


class Red_Enemy(Regular_Enemy.Regular_Enemy):
    def __init__(self, height: int, width: int, x: int, y: int, sprite_image: int,
                 sprite_position_x: int, sprite_position_y: int, velocity: int, spawn_left=True, playerx=0, playery=0,
                 health: int = 1):
        super().__init__(height, width, x, y, sprite_image, sprite_position_x, sprite_position_y, velocity, playerx,
                         playery, health)

        self.spawn_Left = spawn_left

    # As the red enemy is similar to the regular enemy, it will inherit most of its functions.
    # We will do just some minor changes to them

    # function for turning is changed so it gives more than one turn
    def turning(self, radious, direction, time, initial_y):
        # To the left: we use the physics formulas for MCU.
        if direction == 0:
            angle = math.pi
            angular_velocity = self.velocity / radious
            new_angle = angle + (angular_velocity * time * time / 2)
            self.position_x = self.position_x + int(radious + (self.velocity * math.cos(new_angle)))
            self.position_y = self.position_y + int(radious + (self.velocity * math.sin(new_angle)))
            # it stablish the number of turns it makes
            if new_angle >= (6 + math.pi):
                self.turn = False
                self.turned = True


        # if we come from the right then the starting angle for the turn is changed
        elif direction == 1:
            angle = math.pi
            angular_velocity = self.velocity / radious

            new_angle = angle + (angular_velocity * time * time / 2)
            self.position_x = self.position_x - int(radious + (self.velocity * math.cos(new_angle)))
            self.position_y = self.position_y + int(radious + (self.velocity * math.sin(new_angle)))

            if new_angle >= (6 + math.pi):
                self.turn = False
                self.turned = True

    def update(self):
        # Here we get the delta time for when it starts to turns
        time_this_frame = time.time()
        self.dt = time_this_frame - self.time_last_frame
        # We check that it is not turning and that it has not turned before
        if self.turn == False and self.turned == False:
            if self.spawn_Left == True:
                if self.position_x > 126:
                    # We just create a little probability so the planes doesn´t turn all at the same time.
                    if random.randint(0, 10) == 3:
                        self.turn = True
                        self.initial_y = self.position_y
                        self.time_last_frame = time.time()
                        self.dt = time_this_frame - self.time_last_frame
            # same as before but for coming from the right
            if self.spawn_Left == False:
                if self.position_x < 160:

                    if random.randint(0, 10) == 3:
                        self.turn = True
                        self.initial_y = self.position_y
                        self.time_last_frame = time.time()
                        self.dt = time_this_frame - self.time_last_frame
        # we call the function turning each time it is turning
        if self.turn == True:

            radious = 1
            self.turning(radious, self.direction, self.dt, self.initial_y)
        # If it is not turning it will just move down normally
        elif self.turned == False:
            self.position_x += self.velocity
        # If it has turned the direction will change to up.
        else:
            self.position_x -= self.velocity

        # Just Shooting at random intervals
        if random.randint(0, 50) == 3:
            self.shooting()
            self.shooting()
        self.Bull_Manager.update()
