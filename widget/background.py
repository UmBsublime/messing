import curses

class Background(object):

    def __init__(self):
        self.HEIGHT = curses.LINES
        self.WIDTH = curses.COLS
        self.BASE_X = 0
        self.BASE_Y = 0

        # WINDOW Declaration
        background_win = curses.newwin(self.HEIGHT, self.WIDTH, self.BASE_Y, self.BASE_X)

        #PREP
        background_win.box()
        background_win.refresh()
