#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class definition"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of the rectangle object """
        return (self.__width * self.__height)

    def display(self):
        """print the rectangle"""
        if self.__y != 0:
            for k in range(self.__y):
                print()
        for i in range(self.__height):
            if self.__x != 0:
                for h in range(self.__x):
                    print(" ", end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """string format"""
        my_str = "[" + str(self.__class__.__name__) + "] "
        my_str += "(" + str(self.id) + ") " + str(self.__x)
        my_str += "/" + str(self.__y)
        my_str += " - " + str(self.__width) + "/" + str(self.__height)
        return (my_str)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None and len(args) is not 0:
            attr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        my_dic = {}
        attr = ['id', 'size', 'x', 'y']

        for key in attr:
            if key == 'size':
                my_dic['width'] = getattr(self, 'width')
                my_dic['height'] = getattr(self, 'height')
            else:
                my_dic[key] = getattr(self, key)

        return (my_dic)
