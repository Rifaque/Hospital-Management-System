import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import patientswindow
import appointmentwindow
import docwindow
class SidebarMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Sidebar Menu")
        self.root.geometry("800x600")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.window_width = self.screen_width
        self.window_height = self.screen_height
        self.root.state('zoomed')

        # Create sidebar frame
        self.sidebar_frame = tk.Frame(self.root, width=200, bg="#73FBFD")
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Load icon image
        try:
            self.icon_image = Image.open("images/UNSHRINK.png")
            self.icon_image = self.icon_image.resize((199, 85))
            self.icon_image = ImageTk.PhotoImage(self.icon_image)
        except FileNotFoundError:
            print("Error: Icon image not found.")
            self.icon_image = None
        except Exception as e:
            print("Error: Unable to load icon image.")
            print(str(e))
            self.icon_image = None

        # Create icon label
        if self.icon_image:
            self.icon_label = tk.Label(self.sidebar_frame, image=self.icon_image, bg="#333")
            self.icon_label.image = self.icon_image
            self.icon_label.pack(fill=tk.X)
        else:
            self.icon_label = tk.Label(self.sidebar_frame, text="Icon", bg="#333")
            self.icon_label.pack(fill=tk.X)

        # Create menu buttons
        self.menu_buttons = self.create_menu_buttons()

        # Bind leave event to sidebar frame
        self.sidebar_frame.bind("<Leave>", self.shrink_sidebar)

        # Bind enter event to sidebar frame
        self.sidebar_frame.bind("<Enter>", self.expand_sidebar)

        # Initial state
        self.sidebar_expanded = True

        # Create frames for each menu button
        self.home_frame = tk.Frame(self.main_frame, bg="#ddd")
        self.doctors_frame = tk.Frame(self.main_frame, bg="#ddd")
        self.patients_frame = tk.Frame(self.main_frame, bg="#ddd")
        self.appointments_frame = tk.Frame(self.main_frame, bg="#ddd")
        #self.medicines_frame = tk.Frame(self.main_frame, bg="#ddd")

        # Hide all frames except home frame
        self.doctors_frame.pack_forget()
        self.patients_frame.pack_forget()
        self.appointments_frame.pack_forget()
        #self.medicines_frame.pack_forget()

        # Show home frame
        self.home_frame.pack(fill=tk.BOTH, expand=True)
        image = Image.open("images/homepagev1.png")
        image = image.resize((1500, 800))  # Resize the image to 200x200 pixels
        image = ImageTk.PhotoImage(image)
        image_label = tk.Label(self.home_frame, image=image)
        image_label.image = image  # Keep a reference to the image
        image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create a treeview for patients
        #self.patients_tree = None
        #self.show_patients()

    def create_menu_buttons(self):
        menu_buttons = []
        labels = ["Home", "Doctors", "Patients", "Appointments"]
        for i, label in enumerate(labels):
            btn = tk.Button(self.sidebar_frame, text=label, command=lambda i=i: self.show_menu(i))
            btn.pack(fill=tk.X)
            menu_buttons.append(btn)
        return menu_buttons

    def show_menu(self, index):
        labels = ["Home", "Doctors", "Patients", "Appointments"]
        if labels[index] == "Home":
            self.show_home()
        elif labels[index] == "Doctors":
            self.show_doctors()
        elif labels[index] == "Patients":
            self.show_patients()
        elif labels[index] == "Appointments":
            self.show_appointments()

    def show_home(self):
        # Hide all frames
        self.doctors_frame.pack_forget()
        self.patients_frame.pack_forget()
        self.appointments_frame.pack_forget()
        #self.medicines_frame.pack_forget()
        #background_image = tk.PhotoImage(file="images/homepagev1.png")
        # Show home frame
        self.home_frame.pack(fill=tk.BOTH, expand=True)
        if not self.home_frame.winfo_children():
            # Create a Label with the image
            image = Image.open("images/homepagev1.png")
            image = image.resize((1500, 800))  # Resize the image to 200x200 pixels
            image = ImageTk.PhotoImage(image)
            image_label = tk.Label(self.home_frame, image=image)
            image_label.image = image  # Keep a reference to the image
            image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    def show_doctors(self):
        # Hide all frames
        self.home_frame.pack_forget()
        self.patients_frame.pack_forget()
        self.appointments_frame.pack_forget()
        #self.medicines_frame.pack_forget()

        # Show doctors frame
        self.doctors_frame.pack(fill=tk.BOTH, expand=True)
        if not self.patients_frame.winfo_children():
            docwindow.docdetail(self.doctors_frame)


    def show_patients(self):
        # Hide all frames
        self.home_frame.pack_forget()
        self.doctors_frame.pack_forget()
        self.appointments_frame.pack_forget()
        #self.medicines_frame.pack_forget()

        # Show patients frame
        self.patients_frame.pack(fill=tk.BOTH, expand=True, )
        if not self.patients_frame.winfo_children():
            patientswindow.patwindow(self.patients_frame)

    def show_appointments(self):
        # Hide all frames
        self.home_frame.pack_forget()
        self.doctors_frame.pack_forget()
        self.patients_frame.pack_forget()
        #self.medicines_frame.pack_forget()

        # Show appointments frame
        self.appointments_frame.pack(fill=tk.BOTH, expand=True)
        if not self.appointments_frame.winfo_children():
            appointmentwindow.appointmentwindow(self.appointments_frame)


    def show_medicines(self):
        # Hide all frames
        self.home_frame.pack_forget()
        self.doctors_frame.pack_forget()
        self.patients_frame.pack_forget()
        self.appointments_frame.pack_forget()

        # Show medicines frame
        #self.medicines_frame.pack(fill=tk.BOTH, expand=True)

    def shrink_sidebar(self, event):
        if self.sidebar_expanded:
            self.sidebar_frame.config(width=70)
            for btn in self.menu_buttons:
                btn.pack_forget()
            if self.icon_image:
                img = Image.open("images/hyy.png")
                img = img.resize((50, 50))
                self.icon_image = ImageTk.PhotoImage(img)
                self.icon_label.config(image=self.icon_image)

            self.sidebar_expanded = False

    def expand_sidebar(self, event=None):
        if not self.sidebar_expanded:
            self.sidebar_frame.config(width=200)
            for i, btn in enumerate(self.menu_buttons):
                btn.pack(fill=tk.X)
                btn.config(text=["Home", "Doctors", "Patients", "Appointments", "Medicines"][i])
            if self.icon_image:
                img = Image.open("images/UNSHRINK.png")
                img = img.resize((199, 85))
                self.icon_image = ImageTk.PhotoImage(img)
                self.icon_label.config(image=self.icon_image)
            self.sidebar_expanded = True


def run():
    root = tk.Tk()
    app = SidebarMenu(root)
    root.mainloop()


if __name__ == "__main__":
    run()