import R
import Board

class Piece:
    def __init__(self):
        self.xPos = 0
        self.yPos = 0
        self.zPos = 0
        self.xVel = 0
        self.yVel = 0
        self.zVel = 0
        self.color = 'grey'
        self.rank = 'none'
        self.board = Board.chessboard

    def setBoard(self, board):
        self.board = board

    def makePiece(self, color, rank, location):
        self.xPos = location.x
        self.yPos = location.y
        self.zPos = location.z
        self.rank = rank
        self.color = color
        return self

    def movement(self, y):
        if(self.rank.upper()=='PAWN' and self.color.upper()=="BLACK"):
            return R.MakeRForBoard(self.board)(R.r_pB, Board.Location(self.xPos, self.yPos, self.zPos), y)
        elif(self.rank.upper()=='PAWN' and self.color.upper()=="WHITE"):
            return R.MakeRForBoard(self.board)(R.r_pW, Board.Location(self.xPos, self.yPos, self.zPos), y)
        elif(self.rank.upper()=='BISHOP'):
            return R.MakeRForBoard(self.board)(R.r_b, Board.Location(self.xPos, self.yPos, self.zPos), y)
        elif(self.rank.upper()=='KNIGHT'):
            return R.MakeRForBoard(self.board)(R.r_n, Board.Location(self.xPos, self.yPos, self.zPos), y)
        elif(self.rank.upper()=='ROOK'):
            return R.MakeRForBoard(self.board)(R.r_r, Board.Location(self.xPos, self.yPos, self.zPos), y)
        elif(self.rank.upper()=='QUEEN'):
            return R.MakeRForBoard(self.board)(R.r_q, Board.Location(self.xPos, self.yPos, self.zPos), y)
        elif(self.rank.upper()=='KING'):
            return R.MakeRForBoard(self.board)(R.r_k, Board.Location(self.xPos, self.yPos, self.zPos), y)
        else: return False


    def __repr__(self):
        returnString =  self.color + " " +\
                        self.rank + " at (" + \
                        str(self.xPos) + "," + str(self.yPos) + ")"
        return returnString

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self))


'''

--needs to include more than the movment check, needs to remove oposing piece
--I think that this would also be a good place to implement Pawn movments...
movePice piece locat
    | (movement piece) locat = makePiece (color piece) (rank piece) locat 
    | otherwise              = piece

genaricBoardMovments board piece = [(x,y) | x <- (boardXrange board), y <- (boardYrange board), movement piece (x,y)]
chessBoardMovments piece = [(x,y) | x <- [1..8], y <- [1..8], movement piece (x,y)]

pawnsB   = [makePiece Black Pawn   (x,2) | x <- [1..8]]
rooksB   = [makePiece Black Rook   (x,1) | x <- [1,8]]
knishtsB = [makePiece Black Knight (x,1) | x <- [2,7]]
bishopsB = [makePiece Black Bishop (x,1) | x <- [3,5]]
queenB   = [makePiece Black Queen  (x,1) | x <- [4]]
kingB    = [makePiece Black King   (x,1) | x <- [5]]

pawnsW   = [makePiece White Pawn   (x,7) | x <- [1..8]]
rooksW   = [makePiece White Rook   (x,8) | x <- [1,8]]
knishtsW = [makePiece White Knight (x,8) | x <- [2,7]]
bishopsW = [makePiece White Bishop (x,8) | x <- [3,5]]
queenW   = [makePiece White Queen  (x,8) | x <- [4]]
kingW    = [makePiece White King   (x,8) | x <- [5]]

main = do

    print $ map chessBoardMovments pawnsB

{--
    let p1 = makePiece Black Pawn (2,6)
    print $ location p1
    print $ chessBoardMovments p1
    let p1_2 = movePice p1 (2,5)
    print $ chessBoardMovments p1_2
--}

    print $ head [1..8]
    print $ last [1..8]
    print "bye"
'''