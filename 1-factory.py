from abc import ABC, abstractmethod
from enum import Enum


class ShapeEnum(Enum):
    RECTANGLE = 1
    CIRCLE = 2
    SQUARE = 3


class IShape(ABC):
    def draw(self):
        pass


class Rectangle(IShape):

    def draw(self):
        print("Draw a rectangle!")


class Square(IShape):

    def draw(self):
        print("Draw a square!")


class Circle(IShape):

    def draw(self):
        print("Draw a circle!")


class ShapeFactory():

    def getShape(self, ShapeType: ShapeEnum) -> IShape:
        if(ShapeType == ShapeEnum.CIRCLE):
            return Circle()
        elif(ShapeType == ShapeEnum.RECTANGLE):
            return Rectangle()
        elif(ShapeType == ShapeEnum.SQUARE):
            return Square()

            
class Client():

    def __init__(self):
        factory = ShapeFactory()
        factory.getShape(ShapeEnum.CIRCLE).draw()
        

if( __name__  == "__main__"):
    Client()