import Regular_Enemy
import random
import pyxel
import time

# Most of the methods are the same from regular enemy
class Big_Enemmy(Regular_Enemy.Regular_Enemy):

    def update(self):
        #Here we get the delta time for when it starts to turns
        time_this_frame = time.time()
        self.dt = time_this_frame - self.time_last_frame
        #We check that it is not turning and that it has not turned before
        if self.turn == False and self.turned == False:
            if self.position_y > 126:
                #We just create a little probability so the planes doesn´t turn all at the same time.
                if random.randint(0,3) == 3:
                    self.turn = True
                    self.initial_y = self.position_y
                    self.time_last_frame = time.time()
                    self.dt = time_this_frame - self.time_last_frame
    #we call the function turning each time it is turning
        if self.turn == True:

            radious = 2
            self.turning(radious,self.direction,self.dt,self.initial_y)
    #If it is not turning it will just move down normally
        elif self.turned == False:
            self.position_y += self.velocity
    #If it has turned the direction will change to up.
        else:
            self.position_y -= self.velocity

        #Just Shooting at random intervals
        if random.randint(0,50) == 3:
            self.shooting()
            self.shooting()
            self.shooting()
        self.Bull_Manager.update()
