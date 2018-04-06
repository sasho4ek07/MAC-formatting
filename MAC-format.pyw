#!/usr/bin/python
# coding=utf-8
import tkinter as tk
import re

# MAC = ""
# MACs = []

# TODO sdsfsdfa


def window_deleted():
    print("Окно закрыто")
    root.quit()


def format_mac():
    MACs = []
    MAC = insert_MAC.get().strip().upper()
    # print(len(MAC))
    # TODO Добавить проверку на превышение длинны 12
    # TODO Убирать пробельные символы
    if len(MAC) > 17 or len(MAC) < 12:
        # print('ERROR!')
        message("ERROR\n Format is not correct!", True)
    elif len(MAC) == 17:
        MACs = re.split(r'[:;,.-]+', MAC)
        # print(MACs)
        message("Ok!")
    else:
        MACs = [MAC[i:i + 2] for i in range(0, len(MAC), 2)]
        # print(MACs)
        message("Ok!")
    MAC1.config(state='normal')
    MAC1.delete(0, tk.END)
    MAC1.insert(0, '-'.join(MACs))
    MAC1.config(state='readonly')

    MAC2.config(state='normal')
    MAC2.delete(0, tk.END)
    MAC2.insert(0, ':'.join(MACs))
    MAC2.config(state='readonly')


def message(text='', error=False):
    info.config(text=text)
    if error is True:
        info.config(fg='red')
    else:
        info.config(fg='green')


root = tk.Tk()
root.title(u'MAC-Format')
root.geometry('250x200+500+300')  # ширина=500, высота=400, x=300, y=200
root.protocol('WM_DELETE_WINDOW', window_deleted)  # обработчик закрытия окна
root.resizable(False, False)
head = tk.Label(root, text="Insert the MAC address:", font='Arial 15')
head.pack()
insert_MAC = tk.Entry(root, width=16, font='Arial 14')
insert_MAC.focus_set()
insert_MAC.pack()
button_format = tk.Button(root, text='Format MAC', width=10, height=1, fg='green', font='arial 14', command=format_mac)
button_format.pack()
MAC1 = tk.Entry(root, width=16, font='Arial 15', state='readonly')
MAC2 = tk.Entry(root, width=16, font='Arial 15', state='readonly')
MAC1.pack()
MAC2.pack()
info = tk.Label(root, font='Arial 15', fg='green')
info.pack()
root.mainloop()
