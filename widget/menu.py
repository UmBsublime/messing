
import curses

from collections import deque

from widget import Widget

class Menu(Widget):

    def __init__(self, win, params = None, items = None):

        Widget.__init__(self, win, params)
        self.win = win
        self.items = deque(items)
        self.size = len(items)

        #--> change $TERM to rxvt fixes this and hides cursor
        #curses.curs_set(0)
        self.win = self.win.derwin(0, 0)
        self.win.keypad(1)

        self.position = 3
        self.offset = 1

        if self.size <= self.height:

            self.offset = ((self.height - self.size) / 2) + 1
            self.position = (self.size / 2) - 1

            if self.size <= 3:
                self.position = 1
            if self.size <= 2:
                self.position = 0

    def _getItems(self, down=True):

        item = list(self.items)[:self.height]
        new_list = []
        for e in item:
            new_list.append(e)

        return new_list

    def display(self):

        for i in range(self.position):
            self.items.rotate()

        while True:

            shown_item = self._getItems(self.items)
            self.clear()
            self.update()

            for index, item in enumerate(shown_item):
                msg = '{}'.format((item[0]))

                if index == self.position:
                    mode = curses.color_pair(1) + curses.A_REVERSE + curses.A_BOLD
                    msg = '->' + msg
                else:
                    mode = curses.A_NORMAL
                    msg = '  ' + msg

                # check if string is too long
                # strip if it is
                if len(msg) > self.width:
                    msg = msg[:-(len(msg)-self.width)]

                self.win.addstr(self.offset+index, 1, msg, mode)

            key = self.win.getch()
            if key in [curses.KEY_ENTER, curses.KEY_RIGHT]:
                # DO THE ACTION
                if shown_item[self.position][1] == 'exit':
                    break
                else:
                    # I will eventually remove this try except to just launch functions
                    # Only the except part will stay
                    try:
                        shown_item[self.position][1](shown_item[self.position][0])
                    except:
                        shown_item[self.position][1]()
            if key == curses.KEY_LEFT:
                # GO BACK
                break
            elif key == curses.KEY_UP:
                self.items.rotate()
            elif key == curses.KEY_DOWN:
                self.items.rotate(-1)
