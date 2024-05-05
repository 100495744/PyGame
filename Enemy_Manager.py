import random

import Bullet_manager
import Bullets
import Regular_Enemy
import pyxel
import time
import Red_Enemy
import Big_Enemy
import Chungus_Enemy


class Enemy_Manager:
    def __init__(self):
        # Lists of enemies
        self.Regular_Enemy = []
        self.Red_Enemy = []
        self.Total_Enemies = []

        self.dificulty = 0
        self.spawns = 1
        # parameters for colisions
        self.enemies_hit = []
        self.bullets_hit = []

        # parameters for firing at the player
        self.position_player_x = 0
        self.position_player_y = 0
        # This parameters are used when creating the formations of red Enemies.
        self.spawns_red_enemy = 5
        self.inital_y = 0
        self.direction = 2
        self.spawning_red_enemies = False
        # Parameters for Time management.
        self.time_last_frame = time.time()
        self.dt = 0
        self.dt_spawner = 3
        self.last_time_spawn = 0

        # Difficulty levels.
        self.Dificulty1 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 1, 3]
        self.Dificulty2 = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1]
        self.Dificulty3 = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
        self.Dificulty4 = [0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
        self.dificulty = 1
        self.score = 0

    def update(self):
        # we use the time function and ecuations to calculate the time between events
        time_this_frame = time.time()
        self.dt = time_this_frame - self.time_last_frame
        self.dt_spawner = time_this_frame - self.last_time_spawn

        removed = []
        if len(self.Total_Enemies) > 0:
            for i in range(0, len(self.Total_Enemies) - 1):
                # We give each of the enemies the position of the player that instant
                self.Total_Enemies[i].player_position_x = self.position_player_x
                self.Total_Enemies[i].player_position_y = self.position_player_y
                self.Total_Enemies[i].update()
                # We check that the enemy is not outside boundaries
                if (self.Total_Enemies[i].position_x + self.Total_Enemies[i].width > 235
                        or self.Total_Enemies[i].position_x < -10
                        or self.Total_Enemies[i].position_y + self.Total_Enemies[i].height > 266
                        or self.Total_Enemies[i].position_y < -10
                ):
                    removed.append(i)
            # We remove the enemies outside the boundaries
            removed.sort()
            if len(removed) > 0:
                for i in range(len(removed) - 1, -1, -1):
                    del (self.Total_Enemies[removed[i]])

                    # Bullets of its enemy hitted
            print(self.bullets_hit)
            if len(self.bullets_hit) > 0:
                counter = 0
                for bullet in self.bullets_hit:
                    self.Total_Enemies[counter].Bull_manager.bullets_hitted = bullet
                    counter += 1

            # Enemies hited by player.
            if len(self.enemies_hit) > 0:
                # For cheking that an enemy is not repeated
                Same_value = []
                for i in range(0, len(self.enemies_hit) - 1):
                    for j in range(i, len(self.enemies_hit) - 1):
                        if self.enemies_hit[i] == self.enemies_hit[j]:
                            Same_value.append(i)
                for k in Same_value:
                    del (self.enemies_hit[k])
                # We short the enemy list for no errors
                len_enemies_hit = len(self.enemies_hit)
                self.enemies_hit.sort()
                if len(self.enemies_hit) > 0:
                    for i in range(len_enemies_hit - 1, -1, -1):
                        # If the enemy needs more than one bullet to die then it will just reduce it health.
                        if type(self.Total_Enemies[self.enemies_hit[i]]) == Big_Enemy.Big_Enemmy or \
                                type(self.Total_Enemies[self.enemies_hit[i]]) == Chungus_Enemy.Chungus_Enemy:
                            self.Total_Enemies[self.enemies_hit[i]].health -= 1
                            if self.Total_Enemies[self.enemies_hit[i]].health < 0:
                                del (self.Total_Enemies[self.enemies_hit[i]])
                        # if the health of the enemy is 0 then we delete it
                        else:
                            del (self.Total_Enemies[self.enemies_hit[i]])

        # Setting the difficulty depening on the score.
        elif self.score > 4000 and self.score < 6500:
            self.dificulty = 2
        elif self.score > 6500 and self.score < 10000:
            self.dificulty = 3
        elif self.score > 10000:
            self.dificulty = 4

        # Spawning and difficulty system.
        if self.dt > 1.5:
            # checking the difficulty
            if self.dificulty == 1:
                spawn = random.choice(self.Dificulty1)
            elif self.dificulty == 2:
                spawn = random.choice(self.Dificulty2)
            elif self.dificulty == 3:
                spawn = random.choice(self.Dificulty3)
            else:
                spawn = random.choice(self.Dificulty4)
            # depending on the number selected in the dificulty list a type of enemy will be spawned
            if spawn == 0:
                pass
            elif spawn == 1:
                self.spawner_regular_enemies()

            elif spawn == 2:

                self.spawning_red_enemies = True

            elif spawn == 3:
                self.spawn_big_enemy()

            elif spawn == 4:
                self.spawn_chungus_enemy()
            self.time_last_frame = time.time()
        # Red enemies are spawned in formation so they will be created in different time intervals.
        if self.spawning_red_enemies == True:
            if self.dt_spawner > 0.25:
                self.spawner_red_enemies()
                self.last_time_spawn = time.time()

    # draw function calls the draw fucntion in each of the enemies
    def draw(self):
        if len(self.Total_Enemies) > 0:
            for i in range(0, len(self.Total_Enemies) - 1):
                self.Total_Enemies[i].draw()

    # It just creates 4 random regular enemies
    def spawner_regular_enemies(self):
        for i in range(0, 4):
            self.Total_Enemies.append(Regular_Enemy.Regular_Enemy(16, 16, random.randint(40, 230), 0, 1, 156, 199, 4))

    # the spawner of red enemy creates a formation of red enemies
    def spawner_red_enemies(self):
        if self.spawns_red_enemy == 5:
            # we decide if they come from the left or the right
            self.direction = random.randint(0, 2)
            # random y position from where they spawn
            self.initial_y = random.randint(60, 200)
            # first enemy - leader of the group: the velocity and position change depending on the spawn position
            if self.direction == 0:
                self.Total_Enemies.append(Red_Enemy.Red_Enemy(16, 16, 1, self.initial_y, 1, 156, 218, 3))
            else:
                self.Total_Enemies.append(Red_Enemy.Red_Enemy(16, 16, 207, self.initial_y, 1, 197, 218, -3, False))
            self.spawns_red_enemy = 4
            # Second set of enemy spawned: each at each side of the main plane.
        elif self.spawns_red_enemy == 4:
            if self.direction == 0:
                self.Total_Enemies.append(Red_Enemy.Red_Enemy(16, 16, 1, self.initial_y + 16, 1, 156, 218, 3))
                self.Total_Enemies.append(Red_Enemy.Red_Enemy(16, 16, 1, self.initial_y - 16, 1, 156, 218, 3))
            else:
                self.Total_Enemies.append(Red_Enemy.Red_Enemy(16, 16, 207, self.initial_y + 16, 1, 197, 218, -3, False))
                self.Total_Enemies.append(Red_Enemy.Red_Enemy(16, 16, 207, self.initial_y - 16, 1, 197, 218, -3, False))
            self.spawns_red_enemy = 2
            # Final pair of enemy
        elif self.spawns_red_enemy == 2:
            if self.direction == 0:
                self.Total_Enemies.append(Red_Enemy.Red_Enemy(16, 16, 1, self.initial_y + 32, 1, 156, 218, 3))
                self.Total_Enemies.append(Red_Enemy.Red_Enemy(16, 16, 1, self.initial_y - 32, 1, 156, 218, 3))
            else:
                self.Total_Enemies.append(Red_Enemy.Red_Enemy(16, 16, 207, self.initial_y + 32, 1, 197, 218, -3, False))
                self.Total_Enemies.append(Red_Enemy.Red_Enemy(16, 16, 207, self.initial_y - 32, 1, 197, 218, -3, False))
            self.spawns_red_enemy = 0
            # finaly we reset the count for the next formation that spawns
        elif self.spawns_red_enemy == 0:
            self.spawns_red_enemy = 5
            self.spawning_red_enemies = False

    # Spawner for the big enemy, it just gives a chance for it to come from the left or the right
    def spawn_big_enemy(self):
        direcion = random.randint(0, 2)
        if direcion == 0:
            self.Total_Enemies.append(Big_Enemy.Big_Enemmy(24, 32, 60, 16, 0, 6, 72, 2, health=5))
        else:
            self.Total_Enemies.append(Big_Enemy.Big_Enemmy(24, 32, 150, 16, 0, 6, 72, 2, health=5))

    # chungus enemy always spawn from the same place
    def spawn_chungus_enemy(self):
        self.Total_Enemies.append(Chungus_Enemy.Chungus_Enemy(48, 64, 110, 160, 1, 0, 0, 2, health=15))
