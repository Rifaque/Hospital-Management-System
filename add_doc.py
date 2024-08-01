import tkinter as tk
import random
from tkinter import messagebox
import mysql.connector




class DoctorRegisterForm:
    def __init__(self, master):
        self.master = master
        master.title("Doctor Register Form")
        self.master.geometry("900x800")
        self.master.configure(background='#5a93cb')

        #frame
        self.frame = tk.Frame(self.master, bg='#5a93cb')
        self.frame.pack(pady=50, padx=150,fill='both', anchor='center')
        #heading
        tk.Label(self.frame, text="DOCTOR FORM",
                               font=("Arial", 16, "bold"), fg='#E0E0E0', bg='#961C51').grid(row=0, column=0,
                                                                                                    pady=(10, 5))
        #title_label.place(relx=0.5, rely=0.05, anchor="center")
        # Create labels and entry fields
        tk.Label(self.frame, text="First Name:", font=('Helvetica', 16, 'bold'), bg='#5a93cb').grid(row=1, column=0,
                                                                                                    pady=(10, 5))
        self.first_name_entry = tk.Entry(self.frame, width=30, font=('Helvetica', 16))
        self.first_name_entry.grid(row=1, column=1, pady=(10, 5))

        tk.Label(self.frame, text="Last Name:", font=('Helvetica', 16, 'bold'), bg='#5a93cb').grid(row=2, column=0,
                                                                                                   pady=(5, 5))
        self.last_name_entry = tk.Entry(self.frame, width=30, font=('Helvetica', 16))
        self.last_name_entry.grid(row=2, column=1, pady=(5, 5))

        tk.Label(self.frame, text="Specialization:", font=('Helvetica', 16, 'bold'), bg='#5a93cb').grid(row=3, column=0,
                                                                                                        pady=(5, 5))
        self.specialization_entry = tk.Entry(self.frame, width=30, font=('Helvetica', 16))
        self.specialization_entry.grid(row=3, column=1, pady=(5, 5))

        tk.Label(self.frame, text="Qualifications:", font=('Helvetica', 16, 'bold'), bg='#5a93cb').grid(row=4, column=0,
                                                                                                        pady=(5, 5))
        self.qualifications_entry = tk.Entry(self.frame, width=30, font=('Helvetica', 16))
        self.qualifications_entry.grid(row=4, column=1, pady=(5, 5))

        tk.Label(self.frame, text="Experience:", font=('Helvetica', 16, 'bold'), bg='#5a93cb').grid(row=5, column=0,
                                                                                                    pady=(5, 5))
        self.experience_entry = tk.Entry(self.frame, width=30, font=('Helvetica', 16))
        self.experience_entry.grid(row=5, column=1, pady=(5, 5))

        tk.Label(self.frame, text="Hospital ID:", font=('Helvetica', 16, 'bold'), bg='#5a93cb').grid(row=6, column=0,
                                                                                                     pady=(5, 5))
        self.hospital_id_entry = tk.Entry(self.frame, width=30, font=('Helvetica', 16))
        self.hospital_id_entry.grid(row=6, column=1, pady=(5, 5))

        tk.Label(self.frame, text="Department:", font=('Helvetica', 16, 'bold'), bg='#5a93cb').grid(row=7, column=0,
                                                                                                    pady=(5, 5))
        self.department_entry = tk.Entry(self.frame, width=30, font=('Helvetica', 16))
        self.department_entry.grid(row=7, column=1, pady=(5, 5))

        tk.Label(self.frame, text="Room No:", font=('Helvetica', 16, 'bold'), bg='#5a93cb').grid(row=8, column=0,
                                                                                                 pady=(5, 5))
        self.room_no_entry = tk.Entry(self.frame, width=30, font=('Helvetica', 16))
        self.room_no_entry.grid(row=8, column=1, pady=(5, 5))

        tk.Label(self.frame, text="Phone No:", font=('Helvetica', 16, 'bold'), bg='#5a93cb').grid(row=9, column=0,
                                                                                                  pady=(5, 5))
        self.phone_no_entry = tk.Entry(self.frame, width=30, font=('Helvetica', 16))
        self.phone_no_entry.grid(row=9, column=1, pady=(5, 5))

        tk.Label(self.frame, text="Email:", font=('Helvetica', 16, 'bold'), bg='#5a93cb').grid(row=10, column=0,
                                                                                               pady=(5, 5))
        self.email_entry = tk.Entry(self.frame, width=30, font=('Helvetica', 16))
        self.email_entry.grid(row=10, column=1, pady=(5, 5))

        tk.Label(self.frame, text="Address:", font=('Helvetica', 16, 'bold'), bg='#5a93cb').grid(row=11, column=0,
                                                                                                 pady=(5, 10))
        self.address_entry = tk.Entry(self.frame, width=30, font=('Helvetica', 16))
        self.address_entry.grid(row=11, column=1, pady=(5, 10))

        # Create register button
        tk.Button(self.frame, text="Register", command=self.register_doctor, font=('Helvetica', 14, 'bold')).grid(
            row=12, column=1, pady=(10, 10))

    def register_doctor(self):
        # Get values from entry fields
        doc_id = "DOC" + str(random.randint(100, 999))
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        specialization = self.specialization_entry.get()
        qualifications = self.qualifications_entry.get()
        experience = self.experience_entry.get()
        hospital_id = self.hospital_id_entry.get()
        department = self.department_entry.get()
        room_no = self.room_no_entry.get()
        phone_no = self.phone_no_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        # Validate input (very basic validation)
        if not all([first_name, last_name, specialization, qualifications, experience, hospital_id, department, room_no, phone_no, email, address]):
            messagebox.showerror("Error", "Please fill in all fields")
            return
        #sql connect


        # Define the database connection parameters
        username = 'the'
        password = 'password'
        hostname = 'localhost'
        database = 'hpms'

        # Establish the connection
        cnx = mysql.connector.connect(
            user=username,
            password=password,
            host=hostname,
            database=database
        )

        # Create a cursor object to execute queries
        cursor = cnx.cursor()

        # Define the insert query
        query = """
            INSERT INTO Doctor (
                Doctor_id,
                First_Name,
                Last_Name,
                Specialization,
                Qualifications,
                Experience,
                Hospital_ID,
                Department,
                Room_No,
                Phone_No,
                Email,
                Address
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Execute the insert query
        cursor.execute(query, (
            doc_id,
            first_name,
            last_name,
            specialization,
            qualifications,
            experience,
            hospital_id,
            department,
            room_no,
            phone_no,
            email,
            address
        ))

        # Commit the changes
        cnx.commit()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

        messagebox.showinfo("Success", "Doctor registered successfully!")
        self.master.destroy()
def docinsertrun():
    root = tk.Tk()
    my_form = DoctorRegisterForm(root)
    root.mainloop()
