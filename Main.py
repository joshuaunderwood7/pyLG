__author__ = 'joshua'

from LG.Board import chessboard, Board
from LG.DistanceTables import generateDistenceTable

def main():

    y = int(raw_input('How many rows?   :'))
    x = int(raw_input('How many columns?:'))
    z = int(raw_input('How many levels? :'))

    userBoard = Board(maxx = x, maxy = y, maxz = z)

    print
    print "---"
    print

    print "Black Pawn:"
    print generateDistenceTable('black','pawn', userBoard)
    print "White Pawn:"
    print generateDistenceTable('white','pawn', userBoard)
    print "Rook:"
    print generateDistenceTable('black','Rook', userBoard)
    print "Knight:"
    print generateDistenceTable('black','Knight', userBoard)
    print "Bishop:"
    print generateDistenceTable('black','bishop', userBoard)
    print "Queen:"
    print generateDistenceTable('black','queen', userBoard)
    print "King:"
    print generateDistenceTable('black','king', userBoard)

if __name__=='__main__':
    main()