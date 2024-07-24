from enum import Enum
from random import randint
from copy import deepcopy


class CellAutomate:
    def __init__(self, width: int, height: int) -> None:
        self.__gameBoard = GameBoard(width, height)

    def calcNextState(self):
        self.__gameBoard.calcNextState()

    def getCurrentState(self):
        return self.__gameBoard.getCurrentState()
    
    def getNextState(self):
        return self.__gameBoard.getNextState()
    
    def getNeighboursMatrix(self):
        return self.__gameBoard.getNeighboursMatrix()


class GameBoard:

    class CellState(Enum):
        ALIVE = 1
        DIED = 0

    def __init__(self, width: int, height: int) -> None:
        self.__widthInCells = width
        self.__heightInCells = height
        self.__currentCellMatrix = [[0 for _ in range(self.__widthInCells)] for _ in range(self.__heightInCells)]
        for i in range(self.__heightInCells):
            for j in range(self.__widthInCells):
                    self.__currentCellMatrix[i][j] = randint(0, 1)
        self.__nextCellMatrix = deepcopy(self.__currentCellMatrix)
        self.__neighboursNumberMatrix = [[0 for _ in range(self.__widthInCells)] for _ in range(self.__heightInCells)]

    def getWidthInCells(self):
        return self.__widthInCells
    
    def getHeightInCells(self):
        return self.__heightInCells

    def getCurrentState(self):
        return self.__currentCellMatrix
    
    def getNeighboursMatrix(self):
        return self.__neighboursNumberMatrix

    def calcNextState(self):
        self.__updateNeighboursMatrix()
        self.__setNextStateByNeighboursMatrix()
        self.__swapMatrix()

    def __updateNeighboursMatrix(self):
        for indexRow in range(0, self.__heightInCells):
            for indexCol in range(0, self.__widthInCells):
                prevCellState = self.__currentCellMatrix[indexRow][indexCol]
                if prevCellState == GameBoard.CellState.ALIVE.value:
                    self.__incCounterOfNeighbours(indexRow, indexCol)

    def __incCounterOfNeighbours(self, indexRow: int, indexCol: int):
        shifts = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        for shift in shifts:
            neighbourIndexRow = indexRow + shift[1]
            neighbourIndexCol = indexCol + shift[0]
            if neighbourIndexRow < 0 or neighbourIndexRow >= self.__heightInCells:
                neighbourIndexRow = neighbourIndexRow % self.__heightInCells
            if neighbourIndexCol < 0 or neighbourIndexCol >= self.__widthInCells:
                neighbourIndexCol = neighbourIndexCol % self.__widthInCells
            self.__neighboursNumberMatrix[neighbourIndexRow][neighbourIndexCol] += 1

    def __setNextStateByNeighboursMatrix(self):
        for indexRow in range(0, self.__heightInCells):
            for indexCol in range(0, self.__widthInCells):
                prevCellState = self.__currentCellMatrix[indexRow][indexCol]
                numberOfLivingNeighbours = self.__neighboursNumberMatrix[indexRow][indexCol]
                if prevCellState == GameBoard.CellState.ALIVE.value:
                    if numberOfLivingNeighbours < 2 or numberOfLivingNeighbours > 3:
                        self.__nextCellMatrix[indexRow][indexCol] = GameBoard.CellState.DIED.value
                    else:
                        self.__nextCellMatrix[indexRow][indexCol] = GameBoard.CellState.ALIVE.value
                elif prevCellState == GameBoard.CellState.DIED.value:
                    if numberOfLivingNeighbours == 3:
                        self.__nextCellMatrix[indexRow][indexCol] = GameBoard.CellState.ALIVE.value
                    else:
                        self.__nextCellMatrix[indexRow][indexCol] = GameBoard.CellState.DIED.value
                self.__neighboursNumberMatrix[indexRow][indexCol] = 0

    def __swapMatrix(self):
        self.__currentCellMatrix, self.__nextCellMatrix = self.__nextCellMatrix, self.__currentCellMatrix