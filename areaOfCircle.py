import math
Radius =int(input())
PI=format(int(math.pi),'.2f')
def areaOfCircle(Radius):
    areaOfCircle = PI * (Radius**2)
    areaOfCircle=format(areaOfCircle,'.2f')
    print(areaOfCircle)
areaOfCircle(Radius)

print(PI)