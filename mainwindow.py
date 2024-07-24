import pygame as pg
from cellauto import GameBoard
from enum import Enum


class MainWindow:

    def __init__(self, widthInCells: int, heightInCells: int) -> None:
        self.__cellSideLenght = 10
        self.__widthInCells = widthInCells
        self.__heightInCells = heightInCells
        pg.display.set_caption('Game of Life')
        widthInPixsels = self.__widthInCells * self.__cellSideLenght + self.__widthInCells
        heightInPixsels = self.__heightInCells * self.__cellSideLenght + self.__heightInCells
        self.__screen = pg.display.set_mode((widthInPixsels, heightInPixsels))
        self.__screen.fill((255, 255, 255))

    class Colors(Enum):
        ALIVE = (0, 160, 0)
        DIED = (255, 255, 255)

    def drawState(self, stateMatrix):
        self.__screen.fill(MainWindow.Colors.DIED.value)
        for indexRow in range(self.__heightInCells):
            for indexCol in range(self.__widthInCells):
                cellState = stateMatrix[indexRow][indexCol]
                if cellState == GameBoard.CellState.DIED.value:
                    continue
                x = self.__cellSideLenght * indexCol + indexCol
                y = self.__cellSideLenght * indexRow + indexRow
                pg.draw.rect(self.__screen, MainWindow.Colors.ALIVE.value,
                             (x, y, self.__cellSideLenght, self.__cellSideLenght))