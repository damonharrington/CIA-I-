#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import numpy as np
from tkinter import Tk, Label, Entry, OptionMenu, StringVar, Button, Toplevel

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        raise ValueError("Denominator cannot be zero")
    return x / y

# Function to calculate square root of a number
def sqrt(x):
    if x < 0:
        raise ValueError("Square root of negative number is not defined")
    return np.sqrt(x)

# Global variables
history = []

# GUI Code
root = Tk()
root.title("Calculator")

# Configure window size and background color
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Define font styles
label_font = ("Arial", 12)
button_font = ("Arial", 14, "bold")

# Input fields
num1_label = Label(root, text="Enter first number", bg="#f0f0f0", font=label_font)
num1_label.pack()
num1_entry = Entry(root)
num1_entry.pack()

num2_label = Label(root, text="Enter second number", bg="#f0f0f0", font=label_font)
num2_label.pack()
num2_entry = Entry(root)
num2_entry.pack()

# Operation selection menu
operation_label = Label(root, text="Select operation", bg="#f0f0f0", font=label_font)
operation_label.pack()
operation_var = StringVar(root)
operation_var.set("+")  # Default value
operation_menu = OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.pack()

result_label = Label(root, text="", bg="#f0f0f0", font=label_font)
result_label.pack()

# Calculate button callback
def calculate():
    try:
        # Get input values
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())

        # Get selected operation
        operation = operation_var.get()

        # Execute selected operation
        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)

        # Append calculation to history
        history.append((num1, operation, num2, result))

        # Display result
        result_label.config(text=f"Result: {result}")

    except ValueError as e:
        result_label.config(text=str(e))
    except Exception as e:
        result_label.config(text="An error occurred")

calculate_button = Button(root, text="Calculate", command=calculate, bg="#d3d3d3", font=button_font)
calculate_button.pack(pady=10)

# History button callback
def show_history():
    history_window = Toplevel(root)
    history_window.title("Calculation History")

    # Configure window size and background color
    history_window.geometry("400x300")
    history_window.configure(bg="#f0f0f0")

    # History label
    history_label = Label(history_window, text="Calculation History", font=("Arial", 12, "bold"), pady=10)
    history_label.pack()

    # Display history
    for calculation in history:
        num1, operation, num2, result = calculation
        calculation_text = f"{num1} {operation} {num2} = {result}"
        calculation_label = Label(history_window, text=calculation_text, font=("Arial", 10))
        calculation_label.pack()

history_button = Button(root, text="History", command=show_history, bg="#d3d3d3", font=button_font)
history_button.pack(pady=10)

root.mainloop()


# In[ ]:




