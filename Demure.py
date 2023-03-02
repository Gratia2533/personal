# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
import tkinter.ttk as ttk
import os

window = tk.Tk()
window.title('Demure')
window.geometry("300x100")
window.resizable(0,0)
window.configure(bg="#140500")
window.iconbitmap("D:/Program/workplace_py/Demure.ico")
info=tk.Label(window, text='©kukumant0u',bg="#140500"
              ,fg='#5C5C5C', font=("Arial",8))
info.place(relx=0.005,rely=0.8,relheight=0.2)

time=('取消關機','15min','30min','45min','60min','90min','120min','150min','180min')
combobox = ttk.Combobox(window, value = time, state = "readonly")
combobox.pack(side='top',expand=1)

def checkact():
    option =  combobox.get()
    if option == '取消關機':
        cmd = "shutdown -a"#取消
        os.system(cmd)
    elif option == '15min':
        cmd = "shutdown -s -t 900"#15
        os.system(cmd)
    elif option == '30min':
        cmd = "shutdown -s -t 1800"#30
        os.system(cmd)
    elif option == '45min':
        cmd = "shutdown -s -t 2700"#45
        os.system(cmd)
    elif option == '60min':
        cmd = "shutdown -s -t 3600"#60
        os.system(cmd)
    elif option == '90min':
        cmd = "shutdown -s -t 5400"#90
        os.system(cmd)
    elif option == '120min':
        cmd = "shutdown -s -t 7200"#120
        os.system(cmd)
    elif option == '150min':
        cmd = "shutdown -s -t 9000"#150
        os.system(cmd)
    elif option == '180min':
        cmd = "shutdown -s -t 10800"#180
        os.system(cmd)


confirm_button=tk.Button(window, text="Confirm" ,command=checkact
                         , bd=0.5 ,bg="#FFFFFF"
                         , activebackground="#FFAE00")
confirm_button.pack(side='bottom',expand=1)

#cmd命令列部分

window.mainloop()