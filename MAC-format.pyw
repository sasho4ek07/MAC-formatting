#!/usr/bin/python
# coding=utf-8
import tkinter as tk
import re


def window_deleted():
    # print("Окно закрыто")
    root.quit()


def paste_of_buffer():
    # c = tk.Tk()
    # c.withdraw()
    try:
        cb = root.clipboard_get()
        # print(cb)
        # c.update()
    except tk.TclError:
        cb = ''
    # return cb
    insert_MAC.config(state='normal')
    insert_MAC.delete(0, tk.END)
    insert_MAC.insert(0, cb)


def copy_in_buffer_mac1():
    # cb = tk.Tk()
    # cb.withdraw()
    # cb.clipboard_clear()
    text = MAC1.get()
    root.clipboard_clear()
    root.clipboard_append(text)
    # cb.update()
    # cb.destroy()


def copy_in_buffer_mac2():
    # cb = tk.Tk()
    # cb.withdraw()
    # cb.clipboard_clear()
    text = MAC2.get()
    root.clipboard_clear()
    root.clipboard_append(text)


def format_mac():
    MACs = []
    MAC = insert_MAC.get().strip().upper().replace(' ', '')  # получаем строку без пробелов и верхнем регистре
    # print(len(MAC))
    if len(MAC) == 17:
        MACs = re.split(r'[:;,.-]+', MAC)
        # print(MACs)
        message("Ok!")
    elif len(MAC) == 12:
        MACs = [MAC[i:i + 2] for i in range(0, len(MAC), 2)]
        # print(MACs)
        message("Ok!")
    else:
        # print('ERROR!')
        message("ERROR\n Format is not correct!", True)

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
root.iconbitmap(default='mac.ico')
root.geometry('255x235+550+250')  # ширина=500, высота=400, x=250, y=200
root.protocol('WM_DELETE_WINDOW', window_deleted)  # обработчик закрытия окна
# root.rowconfigure(0, height=1)
root.resizable(False, False)

head = tk.Label(root, text="Insert the MAC address:", font='Arial 15')

insert_MAC = tk.Entry(root,
                      width=16,
                      font='Arial 14')  # окно ввода мак-адреса
insert_MAC.focus_set()

button_paste = tk.Button(root, text="Paste",
                         width=7,
                         # height=1,
                         fg='black',
                         font='arial 13',
                         command=paste_of_buffer)

button_format = tk.Button(root, text='Format MAC',
                          width=15,
                          # height=1,
                          fg='green',
                          font='arial 14',
                          command=format_mac)

MAC1 = tk.Entry(root, width=16,
                font='Arial 15', state='readonly')

MAC2 = tk.Entry(root, width=16,
                font='Arial 15', state='readonly')

mac1_copy = tk.Button(root, text="Copy",
                      width=7, height=1,
                      fg='black',
                      font='arial 13',
                      command=copy_in_buffer_mac1)

mac2_copy = tk.Button(root, text="Copy",
                      width=7, height=1,
                      fg='black',
                      font='arial 13',
                      command=copy_in_buffer_mac2)

info = tk.Label(root, font='Arial 13', fg='green', text="ИНФО")
info.config(text="")
button_exit = tk.Button(root, text='Exit',
                        width=7,
                        height=3,
                        fg='black',
                        font='arial 13',
                        command=window_deleted)
# root.columnconfigure(1, pad=8)
# root.rowconfigure(5, pad=5)
head.grid(row=0, column=0, columnspan=3)
insert_MAC.grid(row=1, column=0, sticky="w")
button_paste.grid(row=1, column=1, sticky="w")
button_format.grid(row=2, column=0, columnspan=2)
MAC1.grid(row=3, column=0, sticky="w")
MAC2.grid(row=4, column=0, sticky="w")
mac1_copy.grid(row=3, column=1, sticky="w")
mac2_copy.grid(row=4, column=1, sticky="w")
info.grid(row=5, column=0, columnspan=2, sticky="w")
button_exit.grid(row=5, column=1, sticky="w")
root.mainloop()
