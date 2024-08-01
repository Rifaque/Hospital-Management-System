import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import docdetailsqlconnect
import add_doc

def docdetail(frame):
    # Destroy all widgets in the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a new treeview
    heading_label = tk.Label(frame, text="Doctor Details", font=("Arial", 24, "bold"))
    heading_label.pack(pady=20)

    # Create a frame for the buttons
    button_frame = tk.Frame(frame)
    button_frame.pack(fill="x", pady=10)

    # Create two buttons
    btn_add_patient = ttk.Button(button_frame, text="Add", command=add_doctor_callback)
    btn_add_patient.pack(side="left", padx=5)

    #btn_edit_patient = ttk.Button(button_frame, text="delete", command=refresh_doc_callback)
    #btn_edit_patient.pack(side="left", padx=5)

    doctable_frame = tk.Frame(frame)
    doctable_frame.pack(fill="both")

    #table
    doc_tree = ttk.Treeview(doctable_frame, columns=("Doctor_ID ","fname","lname","Specialization","Qualifications",
                                                         "Experience","Hospital_ID","Department","Room_No","Phone_No",
                                                         "Email","Address"), show="headings",height=30)
    doc_tree.heading("Doctor_ID ", text="Doctor ID")
    doc_tree.heading("fname", text="First Name")
    doc_tree.heading("lname", text="Last Name")
    doc_tree.heading("Specialization", text="Specialization")
    doc_tree.heading("Qualifications", text="Qualifications")
    doc_tree.heading("Experience", text="Experience")
    doc_tree.heading("Hospital_ID", text="Hospital_ID")
    doc_tree.heading("Department", text="Department")
    doc_tree.heading("Room_No", text="Room_No")
    doc_tree.heading("Phone_No", text="Phone_No")
    doc_tree.heading("Email", text="Email")
    doc_tree.heading("Address", text="Address")
    column_widths = {
        "Doctor_ID ": 100,
        "fname": 100,
        "lname": 100,
        "Specialization": 100,
        "Qualifications": 100,
        "Experience": 100,
        "Hospital_ID": 100,
        "Department": 100,
        "Room_No": 100,
        "Phone_No": 100,
        "Email": 100,
        "Address": 100
    }

    for column, width in column_widths.items():
        doc_tree.column(column, width=width, minwidth=50, stretch=True)

    doc_data = docdetailsqlconnect.fetch_doc_data()
    for doctor in doc_data:
        doc_tree.insert("", tk.END, values=list(doctor))

    #scroolbar
    scrollbar = tk.Scrollbar(doctable_frame, orient="vertical", command=doc_tree.yview)
    doc_tree.configure(yscrollcommand=scrollbar.set)

    doc_tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")


def add_doctor_callback():
    # Code to add a new patient
    print("Add patient button clicked")
    add_doc.docinsertrun()


def refresh_doc_callback():
    # Code to edit an existing patient
    print("Edit patient button clicked")


