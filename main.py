#!/usr/bin/env python
import curses


from widget import content, status, menu, background

class MyApp():

    def __init__(self, stdscreen):

        global win_size

        # WINDOW Declaration
        background.Background() # --> required

        menuWin  = curses.newwin(win_size['MENU']['height'], win_size['MENU']['width'],
                                 win_size['MENU']['start_y'], win_size['MENU']['start_x'])

        contentWin  = curses.newwin(win_size['CONTENT']['height'], win_size['CONTENT']['width'],
                                    win_size['CONTENT']['start_y'], win_size['CONTENT']['start_x'])

        statusWin  = curses.newwin(win_size['STATUS']['height'], win_size['STATUS']['width'],
                                   win_size['STATUS']['start_y'], win_size['STATUS']['start_x'])

        self.contentWin = content.Content(contentWin, win_size['CONTENT'])
        self.statusWin = status.Status(statusWin, win_size['STATUS'])


        sub_action_items = [
                ('sub_action1', self.contentWin.write),
                ('sub_action2', self.contentWin.write),
                ('sub_action3', self.contentWin.write),
                ('sub_action4', self.contentWin.write),
                ('sub_action5', self.contentWin.write),
                ('sub_action6', self.contentWin.write),
                ('sub_action7', self.contentWin.write),
                ('sub_action8', self.contentWin.write),
                ]
        sub_action_menu = menu.Menu(menuWin, win_size['MENU'], sub_action_items)

        action_items = [
                ('action1', sub_action_menu.display),
                ('action2', sub_action_menu.display),
                ('action3', sub_action_menu.display),
                ('action4', sub_action_menu.display),
                ('action5', sub_action_menu.display),
                ('action6', sub_action_menu.display),
                ('action7', sub_action_menu.display),
                ('action8', sub_action_menu.display),
                ]
        action_menu = menu.Menu(menuWin, win_size['MENU'], action_items)

        option_items = [
                ('option1', self.contentWin.write),
                ('option2', self.contentWin.write),
                ('option3', self.contentWin.write),
                ('option4', self.contentWin.write),
                ('option5', self.contentWin.write),
                ('option6', self.contentWin.write),
                ('option7', self.contentWin.write),
                ('option8', self.contentWin.write),
                ]
        option_menu = menu.Menu(menuWin, win_size['MENU'], option_items)

        command_items = [
                ('command1', self.contentWin.write),
                ('command2', self.contentWin.write),
                ('command3', self.contentWin.write),
                ('command4', self.contentWin.write),
                ('command5', self.contentWin.write),
                ('command6', self.contentWin.write),
                ('command7', self.contentWin.write),
                ('command8', self.contentWin.write),
                ]
        command_menu = menu.Menu(menuWin, win_size['MENU'], command_items)

        submenu_items = [
                ('Actions', action_menu.display)
                ]
        submenu = menu.Menu(menuWin, win_size['MENU'], submenu_items)

        main_menu_items = [
                ('Actions', action_menu.display),
                ('Options', option_menu.display),
                ('Commands', command_menu.display),

                ('submenu', submenu.display)
                ]

        main_menu = menu.Menu(menuWin, win_size['MENU'], main_menu_items)
        '''
        MAIN
            Action
                sub_action
            Option
            Command
            submenu
                Action
                    sub_action
        '''
        self.contentWin.write('Hello welcome to this beta interface')
        self.statusWin.write('>DEMO<  cols: {} lines: {}'.format(curses.COLS, curses.LINES))
        main_menu.display()

class ScreenToSmall(Exception):
    def __init__(self):
        self.message = 'Screen has to be minimum of 24x80'


def main(stdscr):
    # Basic size check
    if curses.LINES <= 24:
        raise ScreenToSmall
    if curses.COLS <= 80:
        raise ScreenToSmall

    HEIGHT = curses.LINES
    WIDTH = curses.COLS
    BASE_X = 0
    BASE_Y = 0

    global win_size
    win_size = {'HEIGHT' : HEIGHT,
                'WIDTH' : WIDTH,
                'BASE_X' : BASE_X,
                'BASE_Y' : BASE_Y,

                 'MENU': {'height' : 10,
                          'width' : (WIDTH / 4) -2,
                          'start_y' : BASE_X + 4,
                          'start_x' : BASE_Y + 1,},

                'CONTENT': {'height' : HEIGHT-5,
                            'width' : (WIDTH / 4) * 3,
                            'start_x' : (WIDTH / 4) - 1 + BASE_X,
                            'start_y' : BASE_Y+4,},

                'STATUS': {'height' : 3,
                           'width': WIDTH - 2,
                           'start_y': BASE_Y + 1,
                           'start_x': BASE_X + 1}}

    # color pairs
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    MyApp(stdscr)


if __name__ == '__main__':

    curses.wrapper(main)
