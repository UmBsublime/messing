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


    def _print_menu(self, direction=''):
        '''
            dir can be  'u'p 'd'own 'l'eft 'r'ight
        '''
        if direction == 'u':
            self.menu.rotate(-1)
        elif direction == 'd':
            self.menu.rotate(1)
        elif direction == 'l':
            pass
        elif direction == 'r':
            pass

        print ('DEBUG choice: {}'.format(direction))


        if len(self.menu) < self.shown_size:
            self.menu_size = len(self.menu)
        else:
            self.menu_size = len(self.menu)

        print ("DEBUG shown_size: {}".format(self.shown_size))
        print ('DEBUG menu_size: {}'.format(self.menu_size))
        items = list(self.menu)[:self.shown_size]
        for e in items:
            print ('DEBUG : value: {:<4}action: {:<8}'.format(e[0], e[1]))




    def mainLoop(self, shown_size=4):

        self.shown_size = shown_size
        self._print_menu()
        os.system('clear')
        c='None'
        while True:

            print('\n{:^}\n'.format(self.name))
            print('Press ^C to move on')
            self._print_menu(c)
            c = raw_input('direction [u/d]: ')
            os.system('clear')



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
        t1.mainLoop()
    except KeyboardInterrupt:
        pass

    try:
        t2.mainLoop()
    except KeyboardInterrupt:
        pass

    try:
        t3.mainLoop(shown_size=6)
    except KeyboardInterrupt:
        print
        pass

if __name__ =='__main__':
    main()
