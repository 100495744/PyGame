import pyxel


class Colision_System:
    def __init__(self, player, enemies: list = [], bullets: list = []):
        self.enemies = enemies
        self.player = player
        self.bullets = bullets
        self.bullets_enemies = []
        # List of hitted objects
        self.Enemies_hit = []
        self.Bullets_hit = []
        self.Bullets_hit_enemies = []

    @property
    def enemies(self):
        return self.__enemies

    @enemies.setter
    def enemies(self, en):
        if type(en) != list:
            raise TypeError("enemies must be a list")
        else:
            self.__enemies = en

    @property
    def bullets(self):
        return self.__bullets

    @bullets.setter
    def bullets(self, bul):
        if type(bul) != list:
            raise TypeError("bullets needs to be a list")
        else:
            self.__bullets = bul

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, pla):
        self.__player = pla

    def update(self):
        # We clear the lists before appending new elements to them
        self.Enemies_hit = []
        self.Bullets_hit = []
        # copy of the bullet list from the player object
        self.bullets = self.player.Bull_manager.list_bullets_player.copy()
        # We call each of the methods
        self.Check_Enemies()
        self.Check_Bullets_enemies()
        self.Chenck_bullets_player()

    # Here we check that the enemies colide with the player
    def Check_Enemies(self):

        counter = 0
        # if the player is turning then it will not sense any colision
        if self.player.turning == True:
            pass
        else:
            # there needs to be anemies in the screen
            if len(self.enemies) > 0:
                for enem in self.enemies:
                    # simple if that checks that the area of the plane is not touching the area of the enemy
                    if (

                            enem.position_x + enem.width > self.player.position_x
                            and enem.position_x < self.player.position_x + self.player.width - 3
                            and enem.position_y < self.player.position_y + self.player.height - 3
                            and enem.position_y + enem.height > self.player.position_y
                    ):
                        # we append the position of the enemy in the list
                        self.Enemies_hit.append(counter)
                        # the player lose health and activates the hurt event
                        self.player.health -= 1
                        self.player.hurt = True
                    counter += 1

    # This function checks that the bullets from the player does not touch any enemies
    def Check_Bullets_enemies(self):

        counter = 0
        # First we iterate each enemy
        if len(self.enemies) > 0:
            for i in range(0, len(self.enemies)):
                counter2 = 0
                # then each bullet is checked for each enemy
                for bull in self.bullets:

                    if (
                            self.enemies[i].position_x + self.enemies[i].width > bull.position_x
                            and self.enemies[i].position_x < bull.position_x + bull.width
                            and self.enemies[i].position_y < bull.position_y + bull.height
                            and self.enemies[i].position_y + self.enemies[i].height > bull.position_y
                    ):
                        # We append the position in the list of the bullets and enemies
                        self.Enemies_hit.append(counter)
                        self.Bullets_hit.append(counter2)
                    counter2 += 1
                counter += 1

    # We check that any enemy bullet does not hit the player.
    def Chenck_bullets_player(self):

        counter = 0
        # if the player is turning then it does not check any colision
        if self.player.turning == True:
            pass
        else:
            # we create a list with all the bullets created by all the enemies
            bullet_list = []
            for enem in self.enemies:
                for bullet in enem.Bull_Manager.list_bullets_player:
                    bullet_list.append(bullet)

            # now we look if any of those bullets colide with the player
            for enem in bullet_list:
                print(bullet_list)
                if (
                        enem.position_x + enem.width > self.player.position_x
                        and enem.position_x < self.player.position_x + self.player.width - 3
                        and enem.position_y < self.player.position_y + self.player.height - 3
                        and enem.position_y + enem.height > self.player.position_y
                ):
                    # we activate the player hurt event
                    self.player.health -= 1
                    self.player.hurt = True
