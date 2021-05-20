from tkinter import *
from tkinter import messagebox

# Defines and creates the main window for the login program.
def main_menu():
    global main_window
    main_window = Tk()  # Creates the root window of this module.
    main_window.geometry("300x300")  # Window geometry
    main_window.title("User Authentication")  # Window Title
    main_window.configure(bg="dark grey")  # Configures the background(bg) color of the window
    label1 = Label(main_window, text="Choose an option", font=('arial', 9, 'bold'), bg="light gray",
                   fg="black")  # Creates a label with a text string.
    label1.pack(fill=X,
                pady=20)  # Using the pack method to place label instead of .grid, the fill widget tells the label to fill the space horizontally.
    # The pad widget tells the label how many pixels to pad vertically outside of the widgets borders.
    login_btn = Button(main_window, text="Login", font=('arial', 9, 'bold'), bg="light grey", fg="black", width="30", height="2",
                       command=login)  # Creates a button with a text string and a command to execute when pressed.
    login_btn.pack(pady=20)
    new_user_btn = Button(main_window, text="Register", font=('arial', 9, 'bold'), bg="light grey", fg="black",
                          width="30", height="2", command=new_user)
    new_user_btn.pack(pady=20)
    main_window.mainloop()  # loop for the main_window to keep it going continuously, otherwise it would execute the code and then just exit.


# Registration window for a new user.
def new_user():
    global username
    global password
    global username_entry
    global password_entry
    global new_user_window

    # Creates the Registration window with the main_window as its parent window.
    new_user_window = Toplevel(main_window)
    new_user_window.title("Register")
    new_user_window.geometry("300x300")

    # Creates username and password variables.
    username = StringVar()
    password = StringVar()
    label2 = Label(new_user_window, text="Fill in info below", bg="light gray", fg="black", font=('arial', 9, 'bold'))
    label2.pack(fill=X, pady=20)

    # Creates a Frame in the new_user_window.
    user_info_panel = Frame(new_user_window)
    user_info_panel.pack(pady=20)

    username_label = Label(user_info_panel, text="Username: ", font=('arial', 9, 'bold'))
    username_label.grid(row=0, column=0)
    username_entry = Entry(user_info_panel, textvariable=username)
    username_entry.grid(row=0, column=1)

    # Creates a label between the username_label and password_label with no string, only operates to create space between the two labels.
    Label(user_info_panel, text="").grid(row=1)

    password_label = Label(user_info_panel, text="Password: ", font=('arial', 9, 'bold'))
    password_label.grid(row=2, column=0)
    password_entry = Entry(user_info_panel, textvariable=password)
    password_entry.grid(row=2, column=1)

    # Button to call the register function.
    register_btn = Button(new_user_window, text="Register", font=('arial', 9, 'bold'), command=register)
    register_btn.pack()


# Registration function to verify if the user is already created, and to write it to a .txt file if it's not already created.
def register():
    registered = False
    # Sets the registered string to false.

    username_text = username.get()
    password_text = password.get()
    # Variables for .get operator.
    file = open("credentials.txt", "a")  # Sets the variable file to open("credentials.txt", "a"),
    # in order to not have to write the whole thing every time we want to open it.
    for line in open("credentials.txt", "r").readlines():
        login_info = line.split()
        if username_text == login_info[1]:
            registered = True
    # The .readlines() operator reads the lines of the credentials.txt file and compares(==) the username to the login_info variable.
    # if the username string (which is called from the username.get()) is equal to any textvariable in the credentials.txt,
    # the registered string becomes True, which means the username already exists.

    if registered:
        file.close()
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        # If the registered is True the file closes and the username and password entries are deleted.
        messagebox.showerror("Error", "User already Exists!")

    else:
        file.write("Username: " + username_text + " Password: " + password_text + "\n")
        file.close()
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        # If the registered remains False, the file will write the entries in the entry widgets to the credentials.txt file.

        messagebox.showinfo("Success!", "Press OK to Continue!")


# Function for the login window.
def login():
    global username_verify
    global username_verify_entry
    global password_verify
    global password_verify_entry
    global login_window

    login_window = Toplevel(main_window)
    login_window.geometry("300x300")
    login_window.title("Login")
    # Opens a window with the main_window as it's parent.
    label2 = Label(login_window, text="Enter Your Credentials", bg="light gray", fg="black", font=('arial', 9, 'bold'))
    label2.pack(fill=X, pady=20)

    credentials_panel = Frame(login_window)
    credentials_panel.pack(pady=20)

    username_verify = StringVar()
    password_verify = StringVar()

    username_label = Label(credentials_panel, text="Username: ", font=('arial', 9, 'bold'))
    username_label.grid(row=0, column=0)
    username_verify_entry = Entry(credentials_panel, textvariable=username_verify)
    username_verify_entry.grid(row=0, column=1)

    Label(credentials_panel, text="").grid(row=1)

    password_label = Label(credentials_panel, text="Password: ", font=('arial', 9, 'bold'))
    password_label.grid(row=2, column=0)
    password_verify_entry = Entry(credentials_panel, textvariable=password_verify, show="*")
    password_verify_entry.grid(row=2, column=1)

    login_btn = Button(login_window, text="Login", font=('arial', 9, 'bold'), command=login_verify)
    # Creates a button that when pressed, executes the command login_verify.
    login_btn.pack(pady=20)


# Function to verify login against the credentials.txt file.
def login_verify():
    global loginver
    user = username_verify.get()
    pswrd = password_verify.get()
    # Variables for .get operator

    loginver = False
    for line in open("credentials.txt", "r").readlines():
        login_info = line.split()
        if user == login_info[1] and pswrd == login_info[3]:
            loginver = True
    # Reads the lines in credentials.txt and if the user and pswrd variables matches the login_info then login = True.

    if loginver:
        # Executes code below if the login = True.
        btn1 = Button(login_window, text="Success, Click here to Continue", bg="green", fg="blue",
                      command=lambda: main_window.destroy())
        # Creates button that when pressed, destroys the main_window and thus starting the calculator app.
        btn1.pack(fill=X, pady=20)

    else:
        messagebox.showerror("Error", "User does not exist")


main_menu()
