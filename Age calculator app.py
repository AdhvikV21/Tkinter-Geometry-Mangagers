from tkinter import *
from tkinter import messagebox 

def validate_input():
    try:
        age = int(age_entry.get())
        if 0 < age < 150:
            messagebox.showinfo("Success", f"You are {age} years old.")
        else:
            messagebox.showerror("Error", "Please enter a valid age (1-149).")
            
    except ValueError:
        messagebox.showerror("Error", "Input must be a whole number.")
    except Exception:
        messagebox.showerror("Error", "An unexpected error occurred.")

root = Tk()
root.title('Age Input')
root.geometry('250x120')
frame = Frame(root, height=80, width= 230)

lbl = Label(frame, text = "Enter Your Age:")
age_entry = Entry(frame, width=5)
btn = Button(root, text = "Submit", command=validate_input, bg="red", fg="white")

frame.place(x=10, y=10)
lbl.place(x=10, y=10)
age_entry.place(x=120, y=10)
btn.place(x=100, y=70)

root.mainloop()