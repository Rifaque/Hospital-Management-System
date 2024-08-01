import tkinter as tk
from PIL import Image, ImageTk
import registrationappointment
import LoginPage
import doneappoinment
from tkinter import ttk
import sv_ttk

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Best Medical Treatment")
        self.root.geometry("1166x718")
        #self.root.resizable(0, 0)
        self.root.state('zoomed')
        self.root.configure(bg="white")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.load_background()
        self.home_page()

    def load_background(self):
        bg_image = Image.open("images\\backroundreal.png")  # Replace with your image path
        bg_image = bg_image.resize((self.screen_width, self.screen_height), Image.BICUBIC)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self.root, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.lgn_frame = ttk.Frame(self.root, width=1140, height=720)
        self.lgn_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def home_page(self):

        self.home_frame = tk.Frame(self.lgn_frame, bg='white', width=1140, height=720)
        self.home_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        side_image = Image.open('images\\homepagev1.png')
        side_image = side_image.resize((1140, 620))
        photo = ImageTk.PhotoImage(side_image)
        side_image_label = tk.Label(self.home_frame, image=photo, bg="white")
        side_image_label.image = photo
        side_image_label.place(relx=0.49, rely=0.55, anchor=tk.CENTER)



        logo_image = Image.open("images\\hyy.png")  # Replace with your logo image path
        logo_image = logo_image.resize((100, 100))
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(self.home_frame, image=logo_photo, bg="white")
        logo_label.image = logo_photo
        logo_label.place(x=2, y=2)


        #self.create_button(self.home_frame,"REGISTER", self.open_register).place(x=450, y=500)
        self.create_button(self.home_frame,"HOME", lambda: print("Home button clicked!")).place(x=139, y=30)
        self.create_button(self.home_frame,"SERVICES", self.services_page).place(x=297, y=30)
        self.create_button(self.home_frame,"ABOUT", self.about_page).place(x=455, y=30)
        self.create_button(self.home_frame,"CONTACT US", self.contact_page).place(x=613, y=30)
        self.create_button(self.home_frame,"LOGIN", self.open_login).place(x=945, y=30)

    #def services_page_start(self):
            #self.home_frame.destroy()
            #self.services_page()

    def services_page(self):
        self.services_frame = tk.Frame(self.lgn_frame, bg='white', width=1140, height=720)
        self.services_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        side_image = Image.open('images\\servicespagev1.png')
        side_image = side_image.resize((1140, 620))
        photo = ImageTk.PhotoImage(side_image)
        side_image_label = tk.Label(self.services_frame, image=photo, bg="white")
        side_image_label.image = photo
        side_image_label.place(relx=0.49, rely=0.55, anchor=tk.CENTER)

        logo_image = Image.open("images\\hyy.png")  # Replace with your logo image path
        logo_image = logo_image.resize((100, 100))
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(self.services_frame, image=logo_photo, bg="white")
        logo_label.image = logo_photo
        logo_label.place(x=2, y=2)

        tk.Button(
            self.services_frame,
            text="REGISTER AN APPOINTMENT",
            command=self.open_register,
            width=30,
            height=20,
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#4CAF50",
            borderwidth=0,
            cursor="hand2"
        ).place(relx=0.3, rely=0.55, anchor=tk.CENTER)

        tk.Button(
            self.services_frame,
            text="DELETE AN APPOINTMENT",
            command=self.delete_register,    #make a delete appoinment feature
            width=30,
            height=20,
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#4CAF50",
            borderwidth=0,
            cursor="hand2"
        ).place(relx=0.7, rely=0.55, anchor=tk.CENTER)

        # self.create_button(self.services_frame,"REGISTER", self.open_register).place(x=450, y=500)
        self.create_button(self.services_frame, "HOME", self.home_page).place(x=139, y=30)
        self.create_button(self.services_frame, "SERVICES", lambda: print("Services button clicked!")).place(x=297, y=30)
        self.create_button(self.services_frame, "ABOUT", self.about_page).place(x=455, y=30)
        self.create_button(self.services_frame, "CONTACT US", self.contact_page).place(x=613,
                                                                                                             y=30)
        self.create_button(self.services_frame, "LOGIN", self.open_login).place(x=945, y=30)

    def about_page(self):

        self.about_frame = tk.Frame(self.lgn_frame, bg='white', width=1140, height=720)
        self.about_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        side_image = Image.open('images\\aboutpagev1.png')
        side_image = side_image.resize((1140, 620))
        photo = ImageTk.PhotoImage(side_image)
        side_image_label = tk.Label(self.about_frame, image=photo, bg="white")
        side_image_label.image = photo
        side_image_label.place(relx=0.5, rely=0.57, anchor=tk.CENTER)



        logo_image = Image.open("images\\hyy.png")  # Replace with your logo image path
        logo_image = logo_image.resize((100, 100))
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(self.about_frame, image=logo_photo, bg="white")
        logo_label.image = logo_photo
        logo_label.place(x=2, y=2)


        #self.create_button(self.about_frame,"REGISTER", self.open_register).place(x=450, y=500)
        self.create_button(self.about_frame,"HOME", self.home_page).place(x=139, y=30)
        self.create_button(self.about_frame,"SERVICES", self.services_page).place(x=297, y=30)
        self.create_button(self.about_frame,"ABOUT", lambda: print("About button clicked!")).place(x=455, y=30)
        self.create_button(self.about_frame,"CONTACT US", self.contact_page).place(x=613, y=30)
        self.create_button(self.about_frame,"LOGIN", self.open_login).place(x=945, y=30)

    def contact_page(self):

        self.contact_frame = tk.Frame(self.lgn_frame, bg='white', width=1140, height=720)
        self.contact_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        side_image = Image.open('images\\contactpagev1.png')
        side_image = side_image.resize((1140, 620))
        photo = ImageTk.PhotoImage(side_image)
        side_image_label = tk.Label(self.contact_frame, image=photo, bg="white")
        side_image_label.image = photo
        side_image_label.place(relx=0.5, rely=0.57, anchor=tk.CENTER)



        logo_image = Image.open("images\\hyy.png")  # Replace with your logo image path
        logo_image = logo_image.resize((100, 100))
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(self.contact_frame, image=logo_photo, bg="white")
        logo_label.image = logo_photo
        logo_label.place(x=2, y=2)


        #self.create_button(self.contact_frame,"REGISTER", self.open_register).place(x=450, y=500)
        self.create_button(self.contact_frame,"HOME", self.home_page).place(x=139, y=30)
        self.create_button(self.contact_frame,"SERVICES", self.services_page).place(x=297, y=30)
        self.create_button(self.contact_frame,"ABOUT", self.about_page).place(x=455, y=30)
        self.create_button(self.contact_frame,"CONTACT US", lambda: print("Contact Us button clicked!")).place(x=613, y=30)
        self.create_button(self.contact_frame,"LOGIN", self.open_login).place(x=945, y=30)


    def create_button(self, frame ,text, command):
        button = tk.Button(
            frame,
            text=text,
            command=command,
            width=15,
            height=2,
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#4CAF50",
            borderwidth=0,
            cursor="hand2"
        )
        return button

    def open_register(self):
        print("Register button clicked!")
        #self.root.destroy()
        registrationappointment.registerpage()

    def open_login(self):
        print("Login button clicked!")
        self.root.destroy()
        LoginPage.page()

    def delete_register(self):
        print("Login button clicked!")
        #self.root.destroy()
        doneappoinment.doneapp()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
