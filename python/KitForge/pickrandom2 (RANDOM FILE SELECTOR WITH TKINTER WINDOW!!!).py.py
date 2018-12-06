# -*- coding: utf-8 -*-
import os
import random
from tkinter import *
from tkinter import ttk
root = Tk()
path = os.getcwd()
lst = os.listdir(path)
text = StringVar()
text.set('I choose nothing. Yet...')


def PickRandom(lst):
    pick = random.choice(lst)
    text.set('I choose this:\n' + pick)
    print(pick)
    return pick


def Delete():  
    t = text.get().split('\n')[1]
    if os.path.isfile(t):
        os.remove(t)
    else:
        try:
            os.removedirs(t)
        except OSError as e:
            l = os.listdir(t)
            print('l: ', l)
            for i in l:
                print('i: %s\\%s - is file: %s; is dir: %s' %
                      (t, i, os.path.isfile('%s\\%s' % (t, i)), os.path.isdir('%s\\%s' % (t, i))))
                if os.path.isfile(t + '\\' + i):
                    os.remove(t.encode('utf-8') + b'\\' + i.encode('utf-8'))
                elif os.path.isdir(t + '\\' + i):
                    os.removedirs(
                        t.encode('utf-8') + b'\\' + i.encode('utf-8'))
        finally:
            os.rmdir(t.encode('utf-8'))


def WriteAnswer(pick):
    f = open('pickrandom - %s.txt' % PickRandom(lst), 'wb')
    try:
        f.write(b'I choose this: ' + pick.encode('utf-8'))
    finally:
        f.close()


def Navigate():
    t = text.get().split('\n')[1]
    # For some reason encod into utf-8 doesn't allow explorer to navigate:
    # e = os.path.abspath(t.encode('utf-8'))
    os.system(r'start explorer "%s"' % os.path.abspath(t))


f = ttk.Frame(root).pack()
Label(f, textvariable=text).pack()
brickroll = ttk.Button(f, text='Roll!', underline=0)
brickroll.bind('<1>', lambda e: PickRandom(lst))
brickroll.bind('<space>', lambda e: PickRandom(lst), add='+')
brickroll.pack()
ttk.Button(f, text='Open it!', underline=2, command=Navigate).pack()
ttk.Button(f, text='Delete it!', command=Delete).pack()
# ttk.Button(f, text='Exit', command=root.destroy).pack()
root.bind('<Escape>', lambda e: root.destroy())
root.bind('<Key-r>', lambda e: PickRandom(lst), add='+')
root.bind('<Key-e>', lambda e: Navigate(), add='+')
root.title('PickRandom')
root.minsize(200, 32)
root.mainloop()