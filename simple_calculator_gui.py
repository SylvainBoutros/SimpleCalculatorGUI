# Import modules
from tkinter import *
from tkinter import ttk
import math
from decimal import Decimal

buffer = 0
first_operand = 0
second_operand = 0
running_total = 0
first_operand_set = False
arithmetic_symbol_set = False
digits_display_str = ""
dot_set = False

def set_arithmetic(ari):
    pass

def get_results():
    pass

def update_number(inputs):
    pass

def is_float(digits_label):
    try:
        float(digits_label)
        return True
    except ValueError:
        return False

# Define a function that performs unary operations on the current operand
def set_unary_op(op):
    # Access the global variable for the digit display
    global digits_display_str

    # Convert the digit display string to a Decimal object
    current_operand = Decimal(digits_display_str)

    # If the operation is square root, take the square root of the current operand
    if op == "sqrt":
        current_operand = current_operand.sqrt()
    # If the op is negation, negate the current operand using the - op
    else:
        current_operand = -current_operand

    # Round the current operand to 9 decimal places and convert it back to a string
    # Only round if the length of the current operand string is greater than 9
    digits_display_str = str(current_operand.quantize(Decimal('1.000000000'))) if len(str(current_operand)) > 9 else str(current_operand)
    
    # Update the digit display with the new value of the digit display string
    digit_display.config(text=digits_display_str)

def update_digit_display(num):
    global digits_display_str, dot_set

    # If num is not a decimal point and there isn't already a decimal point in digits_display_str, append num to it
    if num != "dot" and "." not in digits_display_str:
        digits_display_str += num
    # If num is a decimal point and there isn't already a decimal point in digits_display_str, append it to the string and set dot_set to True
    elif num == "dot" and "." not in digits_display_str:
        digits_display_str += "."
        dot_set = True
    # If num is not a decimal point and there is already a decimal point in digits_display_str, append num to it
    elif num != "dot" and "." in digits_display_str:
        digits_display_str += num
    # If num is a decimal point and there is already a decimal point in digits_display_str, do nothing
    else:
        pass

    # If digits_display_str is longer than 9 characters, format it to scientific notation with 9 significant figures
    if len(digits_display_str) > 9:
        digits_display_str = "{:.9g}".format(float(digits_display_str))

    digit_display.config(text=digits_display_str)



def clear_screen():
    # Clear the text label and reset the registry
    global buffer
    global first_operand
    global second_operand
    global running_total
    global first_operand_set
    global arithmetic_symbol_set
    global digits_display_str
    global dot_set
 
    buffer = 0
    first_operand = 0
    second_operand = 0
    running_total = 0
    first_operand_set = False
    arithmetic_symbol_set = False
    digits_display_str = ""
    dot_set = False

    digit_display.config(text="0")


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
btn_7 = Button(main_frame, text="7", font=("Arial", 18), command=lambda: update_digit_display("7"))
btn_7.grid(column=0, row=1, sticky="nsew")

btn_8 = Button(main_frame, text="8", font=("Arial", 18), command=lambda: update_digit_display("8"))
btn_8.grid(column=1, row=1, sticky="nsew")

btn_9 = Button(main_frame, text="9", font=("Arial", 18), command=lambda: update_digit_display("9"))
btn_9.grid(column=2, row=1, sticky="nsew")

btn_plus_minus = Button(main_frame, text="±", font=("Arial", 18), command=lambda: set_unary_op(-1))
btn_plus_minus.grid(column=3, row=1, sticky="nsew")

btn_sqrt = Button(main_frame, text="√", font=("Arial", 18), command=lambda: set_unary_op("sqrt"))
btn_sqrt.grid(column=4, row=1, sticky="nsew")

# Row 2 and Column 0 to 4 will be for 4, 5, 6, x, and /
btn_4 = Button(main_frame, text="4", font=("Arial", 18), command=lambda: update_digit_display("4"))
btn_4.grid(column=0, row=2, sticky="nsew")

btn_5 = Button(main_frame, text="5", font=("Arial", 18), command=lambda: update_digit_display("5"))
btn_5.grid(column=1, row=2, sticky="nsew")

btn_6 = Button(main_frame, text="6", font=("Arial", 18), command=lambda: update_digit_display("6"))
btn_6.grid(column=2, row=2, sticky="nsew")

btn_mult = Button(main_frame, text="x", font=("Arial", 18), command=lambda: set_arithmetic("mult"))
btn_mult.grid(column=3, row=2, sticky="nsew")

btn_div = Button(main_frame, text="÷", font=("Arial", 18), command=lambda: set_arithmetic("div"))
btn_div.grid(column=4, row=2, sticky="nsew")

# Row 3 and Column 0 to 3 will be for 1, 2, 3, and -
btn_1 = Button(main_frame, text="1", font=("Arial", 18), command=lambda: update_digit_display("1"))
btn_1.grid(column=0, row=3, sticky="nsew")

btn_2 = Button(main_frame, text="2", font=("Arial", 18), command=lambda: update_digit_display("2"))
btn_2.grid(column=1, row=3, sticky="nsew")

btn_3 = Button(main_frame, text="3", font=("Arial", 18), command=lambda: update_digit_display("3"))
btn_3.grid(column=2, row=3, sticky="nsew")

btn_minus = Button(main_frame, text="-", font=("Arial", 18), command=lambda: set_arithmetic("minus"))
btn_minus.grid(column=3, row=3, sticky="nsew")

# Row 4 and Column 0 to 3 will be for C, 0, ., and +
btn_clear = Button(main_frame, text="C", font=("Arial", 18), bg="red", command=clear_screen)
btn_clear.grid(column=0, row=4, sticky="nsew")

btn_0 = Button(main_frame, text="0", font=("Arial", 18), command=lambda: update_digit_display("0"))
btn_0.grid(column=1, row=4, sticky="nsew")

btn_dot = Button(main_frame, text=".", font=("Arial", 18), command=lambda: update_digit_display("dot"))
btn_dot.grid(column=2, row=4, sticky="nsew")

btn_plus = Button(main_frame, text="+", font=("Arial", 18), command=lambda: set_arithmetic("plus"))
btn_plus.grid(column=3, row=4, sticky="nsew")

# Row 3 + 4 and Column 4 will be for =
btn_equal = Button(main_frame, text="=", font=("Arial", 18), command=lambda: get_results)
btn_equal.grid(column=4, row=3, rowspan=2, sticky="nsew")

btn_exit = Button(main_frame, text="Exit", font=("Arial", 18), command=safely_exit)
btn_exit.grid(column=0, row=5, columnspan=5, sticky="nsew")

root.mainloop()
