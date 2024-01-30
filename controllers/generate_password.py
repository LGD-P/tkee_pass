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
            # option Capitalize Number Sperator Number of words

        self.generate_passphrase_labelframe = ttk.Labelframe(self.root, text='Pass-phrase', style='primary', padding=10)
        self.generate_passphrase_labelframe.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="W")
        self.generate_passphrase_labelframe.pack(side="top", padx=10, pady=10, fill="both")


        self.checkbutton_separator_var = ttk.IntVar(value=0)
        self.radio_separator = ttk.Checkbutton(self.generate_passphrase_labelframe,text='Separator', style='default',
                                               variable=self.checkbutton_separator_var)
        self.radio_separator.grid(row=0, column=0, padx=10, sticky="W")

        self.checkbutton_capitalize_var = ttk.IntVar(value=0)
        self.radio_capitalize = ttk.Checkbutton(self.generate_passphrase_labelframe,text='Capitalize', style='default',
                                                variable=self.checkbutton_capitalize_var)
        self.radio_capitalize.grid(row=0, column=1, padx=10, sticky="W")

        self.checkbutton_number_var = ttk.IntVar(value=0)
        self.radio_number = ttk.Checkbutton(self.generate_passphrase_labelframe,text='Number', style='default',
                                            variable=self.checkbutton_number_var)
        self.radio_number.grid(row=0, column=2, padx=10, sticky="W")

        self.spin_number_of_words_var=ttk.IntVar(value=0)
        self.spin_number_of_words = ttk.Spinbox(self.generate_passphrase_labelframe, from_=1, to=100, increment=1,
                                                textvariable=self.spin_number_of_words_var, width=3)
        self.spin_number_of_words.grid(row=0, column=3, padx=10, sticky="W")

        self.generate_passphrase_button = ttk.Button(self.generate_passphrase_labelframe, style="primary-outline",
                                                   text='Generate Passphrase', command=None, width=18)
        self.generate_passphrase_button.grid(row=0, column=4, padx=10, sticky="W")


        self.pass_phrase_result_frame = ttk.Entry(self.generate_passphrase_labelframe, style='success', width=70)
        # Ajoutez une colonne factice à la fin de la ligne 0 pour étendre l'Entry
        self.generate_passphrase_labelframe.grid_columnconfigure(4, weight=1)

        # Ajoutez le widget Entry à la colonne 5 (la colonne factice) et utilisez columnspan pour couvrir toutes les colonnes précédentes
        self.pass_phrase_result_frame.grid(row=1, padx=10,pady=(10, 0), sticky="W", columnspan=5)

        # GENERATE COMPLEXE PASSWORD


    def run(self):
        self.root.mainloop()


