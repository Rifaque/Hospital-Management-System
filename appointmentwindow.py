import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import registrationappointment
import appointmentdetailsqlconnect
import doneappoinment

def appointmentwindow(frame):
    # Destroy all widgets in the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a new treeview
    heading_label = tk.Label(frame, text="Appointment Details", font=("Arial", 24, "bold"))
    heading_label.pack(pady=20)

    # Create a frame for the buttons
    button_frame = tk.Frame(frame)
    button_frame.pack(fill="x", pady=10)

    # Create two buttons
    btn_add_patient = ttk.Button(button_frame, text="Add", command=registrationappointment.registerpage)
    btn_add_patient.pack(side="left", padx=5)

    #btn_edit_patient = ttk.Button(button_frame, text="Edit", command=edit_appoint_callback)
    #btn_edit_patient.pack(side="left", padx=5)

    btn_edit_patient = ttk.Button(button_frame, text="done", command=done_appoint_callback)
    btn_edit_patient.pack(side="left", padx=5)

    #btn_edit_patient = ttk.Button(button_frame, text="refresh", command=refresh_appoint_callback)
    #btn_edit_patient.pack(side="left", padx=5)

    apptable_frame = tk.Frame(frame)
    apptable_frame.pack(fill="both")

    #table
    appoint_tree = ttk.Treeview(apptable_frame, columns=("pat_no","fname","lname","phonenumber","email","address","age","dateofbirth","doctor","symptons","t_o_appointment","status"), show="headings",height=30)
    appoint_tree.heading("pat_no", text="Patient ID")
    appoint_tree.heading("fname", text="First Name")
    appoint_tree.heading("lname", text="Last Name")
    appoint_tree.heading("phonenumber", text="Contact number")
    appoint_tree.heading("email", text="Email")
    appoint_tree.heading("address", text="Address")
    appoint_tree.heading("age", text="Age")
    appoint_tree.heading("dateofbirth", text="Date of birth")
    appoint_tree.heading("doctor", text="Doctor")
    appoint_tree.heading("symptons", text="Symptons")
    appoint_tree.heading("t_o_appointment", text="Time")
    appoint_tree.heading("status", text="Status")
    column_widths = {
        "pat_no": 100,
        "fname": 100,
        "lname": 100,
        "phonenumber": 100,
        "email": 100,
        "address": 100,
        "age": 100,
        "dateofbirth": 100,
        "doctor": 100,
        "symptons": 100,
        "t_o_appointment": 100,
        "status": 100
    }

    for column, width in column_widths.items():
        appoint_tree.column(column, width=width, minwidth=50, stretch=True)

    appoint_data = appointmentdetailsqlconnect.fetch_appoint_data()
    for patient in appoint_data:
        appoint_tree.insert("", tk.END, values=list(patient))

    #scroolbar
    scrollbar = tk.Scrollbar(apptable_frame, orient="vertical", command=appoint_tree.yview)
    appoint_tree.configure(yscrollcommand=scrollbar.set)

    appoint_tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")


def add_appoint_callback():
    # Code to add a new patient
    print("Add patient button clicked")


def edit_appoint_callback():
    # Code to edit an existing patient
    print("Edit patient button clicked")


def done_appoint_callback():
    # Code to edit an existing patient
    print("done patient button clicked")
    doneappoinment.doneapp()



def refresh_appoint_callback():
    # Code to edit an existing patient
    print("Edit patient button clicked")


