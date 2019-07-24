'''
1. Given four points in the plane, how would you check if they are the vertices of a rectangle?
2. How would you check if two rectangles, not necessarily aligned with the X and Y axes, intersect?
'''

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def ext_prod(self, other):
        return self.x * other.y - self.y * other.x

    
class Rectangle():
    def __init__(self, p1, p2, p3, p4):
        dist1 = (p1-p2)*(p1-p2)
        dist2 = (p1-p3)*(p1-p3)
        dist3 = (p1-p4)*(p1-p4)
        max_dist = max(dist1, dist2, dist3)
        self.p = [p1, p2, p3, p4]
        if(dist1 == max_dist):
            self.p[2] = p2
            self.p[1] = p3
        elif(dist3 == max_dist):
            self.p[2] = p4
            self.p[3] = p3

    def is_intersect_with_line(self, p1, p2):
        for i in range(4):
            v1 = self.p[i]
            v2 = self.p[(i+1)%4]
            sgn1 = sgn((v2 - v1).ext_prod(p1 - v1))
            sgn2 = sgn((v2 - v1).ext_prod(p2 - v1))
            sgn3 = sgn((p2 - p1).ext_prod(v1 - p1))
            sgn4 = sgn((p2 - p1).ext_prod(v2 - p1))
            if(sgn1 != sgn2 and sgn3 != sgn4):
                return True
            elif(sgn1 * sgn2 <= 0 and sgn3 * sgn4 <= 0):
                return True
        return False

    def is_intersect_with_rectangle(self, rec):
        for i in range(4):
            v1 = rec.p[i]
            v2 = rec.p[(i+1)%4]
            if(self.is_intersect_with_line(v1, v2)):
                return True
        return False

    
def sgn(x):
    if(x > 0):
        return 1
    elif(x < 0):
        return -1
    else:
        return 0


def q1(p1, p2, p3, p4):
    dist1 = (p1-p2)*(p1-p2)
    dist2 = (p1-p3)*(p1-p3)
    dist3 = (p1-p4)*(p1-p4)
    max_dist = max(dist1, dist2, dist3)
    if(dist1 + dist2 + dist3 != 2*max_dist):
        return False
    
    if(dist1 == max_dist):
        return p1+p2 == p3+p4
    elif(dist2 == max_dist):
        return p1+p3 == p2+p4
    else:
        return p1+p4 == p2+p3

    
def q2(rec1, rec2):
    if(not(q1(rec1.p[0], rec1.p[1], rec1.p[2], rec1.p[3]) and q1(rec2.p[0], rec2.p[1], rec2.p[2], rec2.p[3]))):
        print('Not rectangle')
        exit()
        
    return rec1.is_intersect_with_rectangle(rec2)


if __name__ == '__main__':
    print(q1(Point(3, 0), Point(7, 3), Point(4, 7), Point(0, 4)))
    print(q1(Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 2)))

    rec1 = Rectangle(Point(3, 0), Point(7, 3), Point(4, 7), Point(0, 4))
    rec2 = Rectangle(Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1))
    rec3 = Rectangle(Point(0, 0), Point(2, 0), Point(0, 2), Point(2, 2))
    print(q2(rec1, rec2))
    print(q2(rec1, rec3))
    print(q2(rec2, rec3))
