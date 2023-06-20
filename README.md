# CACULATOR USING USER DEFINED FUNCTIONS


The code is a basic calculator GUI application written in Python using the Tkinter library. It allows the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division) to perform on those numbers. The result of the operation is displayed in a label.
* The code defines several functions: `add`, `subtract`, `multiply`, `divide`, and `sqrt`. These functions perform basic arithmetic operations. Note that the `sqrt` function uses the `numpy` library to calculate the square root.
* The code creates a GUI window using the `Tk()` class from the Tkinter library.
* The window is configured with a title, size, and background color.
* Font styles are defined for labels and buttons.
* Input fields are created using the `Label` and `Entry` classes. These fields allow the user to enter the numbers and select the operation.
* An operation selection menu is created using the `OptionMenu` class. It allows the user to choose the desired operation.
* A label is created to display the result of the calculation.
* The `calculate` function is defined as the callback for the "Calculate" button. When the button is clicked, this function is executed.
* Inside the `calculate` function, the input values and selected operation are retrieved.
* Based on the selected operation, the corresponding function is called to perform the calculation.
* The result is displayed in the result label. Exception handling is implemented to catch any errors that may occur during the calculation, such as division by zero or square root of a negative number. The error messages are displayed in the result label.
* The "Calculate" button is created with the specified text and command (the `calculate` function).
* The GUI window is displayed using the `mainloop()` method.

The code imports the `numpy` library for the square root calculation, but the `numpy` module itself is not imported. To fix this, you need to add the line `import numpy as np` at the beginning of the code. The code provides a basic calculator GUI application that performs arithmetic calculations based on user input.

## LOGIC BEHIND THE CODE:

The code is a basic calculator program implemented as a Graphical User Interface (GUI) application using the Tkinter library in Python. The calculator allows users to perform arithmetic operations such as addition, subtraction, multiplication, and division on two numbers.

The code begins by defining several arithmetic functions: `add`, `subtract`, `multiply`, `divide`, and `sqrt`. These functions are responsible for performing the corresponding mathematical operations.

The `add` function takes two numbers as input and returns their sum. For example, if the user enters 5 and 3, the `add` function will return 8.

The `subtract` function also takes two numbers as input and returns their difference. For instance, if the user enters 7 and 4, the `subtract` function will return 3.

Similarly, the `multiply` function multiplies two numbers together. If the user enters 6 and 2, the `multiply` function will return 12.

The `divide` function divides one number by another. However, it also includes error handling to prevent division by zero. If the user attempts to divide a number by zero, a `ValueError` is raised with the message "Denominator cannot be zero." Otherwise, the function performs the division and returns the quotient. For instance, if the user enters 8 and 2, the `divide` function will return 4.

The last function, `sqrt`, calculates the square root of a number using the `numpy` library. It also includes error handling to prevent the calculation of the square root of a negative number. If the user enters -9, for example, a `ValueError` is raised with the message "Square root of a negative number is not defined." Otherwise, the function calculates and returns the square root.

Moving on to the GUI code, the first step is to create a window using the `Tk()` class from the Tkinter library. The window serves as the main container for the calculator.

The window's properties are then configured. The title of the window is set to "Calculator," and its size is defined as 400 pixels by 300 pixels. Additionally, the background color of the window is set to a light gray shade.

Next, font styles are defined for labels and buttons. These styles specify the font family, size, and weight to be used in the calculator's user interface.

Following the font definitions, input fields are created using the `Label` and `Entry` classes. Labels are used to provide instructions to the user, such as "Enter first number" and "Enter second number." Entry fields allow the user to input their desired numbers.

For example, the first input field is labeled "Enter first number," and the user can enter their desired value in the corresponding entry field. Similarly, the second input field is labeled "Enter second number."

To perform operations, the user needs to select an operation from a dropdown menu. The `OptionMenu` class is used to create this menu, which includes options for addition, subtraction, multiplication, and division. By default, the menu is set to the addition operation.

A label is created to display the result of the calculation. Initially, this label is left empty. Once the user clicks the "Calculate" button, the result will be displayed in this label.



The `calculate` function is defined as the callback for the "Calculate" button. A callback function is a function that is executed when a specific event occurs, such as a button click. In this case, the `calculate` function is executed when the "Calculate" button is clicked.

Inside the `calculate` function, several steps are taken to perform the calculation based on user input.

First, the numbers entered by the user are retrieved from the input fields and converted to floating-point values. These values are stored in variables `num1` and `num2`, respectively.

Next, the selected operation is obtained from the operation selection menu. The chosen operation is stored in the `operation` variable.

Based on the selected operation, the corresponding arithmetic function is called to perform the calculation. For example, if the user selects the addition operation, the `add` function is called with `num1` and `num2` as arguments. The result of the calculation is stored in the `result` variable.

After performing the calculation, the result is displayed in the result label using the `config` method. The label's text is set to "Result: " followed by the calculated result.

The code includes exception handling to catch and handle potential errors. If a `ValueError` is raised during the calculation (such as division by zero or square root of a negative number), the corresponding error message is displayed in the result label using the `config` method. For example, if the user attempts to divide by zero, the label will display "Denominator cannot be zero." If any other exception occurs, a generic error message is displayed.

Finally, the "Calculate" button is created using the `Button` class. It is assigned the text "Calculate" and linked to the `calculate` function as its command. Additionally, the button's background color and font style are defined.

To display the GUI window and allow user interaction, the program enters the event loop using the `mainloop()` method. The event loop continuously listens for events, such as button clicks or input field changes, and triggers the associated functions.

The code implements a basic calculator GUI application using Tkinter. It allows users to input two numbers, select an operation, and perform arithmetic calculations. The calculated result is displayed in a label, and error handling is implemented to handle potential errors during the calculation process.
