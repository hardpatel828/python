# Write a Python program that implements a temperature converter application using Tkinter, allowing
# users to convert between Celsius and Fahrenheit.

import tkinter as tk

def celsius_to_fahrenheit():
    c = float(entry.get())
    f = (c * 9/5) + 32
    result_label.config(text="Fahrenheit: " + str(f))

def fahrenheit_to_celsius():
    f = float(entry.get())
    c = (f - 32) * 5/9
    result_label.config(text="Celsius: " + str(c))

window = tk.Tk()
window.title("Temperature Converter")
window.geometry("300x250")

heading = tk.Label(window, text="Temperature Converter", font=("Arial", 14))
heading.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=5)

btn1 = tk.Button(window, text="Celsius to Fahrenheit", command=celsius_to_fahrenheit)
btn1.pack(pady=5)

btn2 = tk.Button(window, text="Fahrenheit to Celsius", command=fahrenheit_to_celsius)
btn2.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
