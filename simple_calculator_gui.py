# Import modules
from tkinter import *
from tkinter import ttk

buffer = 0
first_number = 0
second_number = 0
running_total = 0
first_number_set = False


def update_number(inputs):
    # Update running total
    # Should be a global variable
    global buffer
    global first_number
    global second_number
    global running_total
    global first_number_set

    # Basic logic
    # Check if inputs is int or str
    if isinstance(inputs, str):
        # Do something
        pass
    else:
        running_total = inputs

    digit_display.config(text=str(inputs))


def clear_screen():
    # Clear the text label and reset the registry
    global buffer
    global first_number
    global second_number
    global running_total
    global first_number_set

    digit_display.config(text="0")
    buffer = 0
    first_number = 0
    second_number = 0
    running_total = 0
    first_number_set = False


def safely_exit():
    root.destroy()


# Create a window
root = Tk()
# Set the window size
root.geometry("300x300")
# Set window title
root.title("Simple Calculator")
# Make the window stay the same size
root.resizable(0, 0)
# Create a frame and anchor it to the center of the root window
main_frame = ttk.Frame(root, padding=5)
main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
# Calculator will be 5 columns by 5 rows
# Row 0 and Column 0 to 4 will be for the label that display digits
digit_display = Label(main_frame, text="0", font=("Arial", 18), bg='#CCCCCC', anchor="e", width=12, justify=RIGHT)
digit_display.grid(columnspan=5, row=0)
# Row 1 and Column 0 to 4 will be for 7, 8, 9, +/- and Sqrt
btn_7 = Button(main_frame, text="7", font=("Arial", 18), command=update_number(7))
btn_7.grid(column=0, row=1, sticky="nsew")

btn_8 = Button(main_frame, text="8", font=("Arial", 18), command=update_number(8))
btn_8.grid(column=1, row=1, sticky="nsew")

btn_9 = Button(main_frame, text="9", font=("Arial", 18), command=update_number(9))
btn_9.grid(column=2, row=1, sticky="nsew")

btn_plus_minus = Button(main_frame, text="±", font=("Arial", 18), command=update_number("plmn"))
btn_plus_minus.grid(column=3, row=1, sticky="nsew")

btn_sqrt = Button(main_frame, text="√", font=("Arial", 18), command=update_number("sqrt"))
btn_sqrt.grid(column=4, row=1, sticky="nsew")

# Row 2 and Column 0 to 4 will be for 4, 5, 6, x, and /
btn_4 = Button(main_frame, text="4", font=("Arial", 18), command=update_number(4))
btn_4.grid(column=0, row=2, sticky="nsew")

btn_5 = Button(main_frame, text="5", font=("Arial", 18), command=update_number(5))
btn_5.grid(column=1, row=2, sticky="nsew")

btn_6 = Button(main_frame, text="6", font=("Arial", 18), command=update_number(6))
btn_6.grid(column=2, row=2, sticky="nsew")

btn_mult = Button(main_frame, text="x", font=("Arial", 18), command=update_number("mult"))
btn_mult.grid(column=3, row=2, sticky="nsew")

btn_div = Button(main_frame, text="÷", font=("Arial", 18), command=update_number("div"))
btn_div.grid(column=4, row=2, sticky="nsew")

# Row 3 and Column 0 to 3 will be for 1, 2, 3, and -
btn_1 = Button(main_frame, text="1", font=("Arial", 18), command=update_number(1))
btn_1.grid(column=0, row=3, sticky="nsew")

btn_2 = Button(main_frame, text="2", font=("Arial", 18), command=update_number(2))
btn_2.grid(column=1, row=3, sticky="nsew")

btn_3 = Button(main_frame, text="3", font=("Arial", 18), command=update_number(3))
btn_3.grid(column=2, row=3, sticky="nsew")

btn_minus = Button(main_frame, text="-", font=("Arial", 18), command=update_number("minus"))
btn_minus.grid(column=3, row=3, sticky="nsew")

# Row 4 and Column 0 to 3 will be for C, 0, ., and +
btn_clear = Button(main_frame, text="C", font=("Arial", 18), bg="red", command=clear_screen)
btn_clear.grid(column=0, row=4, sticky="nsew")

btn_0 = Button(main_frame, text="0", font=("Arial", 18), command=update_number(0))
btn_0.grid(column=1, row=4, sticky="nsew")

btn_dot = Button(main_frame, text=".", font=("Arial", 18), command=update_number("dot"))
btn_dot.grid(column=2, row=4, sticky="nsew")

btn_plus = Button(main_frame, text="+", font=("Arial", 18), command=update_number("plus"))
btn_plus.grid(column=3, row=4, sticky="nsew")

# Row 3 + 4 and Column 4 will be for =
btn_equal = Button(main_frame, text="=", font=("Arial", 18), command=update_number("="))
btn_equal.grid(column=4, row=3, rowspan=2, sticky="nsew")

btn_exit = Button(main_frame, text="Exit", font=("Arial", 18), command=safely_exit)
btn_exit.grid(column=0, row=5, columnspan=5, sticky="nsew")

root.mainloop()
