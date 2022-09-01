import math
sidesOfTriangle = [int(i) for i in input().split()]
def areaOfTriangle(sidesOfTriangle):
    s = (sidesOfTriangle[0] + sidesOfTriangle[1] + sidesOfTriangle[2])/2
    area = s*(s-sidesOfTriangle[0])*(s-sidesOfTriangle[1])*(s-sidesOfTriangle[2])
    area=format(math.sqrt(area),'.2f')
    print(area)
areaOfTriangle(sidesOfTriangle)