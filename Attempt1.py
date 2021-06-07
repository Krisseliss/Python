#!/bin/bash
import os
import signal
from subprocess import Popen, PIPE
from tkinter import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

global main_window


def main_windows():
    main_window = Tk()
    main_window.title("Confidential Guardian, Linux Automation Tool")
    main_window.geometry("1000x700")
    main_window.configure(bg="dark grey")
    label1 = Label(main_window, text="What Would you like to configure?", font=('arial', 12, 'bold'), bg="white",
                   fg="black")
    label1.pack(fill=X, pady=20)

    btnproc = Button(main_window, text="Process configuration", font=('arial', 9, 'bold'), bg="light grey", fg="black",
                     width="30", height="2", command=process_windows)
    btnproc.pack(pady=20)
    btnfw = Button(main_window, text="Firewall", font=('arial', 9, 'bold'), bg="light grey", fg="black", width="30",
                   height="2", command=firewall_windows)
    btnfw.pack(pady=20)
    btnmon = Button(main_window, text="System Monitoring", font=('arial', 9, 'bold'), bg="light grey", fg="black",
                    width="30",
                    height="2", command=monitor_windows)
    btnmon.pack(pady=20)
    networkbtn = Button(main_window, text="Network Monitoring", font=('arial', 9, 'bold'), bg="light grey", fg="black",
                        width="30",
                        height="2", command=netwindows)
    networkbtn.pack(pady=20)

    main_window.mainloop()


def process_windows():
    global en1
    global process_window
    process_window = Toplevel()
    process_window.title("Confidential Guardian, Process Configuration")
    process_window.geometry("1000x600")
    process_window.configure(bg="dark grey")
    label1 = Label(process_window, text="Specify a Process", font=('arial', 12, 'bold'), bg="white",
                   fg="black")
    label1.pack(pady=20)
    en1 = StringVar()
    e1 = Entry(process_window, textvariable=en1, font=('arial', 14, 'bold'))
    e1.pack(pady=20)
    e1.insert(END, ' ')
    killbtn = Button(process_window, text="Kill process", font=('arial', 9, 'bold'), bg="light grey",
                     fg="black", width="20",
                     height="1", command=killprocess)
    killbtn.pack(pady=8)
    findbtn = Button(process_window, text="Search for process", font=('arial', 9, 'bold'), bg="light grey",
                     fg="black", width="20",
                     height="1", command=searchfunc)
    findbtn.pack(pady=8)
    clearps = Button(process_window, text="clear text", font=('arial', 9, 'bold'), bg="light grey",
                     fg="black", width="20",
                     height="1", command=clearlayoutps)
    clearps.pack(pady=8)


def clearlayoutps():
    texts.pack_forget()


def killprocess():
    procs = en1.get()
    for line in os.popen("ps ax | grep " + procs + " | grep -v grep"):
        fields = line.split()
        pid = fields[0]
        os.kill(int(pid), signal.SIGKILL)


def searchfunc():
    global texts
    search = en1.get()
    texts = Text(process_window, height=150, width=300)
    texts.pack()
    p = Popen(['ps', 'aux'], stdout=PIPE, stderr=PIPE)
    o = Popen(['grep', search], stdin=p.stdout, stdout=PIPE, stderr=PIPE)
    for line in o.stdout:
        texts.insert(END, line)


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

    viewbtn = Button(firewall_window, text="View Current Iptables layout", font=('arial', 9, 'bold'), bg="light grey",
                     fg="black", width="20",
                     height="1", command=showlayout)
    viewbtn.pack(pady=8)
    confbtn = Button(firewall_window, text="Edit iptables", font=('arial', 9, 'bold'), bg="light grey",
                     fg="black", width="20",
                     height="1", command=iptable_editor)
    confbtn.pack(pady=8)

    updatebtn = Button(firewall_window, text="Update iptables", font=('arial', 9, 'bold'), bg="light grey",
                       fg="black", width="20",
                       height="1", command=showlayout2)
    updatebtn.pack(pady=8)
    clearbtn = Button(firewall_window, text="Clear Layout", font=('arial', 9, 'bold'), bg="light grey",
                      fg="black", width="20",
                      height="1", command=clearlayout)
    clearbtn.pack(pady=8)


def showlayout():
    global text
    text = Text(firewall_window, height=150, width=124)
    text.pack()
    with Popen(["iptables", '-L', '-v', '-n'], stdout=PIPE, stderr=PIPE) as p:
        for line in p.stdout:
            text.insert(END, line)


