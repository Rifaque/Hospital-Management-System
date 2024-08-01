import tkinter as tk
from tkinter import font, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import random


class Reg:
    def __init__(self):
        # Create main window

        self.root1 = tk.Tk()
        self.root1.title("Doctor Appointment Form")

        # Set window size and position
        self.screen_width = self.root1.winfo_screenwidth()
        self.screen_height = self.root1.winfo_screenheight()
        self.window_width = self.screen_width
        self.window_height = self.screen_height
        self.root1.state('zoomed')
    # Create background

    def set_background(self):
        background_frame=tk.Frame(self.root1,background='#961C51',width=self.window_width,height=self.window_height)
        background_frame.place(relx=0.5, rely=0.5,anchor="center")
        # Create label for title with adjusted size
        #title_font = font.Font(family="Arial", size="60", weight="bold")
        title_label = tk.Label(self.root1, text="CYPHER HEALTH CENTER\nDOCTOR APPOINTMENT FORM",
                               font=("Arial", 60, "bold"), fg='#E0E0E0', bg='#961C51')
        title_label.place(relx=0.5, rely=0.15, anchor="center")

    def create_gui(self):
        # Create a frame for form fields
        form_frame = tk.Frame(self.root1, background='#FAF9F6')
        form_frame.place(relx=0.5, rely=0.55, anchor="center", width=1000, height=500)
        # Create form fields inside the frame
        fname_label = tk.Label(form_frame, text="First Name", font=("Arial", 19))
        fname_entry = tk.Entry(form_frame, font=("Arial", 19))
        lname_label = tk.Label(form_frame, text="Last Name", font=("Arial", 19))
        lname_entry = tk.Entry(form_frame, font=("Arial", 19))
        phone_label = tk.Label(form_frame, text="Phone Number", font=("Arial", 19))
        phone_entry = tk.Entry(form_frame, font=("Arial", 19))
        email_label = tk.Label(form_frame, text="Email", font=("Arial", 19))
        email_entry = tk.Entry(form_frame, font=("Arial", 19))
        address_label = tk.Label(form_frame, text="Address", font=("Arial", 19))
        address_entry = tk.Entry(form_frame, font=("Arial", 19))
        age_label = tk.Label(form_frame, text="Age", font=("Arial", 19))
        age_entry = tk.Entry(form_frame, font=("Arial", 19))
        dob_label = tk.Label(form_frame, text="Date of Birth", font=("Arial", 19))
        dob_entry = tk.Entry(form_frame, font=("Arial", 19))
        symptoms_label = tk.Label(form_frame, text="Symptoms", font=("Arial", 19))
        symptoms_entry = tk.Entry(form_frame, font=("Arial", 19))
        blood_label = tk.Label(form_frame, text="Blood Group", font=("Arial", 19))
        blood_entry = tk.StringVar()
        blood_combobox = ttk.Combobox(form_frame, textvariable=blood_entry, font=("Arial", 18))
        blood_combobox['values'] = ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")
        doctor_label = tk.Label(form_frame, text="Doctor", font=("Arial", 19))
        doctor_entry = tk.StringVar()
        doctor_combobox = ttk.Combobox(form_frame, textvariable=doctor_entry, font=("Arial", 18))
        doctor_combobox['values'] = ('Dr. Chetan (MBBS)', 'Dr. Sunil (BHMS)', 'Dr. Ahmed (B.Pharm)', 'Dr. Thomas (MDS)')
        time_label = tk.Label(form_frame, text="Time", font=("Arial", 19))
        time_entry = tk.StringVar()
        time_combobox = ttk.Combobox(form_frame, textvariable=time_entry, font=("Arial", 18))
        time_combobox['values'] = ('10 am', '11 am', '12 pm', '1 pm', '2 pm')
        pat_no = "pat" + str(random.randint(100, 999))

        def submit_appointment():
            patient_id = pat_no
            messagebox.showinfo("Appointment Booking", f"Appointment successfully booked\n\tpatient_id={patient_id}")
            response = messagebox.askyesno("Continue?", "Do you want to book another appointment?")
            if response:
                # Rerun the interface
                fname_entry.delete(0, tk.END)  # Clear the entry field
                lname_entry.delete(0, tk.END)
                phone_entry.delete(0, tk.END)
                email_entry.delete(0, tk.END)
                address_entry.delete(0, tk.END)
                age_entry.delete(0, tk.END)
                dob_entry.delete(0, tk.END)
                blood_combobox.set("")
                doctor_combobox.set("")  # Clear the combobox
                symptoms_entry.delete(0, tk.END)
                time_combobox.set("")
            else:
                # Exit the current interface
                self.root1.destroy()

        def validate_form():
            if not fname_entry.get().strip():
                messagebox.showwarning("Validation Error", "First Name is required")
                return False
            if not lname_entry.get().strip():
                messagebox.showwarning("Validation Error", "Last Name is required")
                return False
            if not phone_entry.get().strip():
                messagebox.showwarning("Validation Error", "Phone Number is required")
                return False
            if not email_entry.get().strip():
                messagebox.showwarning("Validation Error", "Email is required")
                return False
            if not address_entry.get().strip():
                messagebox.showwarning("Validation Error", "Address is required")
                return False
            if not age_entry.get().strip():
                messagebox.showwarning("Validation Error", "Age is required")
                return False
            if not dob_entry.get().strip():
                messagebox.showwarning("Validation Error", "Date of Birth is required")
                return False
            if not blood_combobox.get().strip():
                messagebox.showwarning("Validation Error", "Doctor selection is required")
                return False
            if not doctor_combobox.get().strip():
                messagebox.showwarning("Validation Error", "Doctor selection is required")
                return False
            if not time_combobox.get().strip():
                messagebox.showwarning("Validation Error", "Appointment Time is required")
                return False
            return True

        def register():
            if validate_form():
                import registerconnect
                firstname = fname_entry.get()
                lastname = lname_entry.get()
                ph_no = phone_entry.get()
                email = email_entry.get()
                address = address_entry.get()
                age = age_entry.get()
                dob = dob_entry.get()
                blood = blood_combobox.get()
                doctor = doctor_combobox.get()
                symptoms = symptoms_entry.get()
                t_of_appointment = time_combobox.get()
                registerconnect.insert_patient_data(pat_no, firstname, lastname, ph_no, email, address, age, dob, blood, doctor, t_of_appointment, symptoms)
                submit_appointment()

        submit_button = tk.Button(form_frame, text='SUBMIT', font=("yu gothic ui", 13, "bold"),
                                  width=25, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff',
                                  fg='white', command=register)
        # Grid layout for form fields
        fname_label.grid(row=0, column=0, pady=10, padx=10)
        fname_entry.grid(row=0, column=1, pady=10, padx=10)
        lname_label.grid(row=1, column=0, pady=10, padx=10)
        lname_entry.grid(row=1, column=1, pady=10, padx=10)
        phone_label.grid(row=2, column=0, pady=10, padx=10)
        phone_entry.grid(row=2, column=1, pady=10, padx=10)
        email_label.grid(row=3, column=0, pady=10, padx=10)
        email_entry.grid(row=3, column=1, pady=10, padx=10)
        address_label.grid(row=4, column=0, pady=10, padx=10)
        address_entry.grid(row=4, column=1, pady=10, padx=10)
        age_label.grid(row=5, column=0, pady=10, padx=10)
        age_entry.grid(row=5, column=1, pady=10, padx=10)
        dob_label.grid(row=6, column=0, pady=10, padx=10)
        dob_entry.grid(row=6, column=1, pady=10, padx=10)
        blood_label.grid(row=0, column=2, pady=10, padx=10)
        blood_combobox.grid(row=0, column=3)
        doctor_label.grid(row=1, column=2, pady=10, padx=10)
        doctor_combobox.grid(row=1, column=3)
        symptoms_label.grid(row=2, column=2, pady=10, padx=10)
        symptoms_entry.grid(row=2, column=3, pady=10, padx=10)
        time_label.grid(row=3, column=2, pady=10, padx=10)
        time_combobox.grid(row=3, column=3)
        submit_button.grid(row=8, column=0, columnspan=4, pady=20, padx=20)

    def run(self):
        self.set_background()
        self.create_gui()
        self.root1.mainloop()


def registerpage():
    app = Reg()
    app.run()


    