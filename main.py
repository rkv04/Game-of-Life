import pygame as pg
from mainwindow import MainWindow
from cellauto import CellAutomate


def main():
    pg.init()

    WIDTH_IN_CELLS = 60
    HEIGHT_IN_CELLS = 60

    window = MainWindow(WIDTH_IN_CELLS, HEIGHT_IN_CELLS)
    cellAutomate = CellAutomate(WIDTH_IN_CELLS, HEIGHT_IN_CELLS)

    clock = pg.time.Clock()
    running = True
    FPS = 15

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        window.drawState(cellAutomate.getCurrentState())
        cellAutomate.calcNextState()
        clock.tick(FPS)
        pg.display.flip()
    pg.quit()


if __name__ == '__main__':
    main()