def clearlayout():
    text.pack_forget()


def showlayout2():
    os.system("iptables-restore < /home/stevejablonsky/iptbl.rules")


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


def monitor_windows():
    global en2
    global monitor_window
    monitor_window = Toplevel()
    monitor_window.title("Confidential Guardian, System Monitoring")
    monitor_window.geometry("800x600")
    monitor_window.configure(bg="dark grey")
    en2 = StringVar()
    label1 = Label(monitor_window, text="What Would you like to configure?", font=('arial', 12, 'bold'), bg="white",
                   fg="black")
    label1.pack(fill=X, pady=8)
    e2 = Entry(monitor_window, textvariable=en2, font=('arial', 14, 'bold'))
    e2.pack(pady=8)
    e2.insert(END, ' ')
    lsofbtn = Button(monitor_window, text="Search For Open Files", font=('arial', 9, 'bold'), bg="light grey",
                     fg="black", width="20",
                     height="1", command=monitor_srch)
    lsofbtn.pack(pady=8)
    clearlsof = Button(monitor_window, text="Clear Lsof", font=('arial', 9, 'bold'), bg="light grey",
                       fg="black", width="20",
                       height="1", command=clearlsoftxt)
    clearlsof.pack(pady=8)
    logcheckbtn = Button(monitor_window, text="Open Logs", font=('arial', 9, 'bold'), bg="light grey",
                         fg="black", width="20",
                         height="1", command=logcheckout)
    logcheckbtn.pack(pady=8)


def logcheckout():
    lsof2 = Text(monitor_window, height=150, width=124)
    lsof2.pack()
    with Popen(['sudo', '-u', 'logcheck', 'logcheck', '-o', 'LOG'], stdout=PIPE, stderr=PIPE) as h:
        for line in h.stdout:
            lsof2.insert(END, line)


def monitor_srch():
    global lsof1
    lsofsearch = en2.get()
    lsof1 = Text(monitor_window)
    lsof1.pack(expand=True, fill="both")
    x = Popen(['lsof'], stdout=PIPE, stderr=PIPE)
    y = Popen(['grep', lsofsearch], stdin=x.stdout, stdout=PIPE, stderr=PIPE)
    for line in y.stdout:
        lsof1.insert(END, line)


def clearlsoftxt():
    lsof1.pack_forget()


def netwindows():
    global netwindow
    netwindow = Toplevel()
    netwindow.title("Confidential Guardian, Network Monitoring")
    netwindow.geometry("800x600")
    netwindow.configure(bg="dark grey")
    label1 = Label(netwindow, text="What Would you like to view?", font=('arial', 12, 'bold'), bg="white",
                   fg="black")
    label1.pack(fill=X, pady=8)

    tcpdumpbtn = Button(netwindow, text="TCPDUMP", font=('arial', 9, 'bold'), bg="light grey",
                        fg="black", width="20",
                        height="1", command=tcpdumpfunction)
    tcpdumpbtn.pack(pady=8)
    nettrigg = Button(netwindow, text="Monitor Netstat", font=('arial', 9, 'bold'), bg="light grey",
                      fg="black", width="20",
                      height="1", command=netstatmon)
    nettrigg.pack(pady=8)
    cleartxt = Button(netwindow, text="Clear", font=('arial', 9, 'bold'), bg="light grey",
                      fg="black", width="20",
                      height="1", command=clearlsoftxt1)
    cleartxt.pack(pady=8)


def clearlsoftxt1():
    netstat1.pack_forget()


def netstatmon():
    global netstat1
    netstat1 = Text(netwindow)
    netstat1.pack(expand=True, fill="both")
    with Popen(['netstat', '-l', '-p'], stdout=PIPE, stderr=PIPE) as p:
        for line in p.stdout:
            netstat1.insert(END, line)


# Does not work, can be configured to print the output in realtime to the IDE console, but not in the GUI#
def tcpdumpfunction():
    dump = Text(netwindow)
    dump.pack(expand=True, fill="both")
    x = Popen(['tcpdump', '-l', '>', 'dat', '&', 'tail', '-f', 'dat'], stdout=PIPE, stderr=PIPE, shell=TRUE,
              universal_newlines=TRUE)
    for line in x.stdout:
        dump.insert(END, line)


main_windows()
