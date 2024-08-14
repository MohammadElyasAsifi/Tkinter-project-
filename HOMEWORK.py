import tkinter as tk
from tkinter import scrolledtext

def show_message():
    message = """
def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    return sequence

n = 10 
fibonacci = fibonacci_sequence(n)
print(fibonacci)

2.factorial formula:
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    elif n < 1:
        print("error")
    else:
        return 1
print(factorial(10))

3. Built in functions:

Python abs()
returns absolute value of a number

Python all()
returns true when all elements in iterable is true

Python any()
Checks if any Element of an Iterable is True

Python ascii()
Returns String Containing Printable Representation

Python bin()
converts integer to binary string

Python bool()
Converts a Value to Boolean

Python bytearray()
returns array of given byte size

Python bytes()
returns immutable bytes object

Python callable()
Checks if the Object is Callable

Python chr()
Returns a Character (a string) from an Integer

Python classmethod()
returns class method for given function

Python compile()
Returns a Python code object

Python complex()
Creates a Complex Number

Python delattr()
Deletes Attribute From the Object

Python dict()
Creates a Dictionary

Python dir()
Tries to Return Attributes of Object

Python divmod()
Returns a Tuple of Quotient and Remainder

Python enumerate()
Returns an Enumerate Object

Python eval()
Runs Python Code Within Program

Python exec()
Executes Dynamically Created Program

Python filter()
constructs iterator from elements which are true

Python float()
returns floating point number from number, string

Python format()
returns formatted representation of a value

Python frozenset()
returns immutable frozenset object

Python getattr()
returns value of named attribute of an object

Python globals()
returns dictionary of current global symbol table

Python hasattr()
returns whether object has named attribute

Python hash()
returns hash value of an object

Python help()
Invokes the built-in Help System

Python hex()
Converts to Integer to Hexadecimal

Python id()
Returns Identify of an Object

Python input()
reads and returns a line of string

Python int()
returns integer from a number or string

Python isinstance()
Checks if a Object is an Instance of Class

Python issubclass()
Checks if a Class is Subclass of another
"""
    message_label.config(state=tk.NORMAL)
    message_label.delete(1.0, tk.END)
    message_label.insert(tk.END, message)
    message_label.config(state=tk.DISABLED)  

root = tk.Tk()
root.title("Message Window")
root.geometry("800x600")

message_label = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Helvetica", 8), width=100, height=30)
message_label.pack(pady=20)

show_button = tk.Button(root, text="Show Message", command=show_message)
show_button.pack(pady=10)

root.mainloop()