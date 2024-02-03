import os
import random
import string
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

        self.generate_passphrase_labelframe = ttk.Labelframe(self.root, text='Pass-phrase', style='info', padding=10)
        self.generate_passphrase_labelframe.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="W")
        # self.generate_passphrase_labelframe.pack(side="top", padx=10, pady=10, fill="both")

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
                                                   text='Generate Passphrase', command=self.pass_phrase, width=18)
        self.generate_passphrase_button.grid(row=0, column=4, padx=10, sticky="W")

        self.pass_phrase_result_frame = ttk.Entry(self.generate_passphrase_labelframe, style='success', width=70)

        # Add a dummy column at the end of row 0 to expand the Entry.
        self.generate_passphrase_labelframe.grid_columnconfigure(5, weight=1)

        # Add the Entry widget to column 5 (the dummy column) and use columnspan to cover all the previous columns.
        self.pass_phrase_result_frame.grid(row=1, padx=10,pady=(10, 0), sticky="W", columnspan=5)


        # GENERATE COMPLEX PASSWORD:
        # option Upper Lower Special Number of char'
        self.generate_password_labelframe = ttk.Labelframe(self.root, text='Complex Password', style='info',
                                                           padding=10)
        self.generate_password_labelframe.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="W")
        # self.generate_password_labelframe.pack(side="top", padx=10, pady=10, fill="both")

        # Upper
        self.checkbutton_lowercase_var = ttk.IntVar(value=0)
        self.radio_lowercase = ttk.Checkbutton(self.generate_password_labelframe, text='a-z',
                                               style='default',
                                               variable=self.checkbutton_lowercase_var)
        self.radio_lowercase.grid(row=0, column=0, padx=10, sticky="W")

        # Lower
        self.checkbutton_uppercase_var = ttk.IntVar(value=0)
        self.radio_uppercase = ttk.Checkbutton(self.generate_password_labelframe, text='A-Z',
                                               style='default',
                                               variable=self.checkbutton_uppercase_var)
        self.radio_uppercase.grid(row=0, column=1, padx=10, sticky="W")

        # Spécial
        self.checkbutton_special_chars_var = ttk.IntVar(value=0)
        #'!@#$%^&'
        self.radio_special_chars = ttk.Checkbutton(self.generate_password_labelframe, text='!@#$..',
                                                   style='default',
                                                   variable=self.checkbutton_special_chars_var)
        self.radio_special_chars.grid(row=0, column=2, padx=10, sticky="W")

        # Number
        self.checkbutton_number_chars_var = ttk.IntVar(value=0)
        self.radio_number_chars = ttk.Checkbutton(self.generate_password_labelframe, text='0-9',
                                                   style='default',
                                                   variable=self.checkbutton_number_chars_var)
        self.radio_number_chars.grid(row=0, column=3, padx=10, sticky="W")

        # Number of char
        self.spin_number_of_chars_var = ttk.IntVar(value=0)
        self.spin_number_of_chars = ttk.Spinbox(self.generate_password_labelframe, from_=1, to=100, increment=1,
                                                textvariable=self.spin_number_of_chars_var, width=3)
        self.spin_number_of_chars.grid(row=0, column=4, padx=10, sticky="W")

        # Bouton pour générer le mot de passe complexe
        self.generate_password_button = ttk.Button(self.generate_password_labelframe, style="primary-outline",
                                                   text='Complex Password', command=self.complex_password, width=18)
        self.generate_password_button.grid(row=0, column=5, padx=10, sticky="W")


        # Add a dummy column at the end of row 0 to expand the Entry.
        self.generate_password_labelframe.grid_columnconfigure(5, weight=1)

        self.password_result_frame = ttk.Entry(self.generate_password_labelframe, style='success', width=70)
        self.password_result_frame.grid(row=1, padx=10, pady=(10, 0), sticky="W", columnspan=6)



    def pass_phrase_choices(self,separator=0, capitalize=0, add_numbers=0, number_of_words=0):
        """generate passphrase regarding user choice"""
        fake = Faker()
        words = fake.words(nb=int(number_of_words))

        if capitalize:
            words = [word.capitalize() for word in words]

        if add_numbers:
            words = [word + str(random.randint(0, 9)) for word in words]

        passphrase = "".join(words)

        if separator:
            passphrase = "-".join(words)
        return passphrase

    def complex_password_choice(self,lowercase=0, uppercase=0, special_chars=0, numbers=0, number_of_char=0):
        """
        generate a complex password regarding user choice.
        """
        options = []
        if lowercase:
            options += string.ascii_lowercase
        if uppercase:
            options += string.ascii_uppercase
        if special_chars:
            options += "#?!@$%^&*-"
        if numbers:
            options += string.digits

        password = ''.join(random.choice(options) for _ in range(number_of_char))

        return password

    def pass_phrase(self):
        self.pass_phrase_result_frame.delete(0, 'end')
        separator = self.checkbutton_separator_var.get()
        capitalize = self.checkbutton_capitalize_var.get()
        number = self.checkbutton_number_var.get()
        number_of_words = self.spin_number_of_words_var.get()
        result = self.pass_phrase_choices(separator,capitalize,number,number_of_words)
        return self.pass_phrase_result_frame.insert(0,result)

    def complex_password(self):
        self.password_result_frame.delete(0,'end')
        lower = self.checkbutton_lowercase_var.get()
        upper = self.checkbutton_uppercase_var.get()
        special = self.checkbutton_special_chars_var.get()
        number = self.checkbutton_number_chars_var.get()
        number_of_char = self.spin_number_of_chars_var.get()
        result = self.complex_password_choice(lower,upper,special,number,number_of_char)
        return self.password_result_frame.insert(0,result)

    def run(self):
        self.root.mainloop()


