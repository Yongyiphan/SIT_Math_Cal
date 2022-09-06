import matplotlib.pyplot as plt

from math import *
from mpl_toolkits.mplot3d import Axes3D

class Point:
    def __init__(self, X, Y = None, Z = None):
        if isinstance(X, Point):
            self.x = X.x
            self.y = X.y
            self.z = X.z
        else:
            self.x = X
            self.y = Y
            self.z = Z
        self.Is3D = False if Z == None else True
   
    def GetDis(self):
        if self.Is3D:
            return (self.x, self.y, self.z)
        return (self.x, self.y) 

    def Add(self, EndPoint):
        x = self.x + EndPoint.x
        y = self.y + EndPoint.y
        if self.Is3D and EndPoint.Is3D:
            z = self.z + EndPoint.z
            return Vector(x, y, z)
        return Vector(x, y)

    def Subtract(self, EndPoint):
        x = self.x - EndPoint.x
        y = self.y - EndPoint.y
        if self.Is3D:
            z = self.z - EndPoint.z
            return Vector(x, y, z)
        return Vector(x, y)

    def Distance(self, Point):
        value = pow(Point.x - self.x, 2) + pow(Point.y - self.y, 2)
        if self.Is3D and Point.Is3D:
            value += pow(Point.z - self.z,2)
        return sqrt(value)

    



class Vector:
    def __init__(self, X, Y = None, Z = None) -> None:
        if isinstance(X, Point):
            self.x = X.x
            self.y = X.y
            self.z = X.z
        else:
            self.x = X
            self.y = Y
            self.z = Z
        self.Is3D = False if Z == None else True

    
        
    def GetDis(self):
        return (self.x, self.y, self.z) if self.Is3D else (self.x, self.y)

    def Add(self, EndPoint):
        x = self.x + EndPoint.x
        y = self.y + EndPoint.y
        if self.Is3D and EndPoint.Is3D:
            z = self.z + EndPoint.z
            return Vector(x, y, z)
        return Vector(x, y)

    def Subtract(self, EndPoint):
        x = self.x - EndPoint.x
        y = self.y - EndPoint.y
        if self.Is3D:
            z = self.z - EndPoint.z
            return Vector(x, y, z)
        return Vector(x, y)

    def Scale(self, Scale):
        x = self.x*Scale
        y = self.y*Scale
        if self.Is3D:
            z = self.z * Scale
            return Vector(x, y, z)
        return Vector(x,y)

    def MidPoint(self, EndPoint):
        nX = (self.x + EndPoint.x) / 2
        nY = (self.y + EndPoint.y) / 2
        if self.Is3D:
            nZ = (self.z + EndPoint.z) / 2
            return Vector(nX, nY, nZ)
        return Vector(nX, nY)
        

    def DotProduct(self, Point):
        x = self.x * Point.x
        y = self.y * Point.y
        if self.Is3D and Point.Is3D:
            z = self.z * Point.z
            return x + y + z 
        return x+y

    def GetAbs(self):
        absValue = abs(pow(self.x, 2)) + abs(pow(self.y, 2))
        if self.z is not None:
            absValue += abs(pow(self.z, 2))
        return absValue

    def length(self):
        value = pow(self.x, 2) + pow(self.y, 2)
        if self.Is3D:
            value += pow(self.z,2)
        return sqrt(value)

    def Angle(self, V2):
        xy = self.DotProduct(V2)
        #||X|| = sqrt(x^2 + y^2)
        absV1 = sqrt(self.GetAbs())
        absV2 = sqrt(V2.GetAbs())
        return degrees(acos(xy/(absV1 * absV2)))

    def Projection(self, V2):
            V1V2 = self.DotProduct(V2)
            V2V2 = V2.DotProduct(V2)
            return V2.Scale(V1V2/V2V2)
        
    def Multiply(V1, V2):
        if V1.Is3D and V2.Is3D:
            return Point(V1.x*V2.x, V1.y *V2.y, V1.z * V2.z)
        return Point(V1.x * V2.x, V1.y *V2.y)

if __name__ == '__main__':
    U = Vector(-1, -2)
    V = Vector( 3, 1)
    W = Vector(6, 4)



    Var =  V.Projection(U).GetDis()
    V2 = V.Scale(3)
    print(f"{Var}, {V2.GetDis()}")




    
        


    
