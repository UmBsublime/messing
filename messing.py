#!/usr/bin/env python

import os

from collections import deque

class Menu(object):
    '''
    Proof of concept of a looping menu, just testing for some
    widget I want to make in curses
    Features:
        - Can manipulate any size menu
        - Works both directions 'duh'
        - Can show a variable portion of the menu default=4
    '''

    def __init__(self, menu, name='generic'):

        self.name = name
        self.menu = deque(menu)


    def printMenu(self, down=True):

        if len(self.menu) < self.shownSize:
            self.menuSize = len(self.menu)
        else:
            self.menuSize = len(self.menu)

        print ("DEBUG: shownSize = {}".format(self.shownSize))
        print ('DEBUG menuSize: {}'.format(self.menuSize))
        items = list(self.menu)[:self.shownSize]
        for e in items:
            print ('DEBUG : value: {:<4}action: {:<8}'.format(e[0], e[1]))

        if down:
            self.menu.rotate(-1)
        else:
            self.menu.rotate(1)


    def showMenu(self, shownSize=4):

        self.shownSize = shownSize
        down =True
        while True:
            os.system('clear')
            print('\n{:^}\n'.format(self.name))
            print('Press ^C to move on')
            self.printMenu(down=down)
            c = raw_input('direction [u/d]: ')
            if str(c) == 'd':
                down = True
            else:
                down = False


def main():
    menu1 = [('1', 'abra'),
             ('2', 'cadabra'),
             ('3', 'hello'),
             ('4', 'world'),
             ('5', 'lol'),
             ('6', 'debug'),
             ('7', 'blah')]

    menu2 = [('1', 'abra'),
             ('2', 'cadabra')]
    t1 = Menu(menu1, name = '7 items in list 4 shown')
    t2 = Menu(menu2, name = 'Test small list default')
    t3 = Menu(menu1, name = 'test show 6 elements')


    try:
        t1.showMenu()
    except KeyboardInterrupt:
        pass

    try:
        t2.showMenu()
    except KeyboardInterrupt:
        pass

    try:
        t3.showMenu(shownSize=6)
    except KeyboardInterrupt:
        print
        pass

if __name__ =='__main__':
    main()
