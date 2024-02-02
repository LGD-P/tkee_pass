import os
from tkinter import Toplevel
import ttkbootstrap as ttk
from faker import Faker
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
            # option Capitalize Number Sperator Number of words

        self.generate_passphrase_labelframe = ttk.Labelframe(self.root, text='Pass-phrase', style='primary', padding=10)
        self.generate_passphrase_labelframe.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="W")
        self.generate_passphrase_labelframe.pack(side="top", padx=10, pady=10, fill="both")

        # separator box
        self.checkbutton_separator_var = ttk.IntVar(value=0)
        self.radio_separator = ttk.Checkbutton(self.generate_passphrase_labelframe,text='Separator', style='default',
                                               variable=self.checkbutton_separator_var)
        self.radio_separator.grid(row=0, column=0, padx=10, sticky="W")

        # capitalize box
        self.checkbutton_capitalize_var = ttk.IntVar(value=0)
        self.radio_capitalize = ttk.Checkbutton(self.generate_passphrase_labelframe,text='Capitalize', style='default',
                                                variable=self.checkbutton_capitalize_var)
        self.radio_capitalize.grid(row=0, column=1, padx=10, sticky="W")

        # number box
        self.checkbutton_number_var = ttk.IntVar(value=0)
        self.radio_number = ttk.Checkbutton(self.generate_passphrase_labelframe,text='Number', style='default',
                                            variable=self.checkbutton_number_var)
        self.radio_number.grid(row=0, column=2, padx=10, sticky="W")

        # number of words
        self.spin_number_of_words_var=ttk.IntVar(value=0)
        self.spin_number_of_words = ttk.Spinbox(self.generate_passphrase_labelframe, from_=1, to=100, increment=1,
                                                textvariable=self.spin_number_of_words_var, width=3)
        self.spin_number_of_words.grid(row=0, column=3, padx=10, sticky="W")

        # label to display result
        self.generate_passphrase_button = ttk.Button(self.generate_passphrase_labelframe, style="primary-outline",
                                                   text='Generate Passphrase', command=self.get_values, width=18)
        self.generate_passphrase_button.grid(row=0, column=4, padx=10, sticky="W")


        self.pass_phrase_result_frame = ttk.Entry(self.generate_passphrase_labelframe, style='success', width=70)

        # Add a dummy column at the end of row 0 to expand the Entry.
        self.generate_passphrase_labelframe.grid_columnconfigure(4, weight=1)

        # Add the Entry widget to column 5 (the dummy column) and use columnspan to cover all the previous columns.
        self.pass_phrase_result_frame.grid(row=1, padx=10,pady=(10, 0), sticky="W", columnspan=5)

    # GENERATE COMPLEXE PASSWORD
    def get_values(self):
        separator = self.checkbutton_separator_var.get()
        capitalize = self.checkbutton_capitalize_var.get()
        number = self.checkbutton_number_var.get()
        number_of_words = self.spin_number_of_words_var.get()

        fake = Faker()
        passphrase = "".join(fake.words(nb=int(number_of_words)))
        return self.pass_phrase_result_frame.insert(0, passphrase)





    def run(self):
        self.root.mainloop()


