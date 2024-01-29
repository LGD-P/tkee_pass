import os
from tkinter import Toplevel
import ttkbootstrap as ttk
from zxcvbn import zxcvbn
from pykeepass import PyKeePass, create_database
import re
from threading import Timer


class GeneratePassword():
    def __init__(self, parent):
        # Toplevel to be able to open new window keeping style parameters
        self.root = Toplevel(parent)
        self.root.title('Generate Password')
        self.root.geometry("650x320")

        # GENERATE PASSPHRASE
            # option Capitalize Number Sperator

        self.generate_passphrase_labelframe = ttk.Labelframe(self.root, text='Pass-phrase', style='primary')
        self.generate_passphrase_labelframe.grid(row=0, column=0, padx=10, sticky="W")
        self.generate_passphrase_labelframe.pack(side="top", padx=10, pady=10, fill="both", expand=True)

        # GENERATE COMPLEXE PASSWORD


    def run(self):
        self.root.mainloop()


