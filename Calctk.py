from Loginapp import *

# Declaring an empty string variable for expression
expression = " "


# Defines the function for updating the expression variable.
def press(num):
    global expression
    expression = expression + str(num)
    entryf.set(expression)


# Defines a function to evaluate a string and return it as an integer,
# the returned integer is then showed as total in the entry field.
# It also creates or opens a logfile.txt and stores the total value in it.
def totalpress():
    try:
        global expression

        # Declaring eval(expression) variable
        total = eval(expression)
        # Setting entry field to eval result
        entryf.set(total)

        file = open("logfile.txt", "a")
        logfile = entryf.get()
        file.write(" = " + logfile + "\n")
        file.close()

        # Using except to handle potential errors

    except:
        entryf.set("Error")
        expression = " "


# Defines a function to set expression to an empty string and set the entry field to 0.
def ac():
    global expression
    expression = " "
    entryf.set("0")


# Defines a function to save the user input.
def save_input():
    logtext = entryf.get()
    file = open("logfile.txt", "a")
    file.write(logtext)
    file.close()


def save_input2():
    logtext = entryf.get()
    file = open("logfile2.txt", "a")
    file.write(logtext + "\n")
    file.close()


# Calculator program.
def calculator():
    global loginver
    global entryf

    # If statement that will only launch the calculator if login verification is true.
    if loginver:
        calc = Tk()
        calc.title("Highly advanced interstellar calculator")
        calc.geometry("440x220")
        # Sets the geometry of the gui window
        calc.configure(bg="light grey")
        entryf = StringVar()  # Variable for StringVar()
        expression_field = Entry(calc, textvariable=entryf, font=('arial', 14, 'bold'), width=40,
                                 justify=LEFT)  # Creates the entryfield for the calculator with fonts and other adjustments to appearance.

#################################### ROW 1 #######################################################
        expression_field.grid(row=1, columnspan=8, pady=10)  # Grid placement of Entryfield.
        expression_field.insert(0, "0")  # Sets the entryfield to nothing when the program starts.


#################################### ROW 2 #######################################################
        # Button creation with commands to call the press(num) function, also includes grid placement, pady and other appearance features.
        buttn1 = Button(calc, text=' 1 ', fg='black', bg='grey', command=lambda: press(1), height=2, width=7)
        buttn1.grid(row=2, column=0, pady=10)

        buttn2 = Button(calc, text=' 2 ', fg='black', bg='grey', command=lambda: press(2), height=2, width=7)
        buttn2.grid(row=2, column=1, pady=10)

        buttn3 = Button(calc, text=' 3 ', fg='black', bg='grey', command=lambda: press(3), height=2, width=7)
        buttn3.grid(row=2, column=2, pady=10)

        plus = Button(calc, text=' + ', fg='black', bg='grey', command=lambda: press(' + '), height=2, width=7)
        plus.grid(row=2, column=3, pady=10)

        buttn0 = Button(calc, text=' 0 ', fg='black', bg='grey', command=lambda: press(0), height=2, width=7)
        buttn0.grid(row=2, column=4, pady=10)

        clearbtn = Button(calc, text='AC', fg='black', bg='grey', command=ac, height=2, width=7)
        clearbtn.grid(row=2, column=5, pady=10)
        Exponent = Button(calc, text='x^n', fg='black', bg='grey', command=lambda: press(' ** '), height=2, width=7)
        Exponent.grid(row=2, column=6, pady=10)
#################################### ROW 3 #######################################################
        buttn4 = Button(calc, text=' 4 ', fg='black', bg='grey', command=lambda: press(4), height=2, width=7)
        buttn4.grid(row=3, column=0, pady=10)

        buttn5 = Button(calc, text=' 5 ', fg='black', bg='grey', command=lambda: press(5), height=2, width=7)
        buttn5.grid(row=3, column=1, pady=10)

        buttn6 = Button(calc, text=' 6 ', fg='black', bg='grey', command=lambda: press(6), height=2, width=7)
        buttn6.grid(row=3, column=2, pady=10)

        minus = Button(calc, text=' - ', fg='black', bg='grey', command=lambda: press(' - '), height=2, width=7)
        minus.grid(row=3, column=3, pady=10)

        divide = Button(calc, text=' / ', fg='black', bg='grey', command=lambda: press(' / '), height=2, width=7)
        divide.grid(row=3, column=4, pady=10)

        Decimal = Button(calc, text='.', fg='black', bg='grey', command=lambda: press('.'), height=2, width=7)
        Decimal.grid(row=3, column=5, pady=10)

        Parantheses2 = Button(calc, text="(", fg="black", bg="grey", height=2, width=7, command=lambda: press(" ( "))
        Parantheses2.grid(row=3, column=6, pady=10)
#################################### ROW 4 #######################################################
        buttn7 = Button(calc, text=' 7 ', fg='black', bg='grey', command=lambda: press(7), height=2, width=7)
        buttn7.grid(row=4, column=0, pady=10)

        buttn8 = Button(calc, text=' 8 ', fg='black', bg='grey', command=lambda: press(8), height=2, width=7)
        buttn8.grid(row=4, column=1, pady=10)

        buttn9 = Button(calc, text=' 9 ', fg='black', bg='grey', command=lambda: press(9), height=2, width=7)
        buttn9.grid(row=4, column=2, pady=10)

        multiply = Button(calc, text=' * ', fg='black', bg='grey', command=lambda: press(' *'), height=2, width=7)
        multiply.grid(row=4, column=3, pady=10)

        equal = Button(calc, text=' = ', fg='black', bg='grey',
                       command=lambda: [save_input2(), save_input(), totalpress()], height=2,
                       width=7)
        equal.grid(row=4, column=4, pady=10)

        Sq_root = Button(calc, text="√x", fg='black', bg='grey', command=lambda: [press(' ** '), press(0.5)], height=2,
                         width=7)
        Sq_root.grid(row=4, column=5, pady=10)

        Parantheses1 = Button(calc, text=")", fg="black", bg="grey", height=2, width=7, command=lambda: press(" ) "))
        Parantheses1.grid(row=4, column=6, pady=10)

        calc.mainloop()

    else:
        messagebox.showerror('Could not Verify user', 'Press OK to quit')


calculator()
