import tkinter as tk
from tkinter import ttk

user_input = []

def add_to_list():
    print('running function')
    user_input.append(username_entry.get())
    print(user_input)
    login.destroy()

root = tk.Tk()
root.title('Demo')

login = tk.Tk()
login.title('Login')
login.attributes('-topmost',1)

login.columnconfigure(0, weight= 1)
login.columnconfigure(1, weight=3)

username_label = ttk.Label(login, text='username:')
username_label.grid(column=0, row=0)

username_entry = ttk.Entry(login)
username_entry.grid(column=1, row=0)

login_button = ttk.Button(login, text='login', command=add_to_list)
login_button.grid(column=1, row=3)


root.mainloop()