import Board

def MakeRForBoard(board):
    return ( lambda fP, x, y:
             (x != y) and
             (board.minX <= y.x <= board.maxX) and
             (board.minY <= y.y <= board.maxY) and
             (board.minZ <= y.z <= board.maxZ) and
             fP(x, y) )


#--Here are the Movements for Chess

r = MakeRForBoard(Board.chessboard)
r_distance = MakeRForBoard(Board.distanceboard)


# pawns
#--pawns are difficult and this is not corrct
def r_pB(x,y): return ( ( x.x == y.x ) and ((x.y-y.y == -1)) )
def r_pW(x,y): return ( ( x.x == y.x ) and ((x.y-y.y ==  1)) )

#Knights
def r_n(x,y):
    dx = abs(x.x - y.x)
    dy = abs(x.y - y.y)
    return ( ( (dx == 1) and  (dy == 2) ) or
             ( (dx == 2) and  (dy == 1)) )

#Bishop
def r_b(x,y):
    dx = abs(x.x - y.x)
    dy = abs(x.y - y.y)
    return ( (dx <= 8) and
             (dy <= 8) and
             (dx == dy) )

#rook
def r_r(x,y):
    dx = abs(x.x - y.x)
    dy = abs(x.y - y.y)
    sameColOrRow = ((x.x == y.x) or (x.y ==y.y))
    return ( sameColOrRow and
             (dx <= 8) and
             (dy <= 8) )

#queen
def r_q(x,y): return (r_r(x,y) or r_b(x,y))

#king
def r_k(x,y):
    dx = abs(x.x - y.x)
    dy = abs(x.y - y.y)
    return ( (dx <= 1) and (dy <= 1) )


#3D knight
def r_n3d(x,y):
    dx = abs(x.x - y.x)
    dy = abs(x.y - y.y)
    dz = abs(x.z - y.z)
    return ( ( (dx == 0) and  (dy == 1) and (dz == 2) ) or
             ( (dx == 0) and  (dy == 2) and (dz == 1) ) or
             ( (dx == 1) and  (dy == 0) and (dz == 2) ) or
             ( (dx == 1) and  (dy == 2) and (dz == 0) ) or
             ( (dx == 2) and  (dy == 1) and (dz == 0) ) or
             ( (dx == 2) and  (dy == 0) and (dz == 1) ) )

#3D king
def r_k3d(x,y):
    dx = abs(x.x - y.x)
    dy = abs(x.y - y.y)
    dz = abs(x.z - y.z)
    return ( (dx <= 1) and (dy <= 1) and (dz <= 1) )
