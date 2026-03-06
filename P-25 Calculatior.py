# Write a Python GUI program to create calculator application using radio buttons widgets of tkinter
# module.

# Import tkinter module
import tkinter as tk

# Function to perform calculation
def calculate():
    a = float(entry1.get())
    b = float(entry2.get())
    op = choice.get()

    if op == 1:
        result = a + b
    elif op == 2:
        result = a - b
    elif op == 3:
        result = a * b
    elif op == 4:
        result = a / b

    result_label.config(text="Result: " + str(result))

# Create main window
window = tk.Tk()
window.title("Calculator using Radio Buttons")
window.geometry("300x350")

# Labels and Entry fields
tk.Label(window, text="Enter First Number").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Enter Second Number").pack()
entry2 = tk.Entry(window)
entry2.pack()

# Variable for radio buttons
choice = tk.IntVar()

# Radio Buttons
tk.Radiobutton(window, text="Addition", variable=choice, value=1).pack()
tk.Radiobutton(window, text="Subtraction", variable=choice, value=2).pack()
tk.Radiobutton(window, text="Multiplication", variable=choice, value=3).pack()
tk.Radiobutton(window, text="Division", variable=choice, value=4).pack()

# Calculate Button
tk.Button(window, text="Calculate", command=calculate).pack(pady=10)

# Result Label
result_label = tk.Label(window, text="Result:")
result_label.pack()

# Run the application
window.mainloop()