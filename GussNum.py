#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import Tkinter as tk 
import tkMessageBox

# 使用Tkinter前需要先导入 

# 第1步，实例化object，建立窗口window 
window = tk.Tk() 

# 第2步，给窗口的可视化起名字 
window.title('My Window') 
# 第3步，设定窗口的大小(长 * 宽) 
window.geometry('500x300') # 这里的乘是小x 

Theme_label = tk.Label(window, text='Guess Num Game', bg='red', fg='yellow',font=('Arial', 18))
Theme_label.pack()

# Please input a num
InputNote_label = tk.Label(window, text='Please input a num between 1 and 100', bg='red', fg='yellow',font=('Arial', 16))
InputNote_label.pack()

# Place a Entry
Num_entry = tk.Entry(window, show=None)
Num_entry.pack()


def Check_Num():
    var_str = Num_entry.get()
    var_num = int(var_str)
    if var_num == 37:
        tkMessageBox.showinfo(title='Guess Result',message="Your guss num is "+var_str+", You Win!!")
    elif var_num < 37:
        tkMessageBox.showinfo(title='Guess Result',message="Your guss num is "+var_str+", Litten than the goal num!!")
    else:
        tkMessageBox.showinfo(title='Guess Result',message="Your guss num is "+var_str+", Greater than the goal num!!")
        
# Place a button
Check_button = tk.Button(window, text='Guss', command=Check_Num)
Check_button.pack()


# 第8步，主窗口循环显示 
window.mainloop()
