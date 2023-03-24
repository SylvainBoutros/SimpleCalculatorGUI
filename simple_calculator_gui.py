# Import modules
from tkinter import *
from tkinter import ttk
from math import sqrt

# Creating a class for the calculator
class Calculator:
    # Initializing the class with self and root as parameters
    def __init__(self, root):
        # Setting up the title and window size
        self.root = root
        root.title("Simple Calculator")
        root.geometry("300x300")
        root.resizable(0, 0) # Remove resizing option

        # Creating a main frame to hold all the buttons
        self.main_frame = ttk.Frame(root, padding=5)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.fonts = ("Arial", 18)
        
        # Creating a label for the calculator display and setting its properties
        self.digit_display = Label(self.main_frame, text="0", font=self.fonts, bg="#CCCCCC", anchor="e", width=12, justify=RIGHT)
        self.digit_display.grid(columnspan=5, row=0)

        # Row 1 and Column 0 to 4 will be for 7, 8, 9, +/- and Sqrt
        self.btn_7 = Button(self.main_frame, text="7", font=self.fonts, command=lambda: self.update_digit_display("7"))
        self.btn_7.grid(column=0, row=1, sticky="nsew")

        self.btn_8 = Button(self.main_frame, text="8", font=self.fonts, command=lambda: self.update_digit_display("8"))
        self.btn_8.grid(column=1, row=1, sticky="nsew")

        self.btn_9 = Button(self.main_frame, text="9", font=self.fonts, command=lambda: self.update_digit_display("9"))
        self.btn_9.grid(column=2, row=1, sticky="nsew")

        self.btn_plus_minus = Button(self.main_frame, text="±", font=self.fonts, command=lambda: self.set_unary_op("negate"))
        self.btn_plus_minus.grid(column=3, row=1, sticky="nsew")

        self.btn_sqrt = Button(self.main_frame, text="√", font=self.fonts, command=lambda: self.set_unary_op("sqrt"))
        self.btn_sqrt.grid(column=4, row=1, sticky="nsew")

        # Row 2 and Column 0 to 4 will be for 4, 5, 6, x, and /
        self.btn_4 = Button(self.main_frame, text="4", font=self.fonts, command=lambda: self.update_digit_display("4"))
        self.btn_4.grid(column=0, row=2, sticky="nsew")

        self.btn_5 = Button(self.main_frame, text="5", font=self.fonts, command=lambda: self.update_digit_display("5"))
        self.btn_5.grid(column=1, row=2, sticky="nsew")

        self.btn_6 = Button(self.main_frame, text="6", font=self.fonts, command=lambda: self.update_digit_display("6"))
        self.btn_6.grid(column=2, row=2, sticky="nsew")

        self.btn_mult = Button(self.main_frame, text="x", font=self.fonts, command=lambda: self.set_arithmetic("mult"))
        self.btn_mult.grid(column=3, row=2, sticky="nsew")

        self.btn_div = Button(self.main_frame, text="÷", font=self.fonts, command=lambda: self.set_arithmetic("div"))
        self.btn_div.grid(column=4, row=2, sticky="nsew")

        # Row 3 and Column 0 to 3 will be for 1, 2, 3, and -
        self.btn_1 = Button(self.main_frame, text="1", font=self.fonts, command=lambda: self.update_digit_display("1"))
        self.btn_1.grid(column=0, row=3, sticky="nsew")

        self.btn_2 = Button(self.main_frame, text="2", font=self.fonts, command=lambda: self.update_digit_display("2"))
        self.btn_2.grid(column=1, row=3, sticky="nsew")

        self.btn_3 = Button(self.main_frame, text="3", font=self.fonts, command=lambda: self.update_digit_display("3"))
        self.btn_3.grid(column=2, row=3, sticky="nsew")

        self.btn_minus = Button(self.main_frame, text="-", font=self.fonts, command=lambda: self.set_arithmetic("minus"))
        self.btn_minus.grid(column=3, row=3, sticky="nsew")

        # Row 4 and Column 0 to 3 will be for C, 0, ., and +
        self.btn_clear = Button(self.main_frame, text="C", font=self.fonts, bg="red", command=self.clear_screen)
        self.btn_clear.grid(column=0, row=4, sticky="nsew")

        self.btn_0 = Button(self.main_frame, text="0", font=self.fonts, command=lambda: self.update_digit_display("0"))
        self.btn_0.grid(column=1, row=4, sticky="nsew")

        self.btn_dot = Button(self.main_frame, text=".", font=self.fonts, command=lambda: self.update_digit_display("dot"))
        self.btn_dot.grid(column=2, row=4, sticky="nsew")

        self.btn_plus = Button(self.main_frame, text="+", font=self.fonts, command=lambda: self.set_arithmetic("plus"))
        self.btn_plus.grid(column=3, row=4, sticky="nsew")

        # Row 3 + 4 and Column 4 will be for =
        self.btn_equal = Button(self.main_frame, text="=", font=self.fonts, command=self.get_results)
        self.btn_equal.grid(column=4, row=3, rowspan=2, sticky="nsew")

        self.btn_exit = Button(self.main_frame, text="Exit", font=self.fonts, command=self.safely_exit)
        self.btn_exit.grid(column=0, row=5, columnspan=5, sticky="nsew")

        # Create some variables to keep track of things
        self.results = None
        self.operations = None

    def update_digit_display(self, digit):
        """ Updates the digit display based on input (digit)
        
        If digit is "dot" it checks to see that there isn't already a "." in the string.
        Then it adds the digit to the string that gets updated to the digit display.

        Args:
            digit (str): The input digit to add to the digit display, or the "dot" to add the decimal point.

        Returns:
            None
        """
        if digit == "dot":
            # Check if digit display already contains a decimal point
            if "." not in self.digit_display["text"]:
                self.digit_display["text"] += "."
            else:
                pass # If there is, do nothing
        else:
            # Check if digit display is showing "0" and if input (digit) is not "0"
            # then update the digit display to that input (digit).  digit display is 
            # showing "0" and if input (digit) is "0", then leave it as is. Otherwise
            # append the input (digit) to the digit display
            if self.digit_display["text"] == "0" and digit != "0":
                self.digit_display["text"] = digit
            elif self.digit_display["text"] == "0" and digit == "0":
                self.digit_display["text"] = digit
            else:
                self.digit_display["text"] += digit

    def set_unary_op(self, op):
        """
        Perform the unary operations based on input (op)

        If op is "sqrt", it try to calculate the square root of the current operand that was in the digit display.
        If op is "negate", it multiply the current operand by -1
        Additionally, to keep the number from going off the screen we perfom a check for the length and format 
        it back to about 9 digits if it's above 9

        Args:
            op (str): The unary operation to perform. Can be "sqrt" or "negate".
        
        Returns:
            None
        """
        # Get the current operand from the digit display
        current_operand = float(self.digit_display["text"])
        # Check if op is "sqrt"
        # If it is, try to perfom square root operation on it
        # Catch error if its a negative number and update the display 
        # Reset the variables
        if op == "sqrt":
            try:
                current_operand = sqrt(current_operand)
            except ValueError:
                self.digit_display["text"] = str("Invalid input")
                self.results = None
                self.operations = None
                return
        # Otherwise it's the negate op and we multiply the current operand by -1
        else:
            current_operand *= -1
        
        # Additionally, do check for maintaining visibility on screen with number that have a long
        if len(str(current_operand))>9:
            self.digit_display["text"] = "{:.9g}".format(float(current_operand))
        else:
            self.digit_display["text"] = str(current_operand)

        # Update the results to hold the current operand
        self.results = float(self.digit_display["text"])

    def set_arithmetic(self, ari):
        """
        Sets the arithmetic operation for the calculator

        Args:
            ari (str): The arithmetic operation to set. Can be "plus", "minus", "mult", "div".

        Returns:
            None
        """
        # Get current operand from the digit display
        current_operand = float(self.digit_display["text"])
        # Reset the display
        self.digit_display["text"] = ""
        # Assign the current operand value to results
        self.results = current_operand
        # Assign the current arithmetic value to operations
        self.operations = ari

    def get_results(self):
        """
        Get results from arithmetic operations and display them on the digit display

        Args:
            None
        
        Return:
            None
        """
        # Check if operation is None and break if it is, nothing to do here
        if self.operations is None:
            return
        
        # Get the current operand from the digit display
        current_operand = float(self.digit_display["text"])
        # If operation is set to "plus" perform addition
        if self.operations == "plus":
            results = self.results + current_operand
        # If operation is set to "minus" perform subtraction
        elif self.operations == "minus":
            results = self.results - current_operand
        # If operation is set to "mult" perform multiplication
        elif self.operations == "mult":
            results = self.results * current_operand
        # If operation is set to "div" perform division
        # first check if the current operand is not 0
        # return error and clear variables if it is.
        # Otherwise, perform division
        elif self.operations == "div":
            if current_operand == 0:
                self.digit_display["text"] = "Cannot divide by zero"
                self.results = None
                self.operations = None
                return
            results = self.results / current_operand
        else:
            return
        
        # Update the digit display
        self.digit_display["text"] = str(results)
        # Set the results in case of multiple operations
        self.results = results
        # Clear operation for next one
        self.operations = None

    def safely_exit(self):
        """
        Safely exit the program by destroying the windows

        Args:
            None
        
        Return:
            None
        """
        self.root.destroy()
    
    def clear_screen(self):
        """
        Clear the screen from everything and reset the variables

        Args:
            None
        
        Return:
            None
        """
        self.digit_display["text"] = "0"
        self.results = None
        self.operations = None

    def run(self):
        """
        Run the program

        Args:
            None

        Return:
            None
        """
        self.root.mainloop()

if __name__ == "__main__":
    root = Tk()
    calc = Calculator(root)
    calc.run()
