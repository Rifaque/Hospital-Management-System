import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Registration")

# Set the window size
root.geometry("1166x718")
root.state('zoomed')

# Load the background image
background_image = Image.open("images\\backroundreal.png")
background_photo = ImageTk.PhotoImage(background_image)

# Create a label for the background image
background_label = tk.Label(root, image=background_photo)

background_label.place(x=0, y=0, relwidth=1, relheight=1)


 # ====== Login Frame =========================
lgn_frame = tk.Frame(root, bg='#040405', width=950, height=600)
lgn_frame.place(relx=0.5, rely=0.5,anchor=tk.CENTER)
lgn_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
# ========================================================================
# Create the input fields
patient_name_label = tk.Label(root, text="Patient Name", bg="white", fg="black", font=("Arial", 12))
patient_name_label.place(x=50, y=100)
patient_name_entry = tk.Entry(root, width=30, borderwidth=2, relief="solid")
patient_name_entry.place(x=50, y=130)

email_label = tk.Label(root, text="Email Address", bg="white", fg="black", font=("Arial", 12))
email_label.place(x=50, y=160)
email_entry = tk.Entry(root, width=30, borderwidth=2, relief="solid")
email_entry.place(x=50, y=190)

password_label = tk.Label(root, text="Password", bg="white", fg="black", font=("Arial", 12))
password_label.place(x=50, y=220)
password_entry = tk.Entry(root, width=30, borderwidth=2, relief="solid", show="*")
password_entry.place(x=50, y=250)

confirm_password_label = tk.Label(root, text="Confirm Password", bg="white", fg="black", font=("Arial", 12))
confirm_password_label.place(x=50, y=280)
confirm_password_entry = tk.Entry(root, width=30, borderwidth=2, relief="solid", show="*")
confirm_password_entry.place(x=50, y=310)

# Create the register button
register_button = tk.Button(root, text="REGISTER", width=15, height=2, font=("Arial", 12, "bold"), fg="white", bg="#4CAF50", borderwidth=0, cursor="hand2")
register_button.place(x=50, y=350)

# Create the login button
login_button = tk.Button(root, text="LOGIN", width=15, height=2, font=("Arial", 12, "bold"), fg="white", bg="#4CAF50", borderwidth=0, cursor="hand2")
login_button.place(x=50, y=400)

# Create the logo
logo_image = Image.open("images\\hyy.png")
logo_image = logo_image.resize((100, 50))
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(root, image=logo_photo, bg="white")
logo_label.place(x=50, y=30)

# Create the navigation buttons
home_button = tk.Button(root, text="HOME", width=10, height=1, font=("Arial", 12), fg="white", bg="#4CAF50", borderwidth=0, cursor="hand2")
home_button.place(x=50, y=450)

services_button = tk.Button(root, text="SERVICES", width=10, height=1, font=("Arial", 12), fg="white", bg="#4CAF50", borderwidth=0, cursor="hand2")
services_button.place(x=150, y=450)

about_button = tk.Button(root, text="ABOUT", width=10, height=1, font=("Arial", 12), fg="white", bg="#4CAF50", borderwidth=0, cursor="hand2")
about_button.place(x=250, y=450)

contact_us_button = tk.Button(root, text="CONTACT US!", width=15, height=1, font=("Arial", 12), fg="white", bg="#4CAF50", borderwidth=0, cursor="hand2")
contact_us_button.place(x=350, y=450)

root.mainloop()