from numpy import pi


def get_circle_area(r):
    a = pi * r ** 2
    return a


radius = 10
area = get_circle_area(radius)
print({area})
