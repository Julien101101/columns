from settings import *
from columns_game import ColumnsGame
import sys


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Columns.py')
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        self.columns_game = ColumnsGame(self)


    def update(self):
        self.columns_game.update()
        self.clock.tick(FPS)


    def draw(self):
        self.screen.fill(color = FIELD_COLOR)
        self.columns_game.draw()
        pg.display.flip()


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

             
             
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
        # app = App()
        # app = run()


if __name__ == '__main__':
    # * app = App()

    columns = App()
    columns.run()
