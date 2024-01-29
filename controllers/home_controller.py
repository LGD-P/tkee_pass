from pathlib import Path
from tkinter import filedialog
from tkinter.ttk import Entry, Button
import ttkbootstrap as ttk
from pykeepass import PyKeePass

from controllers.new_db_file_controller import CreateFile

class OpenFile():
    def __init__(self):
        self.root = ttk.Window(themename='cyborg')
        self.root.resizable(False, False)
        self.root.geometry("650x300")

        # FILE PATH FRAME
        self.filepath_frame = ttk.Frame(self.root)
        self.filepath_label = ttk.Label(self.filepath_frame, text="Select a file", width=10)
        self.filepath_entry = Entry(self.filepath_frame, style="info", width=40)
        self.filepath_button = Button(self.filepath_frame, style="info-outline", text='Select',
                                      command=self.filepath_button, width=9)
        self.filepath_label.grid(row=0, column=0, padx=20, sticky="W")
        self.filepath_entry.grid(row=0, column=1, padx=20, sticky="W")
        self.filepath_button.grid(row=0, column=2, padx=20, sticky="W")
        self.filepath_frame.place(y=100)

        # PASSWORD FRAME
        self.password_frame = ttk.Frame(self.root)
        self.password_label = ttk.Label(self.password_frame, text="Password",width=10)
        self.password_entry = Entry(self.password_frame, style='danger', show='*', width=40)
        self.password_button = Button(self.password_frame, style="danger-outline", text="Ok",
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
        self.new_file_button = Button(self.new_file_frame, style='succes',
                                      text="Create a new database for your passwords", command=self.create_new_db, width=73)
        self.new_file_button.grid(row=0, column=0, padx=20, sticky="W")
        self.new_file_frame.grid(row=0, column=0, padx=20)
        self.new_file_frame.place(y=235)

    def filepath_button(self):
        """Get file path & check .kdbx format"""
        path = filedialog.askopenfilename()
        if not Path(path).suffix == ".kdbx":
            return self.wrong_password_label.config(text='Please select a .kdbx file')

        self.filepath_entry.delete(0, "end")
        self.filepath_entry.insert(0, path)
        return path

    def password_button(self):
        """Check Password & if OK return entries"""
        password = self.password_entry.get()
        if password == "":
            return self.wrong_password_label.config(text='Enter a password')

        db_path = self.filepath_entry.get()
        if not db_path or not Path(db_path).exists():
            return self.wrong_password_label.config(text='Select a file first')

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

    def create_new_db(self):
        """Open new window to create_db form"""
        create_db = CreateFile(self.root)
        create_db.run()

    def run(self):
        self.root.mainloop()
