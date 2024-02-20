import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    try:
        temperature = float(temperature_entry.get())
        original_unit = original_unit_combobox.get().lower()
        
        if original_unit == 'celsius':
            fahrenheit = celsius_to_fahrenheit(temperature)
            kelvin = celsius_to_kelvin(temperature)
            result_label.config(text=f"{temperature} Celsius is equal to {fahrenheit:.2f} Fahrenheit and {kelvin:.2f} Kelvin.")
        elif original_unit == 'fahrenheit':
            celsius = fahrenheit_to_celsius(temperature)
            kelvin = fahrenheit_to_kelvin(temperature)
            result_label.config(text=f"{temperature} Fahrenheit is equal to {celsius:.2f} Celsius and {kelvin:.2f} Kelvin.")
        elif original_unit == 'kelvin':
            celsius = kelvin_to_celsius(temperature)
            fahrenheit = kelvin_to_fahrenheit(temperature)
            result_label.config(text=f"{temperature} Kelvin is equal to {celsius:.2f} Celsius and {fahrenheit:.2f} Fahrenheit.")
        else:
            result_label.config(text="Invalid input! Please enter either Celsius, Fahrenheit, or Kelvin.")
    except ValueError:
        result_label.config(text="Invalid temperature value! Please enter a valid number.")

# Create main application window
root = tk.Tk()
root.title("Temperature Conversion Program")

# Create input widgets
temperature_label = ttk.Label(root, text="Enter temperature:")
temperature_label.grid(row=0, column=0, padx=5, pady=5)

temperature_entry = ttk.Entry(root, width=10)
temperature_entry.grid(row=0, column=1, padx=5, pady=5)

original_unit_label = ttk.Label(root, text="Select original unit:")
original_unit_label.grid(row=1, column=0, padx=5, pady=5)

original_unit_combobox = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
original_unit_combobox.grid(row=1, column=1, padx=5, pady=5)
original_unit_combobox.current(0)

convert_button = ttk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create output widget
result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()