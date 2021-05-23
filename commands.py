from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import Pmw


def save_file():
    global save_file
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],)
    file = open(filepath, "w")
    text = txt_edit.get(END)
    file.write(text)


filename = "/home/kali/PycharmProjects/UnixPySP@/iptblU.txt"
root = Tk()
root.title("Update Iptables")
top = Frame(root)
top.pack(side='top')
iptedit = Pmw.ScrolledText(top,
                           borderframe=5,
                           vscrollmode='dynamic',
                           hscrollmode='dynamic',
                           labelpos='n',
                           label_text='file %s' % filename,
                           text_width=90,
                           text_height=30,
                           text_wrap='none',
                           )
iptedit.pack()
txt_edit = Text(top)
txt_edit.insert('end', open(filename, 'r').read())
btn_save = Button(text="Save As", command=save_file)
btn_save.pack()
root.mainloop()

