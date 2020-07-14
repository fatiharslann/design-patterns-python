from pprint import pprint

class Point:
    x: int = 0
    y: int = 0

    def __init__(self, point = None, x = None, y = None):
        if(point is None):
            self.x = x
            self.y = y
        else:
            self.x = point.x
            self.y = point.y

class Line:
    start: Point = None
    end: Point = None
               
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
    
    def deepCopy(self):
        return Line(Point(point= self.start),Point(point=self.end))

    def __repr__(self):  
        return "Line Start-X: %s Start-X: %s End-X : %s End-Y : %s " % (self.start.x, self.start.y, self.end.x, self.end.y)

class Client:
    def __init__(self):
        pointStart = Point(x=1,y=5)
        pointEnd = Point(x=2,y=4)
        line1 = Line(pointStart, pointEnd)

        pprint(line1)

        line2 = line1.deepCopy()
        line2.start.x = 15

        pprint(line2)
        

if(__name__ == "__main__"):
    Client()