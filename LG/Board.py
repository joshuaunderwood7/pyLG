class Location:
    def __init__(self, x=1, y=1, z=1):
        self.x = x
        self.y = y
        self.z = z

    def arrayShift(self):
        self.x-=1
        self.y-=1
        self.z-=1
        return self

    def shiftBack(self):
        self.x+=1
        self.y+=1
        self.z+=1
        return self

    def __repr__(self):
        return '(' + str(self.x) + ', ' + \
               str(self.y) + ', ' + \
               str(self.z) + ')'

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self))


class Board:
    def __init__(self, minx=1, maxx=1, miny=1, maxy=1, minz=1, maxz=1):
        """Default board is 1x1x1 and filled with #'s"""
        self.minX = minx
        self.maxX = maxx
        self.minY = miny
        self.maxY = maxy
        self.minZ = minz
        self.maxZ = maxz
        self.symbol = [ [ ['#' for z in range(maxz)] for y in range(maxy)] for x in range(maxx)]

    def fill(self, symbol):
        """give a character to assign to each square"""
        self.symbol = [ [ [symbol for z in range(self.maxZ)] for y in range(self.maxY)] for x in range(self.maxX)]
        return self

    def canAccess(self, location):
        return (self.minX <= location.x <= self.maxX) and \
               (self.minY <= location.y <= self.maxY) and \
               (self.minZ <= location.z <= self.maxZ)

    def get(self, location):
        if self.canAccess(location):
            location.arrayShift()
            rValue =  self.symbol[location.x][location.y][location.z]
            location.shiftBack()
            return  rValue
        return ''


    def set(self, location, value):
        """Set a specific location to a character value"""
        if self.canAccess(location):
            location.arrayShift()
            self.symbol[location.x][location.y][location.z] = value
            location.shiftBack()
            return True
        return False

    def setUnreachable(self, location):
        """Set a location to the LG system Unrachable symbol"""
        set(location, 'X')
        return self
    def setObstacle(self, location):
        """Set a location to the LG system obstacle symbol"""
        set(location, '$')
        return self


    def rangeOfX(self):
        """Return an eager list of X values"""
        return range(self.minX, self.maxX+1)
    def rangeOfY(self):
        """Return an eager list of Y values"""
        return range(self.minY, self.maxY+1)
    def rangeOfZ(self):
        """Return an eager list of Z values"""
        return range(self.minZ, self.maxZ+1)

    def __repr__(self):
        returnString = ""
        for z in self.rangeOfZ():
            for y in self.rangeOfY():
                for x in self.rangeOfX():
                    returnString += self.get(Location(x,y,z))
                returnString += '\n'
        return returnString

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def getDistanceboard(self):
        return Board(maxx=((self.maxX*2)-1), maxy=((self.maxY*2)-1), maxz=((self.maxZ*2)-1))

    def middle(self):
        """Only returns approximate middle of the distance Board"""
        return Location(self.maxX, self.maxY, self.maxZ)

chessboard    = Board(maxx= 8, maxy=8)
distanceboard = chessboard.getDistanceboard()
chessboard3D  = Board(maxx= 8, maxy=8, maxz=8)

