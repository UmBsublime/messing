class Widget(object):
    '''
        params is a dict with these keys (height, width, start_y, start_x)
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
        self.width = params['width'] -2     # pour avoir la largeur - largeur de la box
        self.start_y = params['start_y']
        self.start_x = params['start_x']

        self.clear()
        self.update()

    def update(self):
        self.win.nooutrefresh()

    def clear(self):
        self.win.clear()
        self.win.box()