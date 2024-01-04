import tkinter as tk

def convert_temperature():
    celsius = float(entry.get())
    fahrenheit = (celsius * 9/5) + 32
    reamur = celsius * 4/5
    kelvin = celsius + 273.15

    result_label.config(text=f"{celsius} Celsius = {fahrenheit} Fahrenheit\n"
                              f"{celsius} Celsius = {reamur} Reamur\n"
                              f"{celsius} Celsius = {kelvin} Kelvin", fg="blue")

# Setup GUI
root = tk.Tk()
root.title("Konverter Suhu")
root.configure(bg='lightgray')

input_label = tk.Label(root, text="Masukkan suhu dalam Celsius:", bg='lightgray')
input_label.pack()

entry = tk.Entry(root)
entry.pack()

convert_button = tk.Button(root, text="Konversi", command=convert_temperature, bg='cyan', fg='black')
convert_button.pack()

result_label = tk.Label(root, text="", bg='lightgray')
result_label.pack()

root.mainloop()