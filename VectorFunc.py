

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
        return Point(x, y, z)
    return Point(x, y)

def Subtract(self, EndPoint):
    x = self.x - EndPoint.x
    y = self.y - EndPoint.y
    if self.Is3D:
        z = self.z - EndPoint.z
        return Point(x, y, z)
    return Point(x, y)

def Scale(self, Scale):
    x = self.x*Scale
    y = self.y*Scale
    if self.Is3D:
        z = self.z * Scale
        return Point(x, y, z)
    return Point(x,y)

def MidPoint(self, EndPoint):
    nX = (self.x + EndPoint.x) / 2
    nY = (self.y + EndPoint.y) / 2
    if self.Is3D:
        nZ = (self.z + EndPoint.z) / 2
        return Point(nX, nY, nZ)
    return Point(nX, nY)
    


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

def Distance(self, Point):
    value = pow(Point.x - self.x, 2) + pow(Point.y - self.y, 2)
    if self.Is3D and Point.Is3D:
        value += pow(Point.z - self.z,2)
    return sqrt(value)

def length(self):
    value = pow(self.x, 2) + pow(self.y, 2)
    if self.Is3D:
        value += pow(self.z,2)
    
    return sqrt(value)
    

def Angle(V1, V2):
    xy = DotProduct(V1,V2)
    #||X|| = sqrt(x^2 + y^2)
    absV1 = sqrt(GetAbs(V1))
    absV2 = sqrt(GetAbs(V2))

    return degrees(acos(xy/(absV1 * absV2)))


if __name__ == '__main__':
    U = Point(3,2)
    V = Point(1,5)
    W = Point(2, -3)

    print("Problem 1")
    print("=> Part (a)\n -> U + V = {0},\n -> V - U = {1},\n -> -3W = {2},\n -> U+V-3W = {3}\n".format(
        Add(U, V).GetDis(), 
        Subtract(V, U).GetDis(),
        Scale(W, -3).GetDis(),
        Subtract(Add(U, V), Scale(W, 3)).GetDis()
    ))

    print("=> Part (c)\n -> U.W = {0},\n -> (U+V).(-3W) = {1},\n -> (U-V).(U-V-3W) = {2}\n".format(
        DotProduct(U, W),
        DotProduct(Add(U, V), Scale(W,-3)),
        DotProduct(Subtract(U, V), Subtract(Subtract(U, V), Scale(W, 3)))
    ))


    print("Part (d) => Angle between U and V = {0} ".format(Angle(U, V)))
    print("Part (e) => Angle between V-U and W-U = {0} ".format(Angle(Subtract(V, U), Subtract(W, U))))

    print("Problem 2:") 
    P = Point(2, 5)
    Q = Point(4, -1)
    R = Point(5, 2)
    print("=> Part (a)\n MidPoints for \n Line PQ = {0},\n Line PR = {1}\n".format(MidPoint(P, Q).GetDis(), MidPoint(P, R).GetDis()))
    print("=> Part (b)\n MidPoints for \n Line PQ-PR = {0}".format(MidPoint(MidPoint(P, Q), MidPoint(P, R)).GetDis()))

    


    
        


    
