#!/usr/bin/env python

import os

from collections import deque





class Menu(object):

    def __init__(self, menu, name='generic'):
        self.name = name
        self.menu = deque(menu)


    def printMenu(self, down=True):
        print len(self.menu)
        if len(self.menu) < self.menuSize:
            menuSize = len(self.menu)
        print ("DEBUG: menuSize = {}".format(self.menuSize))

        items = list(self.menu)[:self.menuSize]
        for e in items:
            print ('DEBUG : value: {:<4}action: {:<8}'.format(e[0], e[1]))

        if down:
            self.menu.rotate(-1)
        else:
            self.menu.rotate(1)


    def showMenu(self, menuSize=4):
        ''' 
            Proof of concept of the looping menu
            Features:
                - Can manipulate any size menu
                - Works both directions 'duh'
                - Can show a variable portion of the menu default=4
        '''
        self.menuSize = menuSize
        down =True
        #self.printMenu(down=False)
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
    menu1 = [('1', 'menu'),
            ('2', 'cadabra'),
            ('3', 'man'),
            ('4', 'world'),
            ('5', 'lol'),
            ('6', 'debug'),
            ('7', 'blah')]

    menu2 = [('1', 'menu'),
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
        t3.showMenu(menuSize=6)
    except KeyboardInterrupt:
        pass

if __name__ =='__main__':
    main()
