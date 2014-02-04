import copy
import Piece as P
import Board as B

#generateDistenceTable' color piece = do
def generateDistenceTable(color, rank, board = B.distanceboard):
    unreachableSymbol = 'X'
    emptyTable = board.getDistanceboard().fill(unreachableSymbol)
    initialPiece = P.Piece()
    initialPiece.setBoard(emptyTable)
    midpoint = board.middle()
    initialPiece.makePiece(color,rank,midpoint)

    validMoves = set()
    for x in emptyTable.rangeOfX():
        for y in emptyTable.rangeOfX():
            if initialPiece.movement(B.Location(x,y)):
                validMoves.add(B.Location(x,y))

    emptyTable.set(midpoint, '0')
    currentTable = copy.deepcopy(emptyTable)
    accum = 1

    for location in validMoves:
        currentTable.set(location, str(accum))

    previousTable = copy.deepcopy(emptyTable)

    while previousTable != currentTable:

        previousTable = copy.deepcopy(currentTable)
        accum += 1
        setOfPieces = {copy.deepcopy(initialPiece.makePiece(color,rank,location)) for location in validMoves}

        validMoves = set()

        for piece in setOfPieces:
            for x in emptyTable.rangeOfX():
                for y in emptyTable.rangeOfX():
                    if piece.movement(B.Location(x,y)):
                        validMoves.add(B.Location(x,y))

        for location in validMoves:
            if currentTable.get(location) == unreachableSymbol:
                currentTable.set(location, str(accum))


    return currentTable


