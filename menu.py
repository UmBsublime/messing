#!/usr/bin/env python

import curses
from collections import deque



class Widget(object):
    '''
        params is dict with these keys (height, width, start_y, start_x)
        example:
        param = {'height': 10,
                 'width': 20,
                 'start_y': 0,
                 'start_x': 0}
    '''
    def __init__(self, parentWindow, params = None):

        if params == None:
            raise NotImplementedError

        self.win = parentWindow
        self.height = params['height'] - 2  # pour avoir la auteur - largeur de la box
        self.width = params['width'] -2     # pour avoir la largeyr - largeur de la box
        self.start_y = params['start_y']
        self.start_x = params['start_x']

        self.clear()
        self.update()

    def update(self):

        self.win.nooutrefresh()

    def clear(self):
        self.win.clear()
        self.win.box()








class Menu(object):

    def __init__(self, items, win, shownSize=8, params = None):

        #curses.curs_set(0)                   --> change $TERM to rxvt fixes this and hides cursor
        self.window = win.derwin(0, 0)
        self.window.keypad(1)

        self.position = 1
        self.items = items
        self.items.append(('exit', 'exit'))
        self.items = deque(items)
        self.shownSize= shownSize


    def _getItems(self, down=True):

        if len(self.items) < self.shownSize:
            self.menuSize = len(self.items)
        else:
            self.menuSize = len(self.items)

        #print ("DEBUG: shownSize = {}".format(self.shownSize))
        #print ('DEBUG menuSize: {}'.format(self.menuSize))
        item = list(self.items)[:self.shownSize]
        newList = []
        for e in item:
            #print ('DEBUG : value: {:<4}action: {:<8}'.format(e[0], e[1]))
            newList.append(e)

        return newList


    def display(self):


        while True:

            shownItems = self._getItems(self.items)
            self.window.clear()
            self.window.box()
            self.window.noutrefresh()
            for index, item in enumerate(shownItems):
                if index == self.position:
                    mode = curses.color_pair(1)+curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                msg = ' %s' % (item[0])

                self.window.addstr(1+index, 1, msg, mode)  # Scrolling menu set here

            key = self.window.getch()

            if key in [curses.KEY_ENTER, curses.KEY_RIGHT]:
                if shownItems[self.position][1] == 'exit':
                    break
                else:
                    try:
                        shownItems[self.position][1](shownItems[self.position][0])  # crazy shit going down
                    except:
                        shownItems[self.position][1]()
            if key == curses.KEY_LEFT:
                break
            elif key == curses.KEY_UP:
                self.items.rotate(-1)
            elif key == curses.KEY_DOWN:

                self.items.rotate(1)


class ContentWin(Widget):

    def __init__(self, win, params = None):

        self.win = win
        self.win.box()
        self.win.noutrefresh()

    def write(self, content):

        self.win.clear()
        self.win.box()
        self.win.addstr(1, 1, str(content))
        self.win.nooutrefresh()


class StatusWin(Widget):
    def __init__(self, win, params = None):

        Widget.__init__(self, win, params)

        self.max_string_length = curses.COLS - 4

    def write(self, content):
        self.win.addstr(1,1, ' '*self.max_string_length)
        if len(content) > self.max_string_length:
            content = content[:self.max_string_length]

        temp = ' ' * self.max_string_length
        temp = temp[:-len(content)]
        temp = temp[:(len(temp)/2)]
        temp = temp + content + temp

        mode  = curses.color_pair(2) #+curses.A_REVERSE

        self.win.attron(curses.color_pair(1))
        self.win.box()
        self.win.attroff(curses.color_pair(1))
        self.win.addstr(1,1, temp, mode)
        self.win.nooutrefresh()

class BaseWin(object):

    def __init__(self):
        self.HEIGHT = curses.LINES
        self.WIDTH = curses.COLS
        self.BASE_X = 0
        self.BASE_Y = 0

        # Color Pairs

        # WINDOW Declaration
        mainWin = curses.newwin(self.HEIGHT, self.WIDTH, self.BASE_Y, self.BASE_X)

        #PREP
        mainWin.box()
        mainWin.refresh()



if __name__ == '__main__':
    curses.wrapper(MyMenu)
