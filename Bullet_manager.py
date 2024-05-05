import pyxel
import Bullets


class Bullet_manager:
    def __init__(self):
        # We just use two lists
        self.list_bullets_player = []
        self.bullets_hitted = []

    def update(self):

        # Removing bullets hitted
        if len(self.bullets_hitted) > 0:
            # For cheking that a bullet is not repeated
            Same_value = []
            for i in range(0, len(self.bullets_hitted) - 1):
                for j in range(i, len(self.bullets_hitted) - 1):
                    if self.bullets_hitted[i] == self.bullets_hitted[j]:
                        Same_value.append(i)
            for k in Same_value:
                del (self.bullets_hitted[k])
            # We short the list so we don't have a length problem
            len_enemies_hit = len(self.bullets_hitted)
            self.bullets_hitted.sort()
            if len(self.bullets_hitted) > 0:
                # deleting from the end
                for i in range(len_enemies_hit - 1, -1, -1):

                    if len(self.list_bullets_player) > 0:
                        del (self.list_bullets_player[self.bullets_hitted[i]])
        # We check that the bullet is not outside the boundaries, if it is we remove it
        counter = len(self.list_bullets_player)
        removed = []
        for i in range(0, counter, 1):
            self.list_bullets_player[i].update()
            # the if that checks they are outside
            if (self.list_bullets_player[i].position_x + 16 > 223
                    or self.list_bullets_player[i].position_x < 0
                    or self.list_bullets_player[i].position_y + 16 > 255
                    or self.list_bullets_player[i].position_y < 0
            ):
                removed.append(i)
        removed.sort()
        # removed from the end so no error sows
        if len(removed) > 0:
            for i in range(len(removed) - 1, -1, -1):
                del (self.list_bullets_player[removed[i]])

    def draw(self):
        # we call the draw function of each of the bullets
        counter = len(self.list_bullets_player)
        for i in range(0, counter, 1):
            self.list_bullets_player[i].draw()
