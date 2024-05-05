import pyxel
import score
import Chungus_Enemy
import Regular_Enemy
import Red_Enemy
import Big_Enemy


class Background:
    def __init__(self, positionx, positiony, scoreX, scoreY):

        self.saying = "Click space to start"
        self.welcome = "Welcome to the 1942 game"
        self.positionx = positionx
        self.positiony = positiony
        self.position_score_x = scoreX
        self.position_score_y = scoreY
        self.width = 200
        self.height = 240
        self.value = 0
        self.turns = 3
        # parameters for the scoring system
        self.score = 0
        self.enemy_dead = []
        self.Total_Enemies = []

    @property
    def positionx(self):
        return self.__positionx

    @positionx.setter
    def positionx(self, p):
        if type(p) != int:
            raise TypeError("The position X must be an int")
        else:
            self.__positionx = p

    @property
    def positiony(self):
        return self.__positiony

    @positiony.setter
    def positiony(self, p):
        if type(p) != int:
            raise TypeError("The position Y must be an int")
        else:
            self.__positiony = p

    @property
    def position_score_x(self):
        return self.__position_score_x

    @position_score_x.setter
    def position_score_x(self, x):
        if type(x) != int:
            raise TypeError("The position of the score must be an int")
        else:
            self.__position_score_x = x

    @property
    def position_score_y(self):
        return self.__position_score_y

    @position_score_y.setter
    def position_score_y(self, y):
        if type(y) != int:
            raise TypeError("The positon of the score must be an int")
        else:
            self.__position_score_y = y

    def update(self):
        # We call the scoring system and check that space is pressed for the inital game
        self.Scoring()
        if pyxel.btn(pyxel.KEY_SPACE):
            self.value = 1

    def draw(self):

        if self.value == 0:
            # Background of the initial
            pyxel.text(80, 120, self.saying, 7)
            pyxel.text(80, 10, self.welcome, 7)
            pyxel.blt(10, 30, 1, 27, 147, 10, 12)
            pyxel.blt(15, 150, 1, 27, 147, 10, 12)
            pyxel.blt(60, 120, 1, 27, 147, 10, 12)
            pyxel.blt(100, 120, 1, 27, 147, 10, 12)
        else:
            # Background game
            self.value = 1
            pyxel.text(self.position_score_x, self.position_score_y, "Highest Score: 10570", 7)
            pyxel.text(10, 10, "1UP", 7)
            pyxel.text(10, 20, str(self.score), 7)
            # text for the turns left
            pyxel.text(10, 30, str("Turns left: " + str(self.turns)), 7)
            pyxel.text(200, 10, "2UP", 7)
            # we change the frase so it does not overlap
            self.saying = " "
            self.welcome = " "

    def Scoring(self):
        # For scoring we check the type enemy of the dead enemies list and sum the correponding value.
        for elem in self.enemy_dead:
            print(elem)
            if type(self.Total_Enemies[elem]) == Regular_Enemy.Regular_Enemy:
                self.score += 50
            elif type(self.Total_Enemies[elem]) == Red_Enemy.Red_Enemy:
                self.score += 75
            elif type(self.Total_Enemies[elem]) == Big_Enemy.Big_Enemmy:
                self.score += 150
            elif type(self.Total_Enemies[elem]) == Chungus_Enemy.Chungus_Enemy:
                self.score += 500

    def player_dead(self):
        # if player dead we saw a text
        pyxel.text(45, 150, "**** PRESS X TO CONTINUE **** ", 7)
