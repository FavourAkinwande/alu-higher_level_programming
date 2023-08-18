#!/usr/bin/python3
"""
defining a class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialising instance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """
        string representation of instance (obj)
        """
        return (f"[{self.__class__.__name__}] ({self.id})"
                f" {self.__x}/{self.__y} - {self.__width}/{self.__height}")

    @property
    def width(self):
        """
        property getter
        """
        return self.__width

    @property
    def height(self):
        """
        property getter
        """
        return self.__height

    @property
    def x(self):
        """
        property getter
        """
        return self.__x

    @property
    def y(self):
        """
        property getter
        """
        return self.__y

    @width.setter
    def width(self, width):
        """
        property setter
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """
        property;setter
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """
        property setter
        """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """
        property setter
        """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        evaluating the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        displaying a string repr of the rectangle
        """
        for i in range(self.__y):
            print("")
        x = " " * self.__x
        s = x + "#" * self.__width
        for i in range(self.__height):
            print(s)

    def update(self, *args, **kwargs):
        """
        updating the attribut of rectangle
        Args:
            args: list of argument
            kwargs: list of keyword arguments
        """
        arg = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for i in range(len(args)):
                setattr(self, arg[i], args[i])
        elif kwargs:
            for attr in kwargs:
                setattr(self, attr, kwargs[attr])
        else:
            raise ValueError("update: positional and/or keyword arg required")

    def to_dictionary(self):
        """
        get a dict repr of a rectangle
        """
        a = self.__dict__
        my_dict = {}
        for key, value in a.items():
            if len(key) > 2:
                my_dict[key[12:]] = value
            else:
                my_dict[key] = value
        return my_dict
