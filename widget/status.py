import curses

from widget import Widget

class Status(Widget):
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

        self.win.attron(curses.color_pair(1)+curses.A_BOLD)
        self.win.box()
        self.win.attroff(curses.color_pair(1))

        mode  = curses.color_pair(2) + curses.A_BOLD
        self.win.addstr(1,1, temp, mode)
        self.win.nooutrefresh()