class Line():
    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def getDistance(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def getSlope(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        return (y2-y1)/(x2-x1)

class Cylinder():
    pi = 3.14

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def getVolume(self):
        return (self.height * Cylinder.pi * self.radius**2)
    
    def getSurfaceArea(self):
        return (2*Cylinder.pi*(self.radius**2) + (2*Cylinder.pi*self.radius*self.height))
        
if __name__ == '__main__':
    c1 = (3,2)
    c2 = (8,10)
    myLine = Line(c1, c2)
    print(myLine.getDistance())
    print(myLine.getSlope())

    myCyl = Cylinder(2, 3)
    print(myCyl.getVolume())
    print(myCyl.getSurfaceArea())

    from SamplePackage import SampleModule
    SampleModule.printSampleModule()

    from SamplePackage.SampleSubPackage import SampleSubModule
    SampleSubModule.printSampleSubModule()


