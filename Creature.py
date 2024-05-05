import pyxel


class Creature:
    # This is the mother class for any enemy, player, or instance that generally moves in the game.
    # It does just have a scale , position, and sprite parameters.

    def __init__(self, height: int, width: int, x: int, y: int, sprite_image: int,
                 sprite_position_x: int, sprite_position_y: int):
        self.height = height
        self.width = width
        self.position_x = x
        self.position_y = y
        self.sprite_position_x = sprite_position_x
        self.sprite_position_y = sprite_position_y
        self.sprite_image = sprite_image

        self.sprite = pyxel.load("assets/assets.pyxres")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("The height must be an integer")
        elif height < 0:
            raise ValueError("It can not be a negative height")
        else:
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("The height must be an integer")
        elif width < 0:
            raise ValueError("It can not be a negative height")
        else:
            self.__width = width

    @property
    def position_x(self):
        return self.__position_x

    @position_x.setter
    def position_x(self, x):
        if type(x) != int:
            raise TypeError("The position must be an integer")
        else:
            self.__position_x = x

    @property
    def position_y(self):
        return self.__position_y

    @position_y.setter
    def position_y(self, y):
        if type(y) != int:
            raise TypeError("The position must be an integer")
        else:
            self.__position_y = y

    @property
    def sprite_image(self):
        return self.__sprite_image

    @sprite_image.setter
    def sprite_image(self, sprite_image):
        if type(sprite_image) != int:
            raise TypeError("The image needs to be an int")
        elif sprite_image < 0 or sprite_image > 2:
            raise ValueError("The image needs to be between 0 and 2(included) ")
        else:
            self.__sprite_image = sprite_image

    @property
    def sprite_position_x(self):
        return self.__sprite_position_x

    @sprite_position_x.setter
    def sprite_position_x(self, sprite_position):
        if type(sprite_position) != int:
            raise TypeError("The image needs to be an int")

        else:
            self.__sprite_position_x = sprite_position

    @property
    def sprite_position_y(self):
        return self.__sprite_position_y

    @sprite_position_y.setter
    def sprite_position_y(self, sprite_position_y):
        if type(sprite_position_y) != int:
            raise TypeError("The image needs to be an int")

        else:
            self.__sprite_position_y = sprite_position_y

    def update(self):
        pass

    # the draw function just creates the image
    def draw(self):
        pyxel.blt(self.position_x, self.position_y, self.sprite_image, self.sprite_position_x,
                  self.sprite_position_y, self.width, self.height, 1)
