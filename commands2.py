#!/bin/bash
from tkinter import *
from subprocess import Popen, PIPE
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess
import os

count = 0

def main_windows():
    global main_window
    main_window = Tk()
    main_window.title("Confidential Guardian, Linux Automation Tool")
    main_window.geometry("1000x700")
    main_window.configure(bg="dark grey")
    label1 = Label(main_window, text="What Would you like to configure?", font=('arial', 12, 'bold'), bg="white",
                   fg="black")
    label1.pack(fill=X, pady=20)

    btnproc = Button(main_window, text="Process configuration", font=('arial', 9, 'bold'), bg="light grey", fg="black",
                     width="30", height="2", command=lambda: process_windows())
    btnproc.pack(pady=20)
    btnfw = Button(main_window, text="Firewall", font=('arial', 9, 'bold'), bg="light grey", fg="black", width="30",
                   height="2", command=firewall_windows)
    btnfw.pack(pady=20)
    btnmon = Button(main_window, text="AIDE", font=('arial', 9, 'bold'), bg="light grey", fg="black", width="30",
                    height="2", command=lambda: monitor_windows())
    btnmon.pack(pady=20)

    main_window.mainloop()


def process_windows():
    global process_window
    process_window = Toplevel()
    process_window.title("Confidential Guardian, Process Configuration")
    process_window.geometry("800x600")
    process_window.configure(bg="dark grey")
    label1 = Label(process_window, text="What Would you like to configure?", font=('arial', 12, 'bold'), bg="white",
                   fg="black")
    label1.pack(fill=X, pady=20)


def firewall_windows():
    global firewall_window
    global update_windows

    firewall_window = Toplevel()
    firewall_window.title("Confidential Guardian, Firewall Configuration")
    firewall_window.geometry("1000x600")
    firewall_window.configure(bg="dark grey")
    label1 = Label(firewall_window, text="What Would you like to configure?", font=('arial', 12, 'bold'), bg="white",
                   fg="black")
    label1.pack(fill=X, pady=8)

    updatebtn = Button(firewall_window, text="View Current Iptables layout", font=('arial', 9, 'bold'), bg="light grey",
                       fg="black", width="20",
                       height="1", command=showlayout)
    updatebtn.pack(pady=8)
    confbtn = Button(firewall_window, text="Edit iptables", font=('arial', 9, 'bold'), bg="light grey",
                     fg="black", width="20",
                     height="1", command=iptable_editor)
    confbtn.pack(pady=8)

    restorebtn = Button(firewall_window, text="Update iptables", font=('arial', 9, 'bold'), bg="light grey",
                        fg="black", width="20",
                        height="1", command=showlayout2)
    restorebtn.pack(pady=8)
    clearbtn = Button(firewall_window, text="Clear Layout", font=('arial', 9, 'bold'), bg="light grey",
                      fg="black", width="20",
                      height="1", command=clearlayout)
    clearbtn.pack(pady=8)


def monitor_windows():
    monitor_window = Toplevel(main_window)
    monitor_window.title("Confidential Guardian, AIDE Configuration")
    monitor_window.geometry("800x600")
    monitor_window.configure(bg="dark grey")
    label1 = Label(monitor_window, text="What Would you like to configure?", font=('arial', 12, 'bold'), bg="white",
                   fg="black")
    label1.pack(fill=X, pady=20)


def showlayout():
    global count
    global text
    text = Text(firewall_window, height=150, width=124)
    text.pack()
    if count > 0 and text.winfo_exists():
        text.pack_forget()
    count += 1
    with Popen(["iptables", '-L', '-v', '-n'], stdout=PIPE, stderr=PIPE) as p:
        for line in p.stdout:
            text.insert(END, line)


def clearlayout():
    text.pack_forget()


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    updateme.title(f"Text Editor Application - {filepath}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    updateme.title(f"Text Editor Application - {filepath}")


def iptable_editor():
    global txt_edit
    global updateme

    updateme = Toplevel(firewall_window)
    updateme.title("Iptables editor")
    updateme.rowconfigure(0, minsize=800, weight=1)
    updateme.columnconfigure(1, minsize=800, weight=1)

    txt_edit = Text(updateme)
    fr_buttons = Frame(updateme, relief=RAISED, bd=2)
    btn_open = Button(fr_buttons, text="Open", command=open_file)
    btn_save = Button(fr_buttons, text="Save As...", command=save_file)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)

    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")


def showlayout2():
    # subprocess.run(["iptables-restore", '<', '/home/kali/iptbl.rules'])
    os.system("iptables-restore < /home/kali/iptbl.rules")


main_windows()
