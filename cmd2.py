import tkinter as tk

track_clicks = 0


def click():
    global track_clicks
    if track_clicks > 0 and l1.winfo_exists():
        l1.destroy()  # destroys the label
    track_clicks += 1


root = tk.Tk()

l1 = tk.Label(root, text="DON'T TRADE")
l1.pack()
b1 = tk.Button(root, text='Click :)', command=click)
b1.pack()

root.mainloop()
