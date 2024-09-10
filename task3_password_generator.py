
import string
import random
import tkinter as tk

def generate_password():
    length = entry_length.get()

    if length.isdigit() and int(length) > 0:
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(password_characters) for _ in range(int(length)))
        
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    else:
        entry_password.delete(0, tk.END)
        entry_password.insert(0, "Enter a valid number")

window = tk.Tk()
window.title("Simple Password Generator")
window.geometry("300x150") 

label_length = tk.Label(window, text="Enter the length of the password:")
label_length.pack(pady=5)

entry_length = tk.Entry(window)
entry_length.pack(pady=5)


button_generate = tk.Button(window, text="Generate Password", command=generate_password)
button_generate.pack(pady=5)


entry_password = tk.Entry(window, width=30)
entry_password.pack(pady=5)

window.mainloop()

