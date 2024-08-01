import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import patdetailssqlconnect
import addpatient

def patwindow(frame):
    #if already exist
    for widget in frame.winfo_children():
        if isinstance(widget, ttk.Treeview):
            widget.destroy()

    # Create a new treeview
    heading_label = tk.Label(frame, text="Patient Database", font=("Arial", 24, "bold"))
    heading_label.pack(pady=20)

    # Create a frame for the buttons
    button_frame = tk.Frame(frame)
    button_frame.pack(fill="x", pady=10)

    # Create two buttons
    btn_add_patient = ttk.Button(button_frame, text="Add Patient", command=addpatient.patpage)
    btn_add_patient.pack(side="left", padx=5)

    #btn_edit_patient = ttk.Button(button_frame, text="Edit Patient", command=edit_patient_callback)
    #btn_edit_patient.pack(side="left", padx=5)

    table_frame = tk.Frame(frame)
    table_frame.pack(fill="both")

    #table
    patients_tree = ttk.Treeview(table_frame,columns=("pat_no","fname","lname","phonenumber","email","address","age","dateofbirth", "blood", "doctor"),show="headings", height=30)
    patients_tree.heading("pat_no", text="Patient ID")
    patients_tree.heading("fname", text="First Name")
    patients_tree.heading("lname", text="Last Name")
    patients_tree.heading("phonenumber", text="Contact number")
    patients_tree.heading("email", text="Email")
    patients_tree.heading("address", text="Address")
    patients_tree.heading("age", text="Age")
    patients_tree.heading("dateofbirth", text="Date of birth")
    patients_tree.heading("blood", text="Blood group")
    patients_tree.heading("doctor", text="Doctor")
    column_widths = {
        "pat_no": 100,
        "fname": 100,
        "lname": 100,
        "phonenumber": 100,
        "email": 100,
        "address": 100,
        "age": 100,
        "dateofbirth": 100,
        "blood": 100,
        "doctor": 100
    }

    for column, width in column_widths.items():
        patients_tree.column(column, width=width, minwidth=50, stretch=True)

    patients_data = patdetailssqlconnect.fetch_patients_data()
    for patient in patients_data:
        patients_tree.insert("", tk.END, values=list(patient))

    #sroolbar
    scrollbar = tk.Scrollbar(table_frame, orient="vertical", command=patients_tree.yview)
    patients_tree.configure(yscrollcommand=scrollbar.set)

    patients_tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    patients_tree.pack()




def add_patient_callback():
    # Code to add a new patient
    print("Add patient button clicked")


def edit_patient_callback():
    # Code to edit an existing patient
    print("Edit patient button clicked")