from abc import ABC, abstractmethod
from enum import Enum


class ShapeEnum(Enum):
    RECTANGLE = 1
    SQUARE = 2

class IShape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Rectangle(IShape):

    def draw(self):
        print("Draw a rectangle!")

class Square(IShape):

    def draw(self):
        print("Draw a square!")

class RoundedRectangle(IShape):
    
    def draw(self):
        print("Draw a rounded rectangle!")

class RoundedSquare(IShape):
    
    def draw(self):
        print("Draw a rounded square!")

class IShapeFactory(ABC):
    @abstractmethod
    def getShape(self,shapeType: int):
        pass

class ShapeFactory(IShapeFactory): 

    def getShape(self, ShapeType: ShapeEnum) -> IShape:
        if(ShapeType == ShapeEnum.RECTANGLE):
            return Rectangle()
        elif(ShapeType == ShapeEnum.SQUARE):
            return Square()

class RoundedShapeFactory(IShapeFactory):
    
    def getShape(self, shapeType: ShapeEnum):
        if(shapeType == ShapeEnum.RECTANGLE):
            return RoundedRectangle()
        elif(shapeType == ShapeEnum.SQUARE):
            return RoundedSquare()
            
class FactoryProducer():
    
    def getFactory(self, isRounded: bool):
        if(isRounded):
            return RoundedShapeFactory()
        else:
            return ShapeFactory()

class Client():

    def __init__(self):
        factory = FactoryProducer().getFactory(True)
        factory.getShape(ShapeEnum.RECTANGLE).draw()
        

if( __name__  == "__main__"):
    Client()