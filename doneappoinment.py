import mysql.connector
import tkinter as tk
from tkinter import messagebox

def connect_to_db():
    try:
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

        return cnx, cursor

    except mysql.connector.Error as err:
        print("Error connecting to database:", err)
        return None, None

class AppointmentDeleter:
    def __init__(self, master):
        self.master = master
        self.master.title("Delete Appointment")
        self.master.geometry("600x500")
        self.master.configure(background='#5a93cb')  # Set the background color of the main window

        # Create a frame to hold the widgets
        self.frame = tk.Frame(self.master, bg='#5a93cb')
        self.frame.pack(pady=100, fill='both', expand=True)  # Fill the frame to the entire window

        # Create the label, entry, and button
        self.appointment_id_label = tk.Label(self.frame, text="Enter Appointment ID Or pat_no:", font=("Arial", 20, "bold"), fg='#E0E0E0', bg='#5a93cb')
        self.appointment_id_label.pack(pady=20)

        self.appointment_id_entry = tk.Entry(self.frame, font=("Arial", 20), width=20, bg='#E0E0E0')
        self.appointment_id_entry.pack(pady=20)

        self.delete_button = tk.Button(self.frame, text="Delete", command=self.delete_appointment, font=("Arial", 20), fg='white', bg='#E0E0E0')
        self.delete_button.pack(pady=20)

    def delete_appointment(self):
        appointment_id = self.appointment_id_entry.get()
        if appointment_id:
            try:
                # Establish the database connection
                cnx, cursor = connect_to_db()

                # Create a query to delete the appointment
                query = "DELETE FROM appointment_details WHERE pat_no = %s"
                cursor.execute(query, (appointment_id,))

                # Commit the changes
                cnx.commit()

                # Close the cursor and connection
                cursor.close()
                cnx.close()

                # Show a message box to confirm the deletion
                messagebox.showinfo("Appointment Deleted", "Appointment deleted successfully!")
                self.master.destroy()

            except mysql.connector.Error as err:
                print("Error deleting appointment:", err)
                messagebox.showerror("Error", "Failed to delete appointment")
        else:
            messagebox.showerror("Error", "Please enter an appointment ID")

def doneapp():
    root = tk.Tk()
    app = AppointmentDeleter(root)
    root.mainloop()