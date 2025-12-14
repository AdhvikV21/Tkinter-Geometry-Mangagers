import tkinter as tk
from datetime import date
from tkinter import messagebox

def calculate_age():
    name = e1.get()
    day = int(e2.get())
    month = int(e3.get())
    year = int(e4.get())
    today = date.today()
    birth_date = date(year, month, day)
    age = today.year - birth_date.year

root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x400")
fields = ["Name:", "Day:", "Month:", "Year:"]
entries = []

for i, text in enumerate(fields):
    tk.Label(root, text=text).grid(row=i, column=0, padx=5, pady=5, sticky="e")
    entry = tk.Entry(root, width=15)
    entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
    entries.append(entry)

e1, e2, e3, e4 = entries 
tk.Button(root, text="Calculate Age", command=calculate_age).grid(
    row=len(fields), column=0, columnspan=2, pady=15)
result = tk.Label(root, text="Enter.")
result.grid(row=len(fields) + 1, column=0, columnspan=2, pady=5)

root.mainloop()