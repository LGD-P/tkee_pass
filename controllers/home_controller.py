from pathlib import Path
from tkinter import filedialog
from tkinter.ttk import Entry, Button
import ttkbootstrap as ttk
from pykeepass import PyKeePass


class OpenFile():
    def __init__(self):
        self.root = ttk.Window(themename='darkly')
        self.geometry = self.root.geometry("650x300")

        # FILE PATH FRAME
        self.filepath_frame = ttk.Frame(self.root)
        self.filepath_label = ttk.Label(self.filepath_frame, text="Select a file", width=10)
        self.filepath_entry = Entry(self.filepath_frame,bootstyle="info", width=40)
        self.filepath_button = Button(self.filepath_frame,bootstyle="info-outline", text='Select',
                                      command=self.filepath_button, width=9)
        self.filepath_label.grid(row=0, column=0, padx=20, sticky="W")
        self.filepath_entry.grid(row=0, column=1, padx=20, sticky="W")
        self.filepath_button.grid(row=0, column=2, padx=20, sticky="W")
        self.filepath_frame.place(y=100)

        # PASSWORD FRAME
        self.password_frame = ttk.Frame(self.root)
        self.password_label = ttk.Label(self.password_frame, text="Password",width=10)
        self.password_entry = Entry(self.password_frame, bootstyle='danger', show='*', width=40)
        self.password_button = Button(self.password_frame, bootstyle="danger-outline", text="Ok",
                                      command=self.password_button, width=9)
        self.password_label.grid(row=0, column=0, padx=20, sticky="W")
        self.password_entry.grid(row=0, column=1, padx=20, sticky="W")
        self.password_button.grid(row=0, column=2, padx=20, sticky="W")
        self.password_frame.place(y=150)


        # ERROR MESSAGE FRAME
        self.wrong_password_frame = ttk.Frame(self.root)
        self.wrong_password_label = ttk.Label(self.wrong_password_frame, justify='center',anchor='center',
                                              foreground="red", width=73)
        self.wrong_password_label.grid(row=0, column=1, padx=20)
        self.wrong_password_frame.place(y=200)


        # NEW FILE FRAME
        self.new_file_frame = ttk.Frame(self.root)
        self.new_file_button = Button(self.new_file_frame, bootstyle='succes',
                                      text="Create a new database for your passwords", command=None, width=73)
        self.new_file_button.grid(row=0, column=0, padx=20, sticky="W")
        self.new_file_frame.grid(row=0, column=0, padx=20)
        self.new_file_frame.place(y=235)

    def filepath_button(self):
        path = filedialog.askopenfilename()
        self.filepath_entry.delete(0, "end")
        self.filepath_entry.insert(0, path)
        return path

    def read_entries(self, entries):
        for k,v in entries:
            print(f"{k.upper} : {v}")

    def password_button(self):
        password = self.password_entry.get()
        if password == "":
            return self.wrong_password_label.config(text='Enter a password')

        db_path = self.filepath_entry.get()
        if not db_path or not Path(db_path).exists():
            return self.wrong_password_label.config(text='Select a file first')

        if not Path(db_path).suffix == ".kdbx":
            return self.wrong_password_label.config(text='Please select a .kdbx file')

        try:
            kp = PyKeePass(self.filepath_entry.get(), password=password)
            entries = kp.entries
            # print("ENTRIE TTTLE : ", entries[0].title)
            # print("USER NAME : ", entries[0].username)
            # print("PASSWORD : ", entries[0].password)
            # print("URL : ",entries[0].url)
            return entries

        except Exception as e:
            self.wrong_password_label.config(text='Wrong Password try again')
            raise e

    def run(self):
        self.root.mainloop()

