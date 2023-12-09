from tkinter import filedialog, Toplevel
import ttkbootstrap as ttk
from zxcvbn import zxcvbn
from pykeepass import PyKeePass


class CreateFile():
    def __init__(self, parent):
        # Toplevel to be able to open new window with keeping style parameters
        self.root = Toplevel(parent)
        self.root.title('Create Database')
        self.geometry = self.root.geometry("650x300")

        # FILE NAME FRAM TO COME

        # FILE PATH FRAME
        self.filepath_frame = ttk.Frame(self.root)
        self.filepath_label = ttk.Label(self.filepath_frame, text="Select a path", width=13)
        self.filepath_entry = ttk.Entry(self.filepath_frame, style="info", width=40)
        self.filepath_button = ttk.Button(self.filepath_frame, style="info-outline", text='Select',
                                          command=self.filepath_button, width=9)
        self.filepath_label.grid(row=0, column=0, padx=15, sticky="W")
        self.filepath_entry.grid(row=0, column=1, padx=15, sticky="W")
        self.filepath_button.grid(row=0, column=2, padx=15, sticky="W")
        self.filepath_frame.place(y=100)

        # PASSWORD FRAME
        self.password_frame = ttk.Frame(self.root)
        self.password_label = ttk.Label(self.password_frame, text="Enter Password", width=13)
        self.password_entry = ttk.Entry(self.password_frame, style='danger', show='*', width=40)
        self.password_entry.bind("<Key>", self.get_password_strength) # to update each entry
        self.password_button = ttk.Button(self.password_frame, style="danger-outline", text="Ok",
                                          command=self.password_button, width=9)
        self.password_label.grid(row=0, column=0, padx=15, sticky="W")
        self.password_entry.grid(row=0, column=1, padx=15, sticky="W")
        self.password_button.grid(row=0, column=2, padx=15, sticky="W")
        self.password_frame.place(y=150)

        # PASSWORD STRENGTH MESSAGE FRAME
        self.password_strength_frame = ttk.Frame(self.root)
        self.very_week_label = ttk.Label(self.password_strength_frame, justify='center', anchor='center',
                                         background="red", text='very week', width=18)
        self.week_label = ttk.Label(self.password_strength_frame, justify='center', anchor='center',
                                    background="red", text='week', width=18)
        self.ok_label = ttk.Label(self.password_strength_frame, justify='center', anchor='center',
                                  background="orange", text='ok', width=18)
        self.good_label = ttk.Label(self.password_strength_frame, justify='center', anchor='center',
                                    background="green", text='good', width=18)
        self.very_week_label.grid(row=0, column=0, padx=5, sticky="W")
        self.week_label.grid(row=0, column=1, padx=5, sticky="W")
        self.ok_label.grid(row=0, column=2, padx=5, sticky="W")
        self.good_label.grid(row=0, column=3, padx=5, sticky="W")

        self.password_strength_frame.place(y=200)

    def get_password_strength(self, *args, **kwargs):
        password = self.password_entry.get()
        strength = zxcvbn(password)['score']
        print(strength)
        return strength

    def filepath_button(self):
        """Ask user to choose a directory to register file"""
        path = filedialog.askdirectory()
        self.filepath_entry.delete(0, "end")
        self.filepath_entry.insert(0, path)
        return path

    def password_button(self):
        """Register and check strength"""
        password = self.password_entry.get()
        print(password)
        #
        return password

    def run(self):
        self.root.mainloop()
