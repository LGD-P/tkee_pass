import os
from tkinter import filedialog, Toplevel
import ttkbootstrap as ttk
from zxcvbn import zxcvbn
from pykeepass import PyKeePass, create_database
import re
from threading import Timer

from controllers.generate_password import GeneratePassword


class CreateFile():
    def __init__(self, parent):
        # Toplevel to be able to open new window keeping style parameters
        self.root = Toplevel(parent)
        self.root.title('Create Database')
        self.root.geometry("650x320")

        # GENERATE PASSWORD BUTTON
        self.generate_password_frame = ttk.Frame(self.root)
        self.generate_password_button = ttk.Button(self.generate_password_frame, style="primary-outline",
                                                   text='Generate password', command=self.generate_password, width=19)
        self.generate_password_button.grid(row=0, column=0, padx=10, sticky="W")
        self.generate_password_frame.place(y=32, x=220)

        # FILE NAME ERROR FRAME
        self.message_frame = ttk.Frame(self.root)
        self.root.resizable(False, False)
        self.message_frame_label = ttk.Label(self.message_frame, justify='center', anchor='center',
                                             width=75)
        self.message_frame_label.grid(row=0, column=0, columnspan=2, padx=15, pady=5, sticky="W")
        self.message_frame.place(y=70)

        # FILE NAME FRAME
        self.filename_frame = ttk.Frame(self.root)
        self.filename_label = ttk.Label(self.filename_frame, text="File name", width=13)
        self.filename_entry = ttk.Entry(self.filename_frame, style='info', width=40)
        self.filename_label.grid(row=0, column=0, padx=15, sticky="W")
        self.filename_entry.grid(row=0, column=1, padx=15, sticky="W")
        self.filename_frame.place(y=120)

        # FILE PATH FRAME
        self.filepath_frame = ttk.Frame(self.root)
        self.filepath_label = ttk.Label(self.filepath_frame, text="Select a path", width=13)
        self.filepath_entry = ttk.Entry(self.filepath_frame, style="info", width=40)
        self.filepath_button = ttk.Button(self.filepath_frame, style="info-outline", text='Select',
                                          command=self.filepath_button, width=9)
        self.filepath_label.grid(row=0, column=0, padx=15, sticky="W")
        self.filepath_entry.grid(row=0, column=1, padx=15, sticky="W")
        self.filepath_button.grid(row=0, column=2, padx=15, sticky="W")
        self.filepath_frame.place(y=170)

        # PASSWORD FRAME
        self.password_frame = ttk.Frame(self.root)
        self.password_label = ttk.Label(self.password_frame, text="Enter Password", width=13)
        self.password_entry = ttk.Entry(self.password_frame, style='danger', show="*", width=40)
        self.password_entry.bind("<KeyRelease>", self.get_password_strength)  # to update each entry
        self.password_button = ttk.Button(self.password_frame, style="danger-outline", text="Ok",
                                          command=self.password_button, width=9)
        self.password_label.grid(row=0, column=0, padx=15, sticky="W")
        self.password_entry.grid(row=0, column=1, padx=15, sticky="W")
        self.password_button.grid(row=0, column=2, padx=15, sticky="W")
        self.password_frame.place(y=220)

        # PASSWORD STRENGTH MESSAGE FRAME
        self.password_strength_frame = ttk.Frame(self.root)
        self.very_weak_label = ttk.Label(self.password_strength_frame, justify='center', anchor='center',
                                         background="red", width=18)
        self.weak_label = ttk.Label(self.password_strength_frame, justify='center', anchor='center',
                                    background="red", width=18)
        self.ok_label = ttk.Label(self.password_strength_frame, justify='center', anchor='center',
                                  background="orange", width=18)
        self.good_label = ttk.Label(self.password_strength_frame, justify='center', anchor='center',
                                    background="green", width=18)
        self.password_strength_frame.place(y=250)

    def get_password_strength(self, *args, **kwargs):
        """Display strength of the input password"""
        password = self.password_entry.get()
        if len(password) > 0:
            strength = zxcvbn(password)['score']
            # print(strength)
            if strength <= 1:
                self.clear_labels()
                self.very_weak_label.configure(text="Very Weak")
                self.very_weak_label.grid(row=0, column=0, padx=5, sticky="W")
            elif strength <= 2:
                self.clear_labels()
                self.very_weak_label.configure(text="")
                self.weak_label.configure(text="Weak")
                self.very_weak_label.grid(row=0, column=0, padx=5, sticky="W")
                self.weak_label.grid(row=0, column=1, padx=5, sticky="W")
            elif strength <= 3:
                self.clear_labels()
                self.very_weak_label.configure(text="")
                self.weak_label.configure(text="")
                self.ok_label.configure(text="Good")
                self.very_weak_label.grid(row=0, column=0, padx=5, sticky="W")
                self.weak_label.grid(row=0, column=1, padx=5, sticky="W")
                self.ok_label.grid(row=0, column=2, padx=5, sticky="W")
            elif strength > 3:
                self.clear_labels()
                self.very_weak_label.configure(text="")
                self.weak_label.configure(text="")
                self.ok_label.configure(text="")
                self.good_label.configure(text="Strong")
                self.very_weak_label.grid(row=0, column=0, padx=5, sticky="W")
                self.weak_label.grid(row=0, column=1, padx=5, sticky="W")
                self.ok_label.grid(row=0, column=2, padx=5, sticky="W")
                self.good_label.grid(row=0, column=3, padx=5, sticky="W")
        else:
            pass

    def clear_labels(self):
        """Clear all labels before updating"""
        for label in [self.very_weak_label, self.weak_label, self.ok_label, self.good_label]:
            label.grid_forget()

    def filepath_button(self):
        """Ask user to choose a directory to register file"""
        path = filedialog.askdirectory()
        self.filepath_entry.delete(0, "end")
        self.filepath_entry.insert(0, path)
        return path

    def is_valid_filename(self, filename):
        pattern = r'^[a-zA-Z0-9_\-\.]+$'
        return re.match(pattern, filename) is not None

    def hide_message(self):
        return self.message_frame_label.configure(text="", background="black")

    def is_file_ready_to_save(self, filename, path, password):
        """ Check that every parameter for file creation is completed, else return error message & False
        """
        if self.is_valid_filename(filename) is False or filename == "":
            self.message_frame_label.configure(text="File name needed - No Space & No Special characters "
                                                    "allowed in your filename", foreground="red")
            Timer(5.0, self.hide_message).start()
            return False

        elif path == "":
            self.message_frame_label.configure(text="Please select a path to your file",
                                               foreground="red")
            Timer(5.0, self.hide_message).start()
            return False

        elif password == "":
            self.message_frame_label.configure(text="Please enter a strong password - prefer it strong",
                                               foreground="red")
            Timer(5.0, self.hide_message).start()
            return False
        else:
            return True

    def password_button(self):
        """Create kdbx file"""
        password = self.password_entry.get()
        filename = self.filename_entry.get()
        path = self.filepath_entry.get()

        filename_with_extension = f"{filename}.kdbx"
        file_path = os.path.join(path, filename_with_extension)

        if self.is_file_ready_to_save(filename, path, password) is True:
            file = create_database(file_path, password=password, keyfile=None, transformed_key=None)
            file.save()
            self.message_frame_label.configure(text="File created", foreground="green")
            Timer(5.0, self.hide_message).start()

    def generate_password(self):
        """Open new window to create_db form"""
        generate_pass = GeneratePassword(self.root)
        generate_pass.run()


    def run(self):
        self.root.mainloop()
