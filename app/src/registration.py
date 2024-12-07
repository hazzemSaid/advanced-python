import tkinter as tk
from tkinter import messagebox
import re
from utils import PlaceholderEntry, create_left_panel


class RegistrationPage:
    def __init__(self, root, switch_to_login):
        self.root = root
        self.switch_to_login = switch_to_login
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
            "./assets/register.png",
            "Secure and easy banking experience.\nRegister now to explore more features.",
        )

        # Right Panel (Registration Form)
        right_frame = tk.Frame(registration_page, bg="#EEEEEE", width=450)
        right_frame.grid(row=0, column=1, sticky="nsew")
        registration_page.grid_columnconfigure(1, weight=1)

        title_label = tk.Label(
            right_frame,
            text="Create Your Account",
            fg="#1E1F47",
            bg="#EEEEEE",
            font=("Calibri", 18, "bold"),
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

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
        for idx, (field, placeholder) in enumerate(reg_fields):
            label = tk.Label(
                right_frame,
                text=field,
                fg="#1E1F47",
                bg="#EEEEEE",
                font=("Calibri", 12),
            )
            label.grid(row=idx + 1, column=0, padx=(40, 10), pady=10, sticky="w")

            entry = PlaceholderEntry(
                right_frame,
                font=("Calibri", 12),
                placeholder=placeholder,
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
            onvalue=1,
            offvalue=0,
            bg="#EEEEEE",
            fg="#1E1F47",
            font=("Calibri", 10),
        )
        terms_check.grid(
            row=len(reg_fields) + 1,
            column=0,
            columnspan=2,
            padx=40,
            pady=10,
            sticky="w",
        )

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

    def destroy(self):
        """Destroy the registration frame if it exists"""
        if self.registration_frame:
            self.registration_frame.destroy()
