import Regular_Enemy
import random
import pyxel


# The Chungus enemy gets most of the methods from the regular enemy
class Chungus_Enemy(Regular_Enemy.Regular_Enemy):

    def update(self):
        # We set a simple path fot the enemy to follow
        if self.position_x >= 110 and self.position_y >= 80:
            self.position_y -= self.velocity
        elif self.position_x >= 30 and self.position_y <= 80:
            self.position_x -= self.velocity
        else:
            self.position_y += self.velocity

        # it shoots at random intervals several bullets.
        if random.randint(0, 70) == 3:
            self.shooting()
            self.shooting()
            self.shooting()
            self.shooting()
            self.shooting()
        self.Bull_Manager.update()
