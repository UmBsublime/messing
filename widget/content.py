from widget import Widget

class Content(Widget):

    def __init__(self, win, params = None):

        Widget.__init__(self, win, params)


    def write(self, content):
        self.clear()
        self.win.addstr(1, 1, str(content))
        self.update()

