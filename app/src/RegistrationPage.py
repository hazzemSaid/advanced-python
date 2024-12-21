import tkinter as tk
from tkinter import messagebox
import re
from classes.Account import Account
from classes.User import User, Gender
from utils import PlaceholderEntry, create_left_panel
import sqlite3
con = sqlite3.connect('app/database/project.db')
c = con.cursor()

class RegistrationPage:
    def __init__(self, root, switch_to_login, switch_to_account):
        self.root = root
        self.switch_to_login = switch_to_login
        self.switch_to_account = switch_to_account
        self.registration_frame = None
        self.entries = {}
        self.agree_var = None

    def create_page(self):
        # Create root frame for registration
        registration_page = tk.Frame(self.root, bg="#E5E5E5")
        registration_page.grid(row=0, column=0, sticky="nsew")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Left Panel
        left_frame = create_left_panel(
            registration_page,
            "Register Now",
            "app/assets/register.png",
            "Secure and easy banking experience.\nRegister now to explore more features.",
        )

        # Right Panel (Registration Form)
        right_frame = tk.Frame(registration_page, bg="#EEEEEE", width=450)
        right_frame.grid(row=0, column=1, sticky="nsew")
        registration_page.grid_columnconfigure(1, weight=1)

        title_label = tk.Label(
            right_frame,
            text="Create Account",
            font=("Helvetica", 16),
            bg="#EEEEEE"
        )
        title_label.grid(row=0, column=0, pady=20)

        # Registration Fields
        reg_fields = [
            ("Enter Name", "Name"),
            ("Username", "Username"),
            ("Your Email", "Email"),
            ("Phone Number", "Phone"),
            ("Password", "Password"),
            ("Confirm Password", "Confirm Password"),
        ]
        entries = {}
        
        # Place fields using grid
        for idx, (label_text, placeholder) in enumerate(reg_fields):
            label = tk.Label(
                right_frame,
                text=label_text,
                font=("Calibri", 12),
                bg="#EEEEEE"
            )
            label.grid(row=idx + 1, column=0, padx=(40, 10), pady=10, sticky="w")

            if placeholder in ["Password", "Confirm Password"]:
                entry = PlaceholderEntry(
                    right_frame,
                    font=("Calibri", 12),
                    placeholder=placeholder,
                    show="*"
                )
            else:
                entry = PlaceholderEntry(
                    right_frame,
                    font=("Calibri", 12),
                    placeholder=placeholder
                )

            entry.grid(row=idx + 1, column=1, padx=(0, 40), pady=10, sticky="ew")
            entries[placeholder] = entry

        right_frame.grid_columnconfigure(1, weight=1)

        # Terms and Conditions
        agree_var = tk.IntVar()
        terms_check = tk.Checkbutton(
            right_frame,
            text="I agree to the Terms & Conditions",
            variable=agree_var,
            bg="#EEEEEE",
            font=("Calibri", 12)
        )
        terms_check.grid(row=len(reg_fields) + 1, column=0, columnspan=2, pady=10)

        # Register Button
        register_button = tk.Button(
            right_frame,
            text="Register",
            background="#1E1F47",
            foreground="white",
            font=("Calibri", 14, "bold"),
            command=self.validate_registration,
            border=1,
            cursor="hand2",
            relief="flat",
            highlightthickness=0,
            bd=0,
        )
        register_button.grid(
            row=len(reg_fields) + 2,
            column=0,
            columnspan=2,
            pady=20,
            padx=40,
            ipadx=10,
            ipady=5,
        )

        # Footer
        footer_label = tk.Label(
            right_frame,
            text="Already have an account? Sign In",
            fg="#5855E5",
            bg="#EEEEEE",
            font=("Calibri", 10),
            cursor="hand2",
        )
        footer_label.bind("<Button-1>", self.switch_to_login)
        footer_label.grid(row=len(reg_fields) + 3, column=0, columnspan=2, pady=20)

        # Store references
        self.registration_frame = registration_page
        self.entries = entries
        self.agree_var = agree_var

    def validate_registration(self):
        """Validate registration form inputs"""
        # Basic validation example

        name = self.entries["Name"].get()
        username = self.entries["Username"].get()
        email = self.entries["Email"].get()
        phone = self.entries["Phone"].get()
        password = self.entries["Password"].get()
        confirm_password = self.entries["Confirm Password"].get()

        # Email validation
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        # Basic validation checks
        errors = []
        if not name or name == "Name":
            errors.append("Name is required")

        if not username or username == "Username":
            errors.append("Username is required")

        if not email or email == "Your Email" or not re.match(email_regex, email):
            errors.append("Valid email is required")

        if not phone or phone == "Phone Number" or not phone.isdigit():
            errors.append("Valid phone number is required")

        if not password or password == "Password":
            errors.append("Password is required")

        if not confirm_password or confirm_password == "Confirm Password":
            errors.append("Please confirm your password")

        if password != confirm_password:
            errors.append("Passwords do not match")

        if not self.agree_var.get():
            errors.append("You must agree to Terms & Conditions")

        # Display errors or proceed
        if errors:
            error_message = "\n".join(errors)
            messagebox.showerror("Registration Error", error_message)
        else:
            messagebox.showinfo("Registration", "Registration Successful!")
            user = User(name=name, phone_number=phone, address="Ismailia", gender=Gender.Male, user_id=1)
            c.execute("INSERT INTO User ( Name, Phone, Gender, Address) VALUES ( ?, ?, ?, ?)", ( user.get_name(), user.get_phone_number(), user.get_gender(), user.get_address()))
            account = Account(username=username, password=password, user_id=c.lastrowid, card_number=123456789, pin=1234, balance=1000.0)
            c.execute("INSERT INTO Account ( user_acc_ID, acc_user_name, acc_password, pin, balance) VALUES ( ?, ?, ?, ?, ?)", ( account.get_user_id(), account.get_username(), account.get_password(), account.get_pin(), account.get_balance()))
            con.commit()
            # Destroy registration page before switching
            self.destroy()
            # Switch to account page
            self.switch_to_account(user)

    def destroy(self):
        """Destroy the registration frame if it exists"""
        if self.registration_frame:
            self.registration_frame.destroy()

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", show=None, **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.show_char = show
        self.default_show = self.cget('show')
        self.placeholder_color = 'grey'
        self.default_fg_color = self.cget("fg")
        
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
        
        self._add_placeholder()

    def _clear_placeholder(self, event=None):
        if self.get() == self.placeholder and self.cget("fg") == self.placeholder_color:
            self.delete(0, tk.END)
            self.config(fg=self.default_fg_color)
            if self.show_char:
                self.config(show=self.show_char)

    def _add_placeholder(self, event=None):
        if not self.get():
            self.config(fg=self.placeholder_color)
            self.insert(0, self.placeholder)
            if self.show_char:
                self.config(show=self.default_show)
