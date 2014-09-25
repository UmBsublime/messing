#!/usr/bin/env python
import curses
import menu

class MyApp():

    def __init__(self, stdscreen):

        global win_size

        # WINDOW Declaration
        menu.BaseWin() # --> required
        menuWin  = curses.newwin(win_size['MENU_HEIGHT'], win_size['MENU_WIDTH'],
                                 win_size['MENU_BASE_Y'], win_size['MENU_BASE_X'])

        contentWin  = curses.newwin(win_size['CONTENT_HEIGHT'], win_size['CONTENT_WIDTH'],
                                    win_size['CONTENT_BASE_Y'], win_size['CONTENT_BASE_X'])

        statusWin  = curses.newwin(win_size['STATUS_HEIGHT'], win_size['STATUS_WIDTH'],
                                   win_size['STATUS_BASE_Y'], win_size['STATUS_BASE_X'])

        self.contentWin = menu.ContentWin(contentWin)
        self.contentWin.write('Hello welcome to this beta interface')
        self.statusWin = menu.StatusWin(statusWin)

        self.statusWin.write('>DEMO<  cols: {} lines: {}'.format(curses.COLS, curses.LINES))

        subsubmenu_items = [
                ('test1', self.contentWin.write),
                ('test2', self.contentWin.write)
                ]
        subsubmenu = menu.Menu(subsubmenu_items, menuWin)
        submenu_items = [
                ('beep', self.contentWin.write),
                ('flash', self.contentWin.write),
                ('subsubmenu', subsubmenu.display)
                ]
        submenu = menu.Menu(submenu_items, menuWin)

        main_menu_items = [
                ('beep', self.contentWin.write),
                ('blah', self.contentWin.write),
                ('abra', self.contentWin.write),
                ('cadabra', self.contentWin.write),
                ('hello', self.contentWin.write),
                ('world', self.contentWin.write),
                ('debug', self.contentWin.write),
                ('testing', self.contentWin.write),
                ('junk', self.contentWin.write),
                ('submenu', submenu.display)
                ]

        main_menu = menu.Menu(main_menu_items, menuWin)
        main_menu.display()

class ScreenToSmall(Exception):
    def __init__(self):
        self.message = 'Screen has to be minimum of 24x80'


def main(stdscr):
    if curses.LINES <= 24:
        raise ScreenToSmall
    if curses.COLS <= 80:
        raise ScreenToSmall


    # color pairs
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    HEIGHT = curses.LINES
    WIDTH = curses.COLS
    BASE_X = 0
    BASE_Y = 0
    global win_size
    win_size = {'HEIGHT' : HEIGHT,
                'WIDTH' : WIDTH,
                'BASE_X' : BASE_X,
                'BASE_Y' : BASE_Y,
                 # menu win dimentions
                'MENU_HEIGHT' : 10,
                'MENU_WIDTH' : (WIDTH / 4) - 2,
                'MENU_BASE_X' : BASE_X + 1,
                'MENU_BASE_Y' : BASE_Y + 4,
                # content win
                'CONTENT_HEIGHT' : HEIGHT-5,
                'CONTENT_WIDTH' : (WIDTH / 4) * 3,
                'CONTENT_BASE_X' : (WIDTH / 4) - 1 + BASE_X,
                'CONTENT_BASE_Y' : BASE_Y+4,
                # status win
                'STATUS': {'height' : 3,
                           'width': WIDTH - 2,
                           'start_y': BASE_Y + 1,
                           'start_x': BASE_X}
                'STATUS_HEIGHT' : 3,
                'STATUS_WIDTH' : WIDTH - 2,
                'STATUS_BASE_X' : BASE_X + 1,
                'STATUS_BASE_Y' : BASE_Y + 1}

    MyApp(stdscr)


if __name__ == '__main__':
    #main()
    #print 'LOL'
    curses.wrapper(main)
