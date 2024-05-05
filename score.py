import pyxel

class Score:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

    def update(self):
        pass
    def draw(self):
        pyxel.text(self.position_x, self.position_y, "Highest Score", 7)
        pyxel.text(10,10, "1UP", 7)
        pyxel.text(200, 10, "2UP", 7)
class Background:
    def __init__(self, positionx, positiony,scoreX, scoreY):
        self.positionx = positionx
        self.positiony = positiony
        self.position_score_x = scoreX
        self.position_score_y = scoreY


        self.width = 200
        self.height = 240
    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.positionx, self.positiony, 0, 0,0, self.width, self.height)


class Mainmenu:
    def __init__(self,positionxx, positionyy, positionx, positiony,scoreX, scoreY):
        self.positionxx = positionxx
        self.positionyy = positionyy
        self.saying = "Click space to start"
        self.welcome = "Welcome to the 1942 game"
        self.positionx = positionx
        self.positiony = positiony
        self.position_score_x = scoreX
        self.position_score_y = scoreY
        self.width = 200
        self.height = 240

    def update(self):
        pass
    def draw(self):
        #pyxel.cls(2)
        pyxel.text(80, 120, self.saying, 7)
        pyxel.text(80,10, self.welcome,7)
        pyxel.blt(10, 30, 1, 27, 147, 10, 12)
        pyxel.blt(15, 150, 1, 27, 147, 10, 12)
        pyxel.blt(60, 120, 1, 27, 147, 10, 12)
        pyxel.blt(100, 120, 1, 27, 147, 10, 12)
        pyxel.text(self.position_score_x, self.position_score_y, "Highest Score", 7)
        pyxel.text(10, 10, "1UP", 7)
        pyxel.text(200, 10, "2UP", 7)
        pyxel.blt(self.positionx, self.positiony, 0, 0, 0, self.width, self.height)


        pyxel.blt(80, 200, 2, 40, 16, 136, 32)
        pyxel.blt(30, 30, 2, 0, 0, 192, 56)




