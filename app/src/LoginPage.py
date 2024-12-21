import tkinter as tk
from tkinter import messagebox
from utils import PlaceholderEntry, create_left_panel

from classes.User import User, Gender
import sqlite3
con = sqlite3.connect('app/database/project.db')
c = con.cursor()

class LoginPage:
    def __init__(self, root, switch_to_registration, switch_to_account):
        self.root = root
        self.switch_to_registration = switch_to_registration
        self.switch_to_account = switch_to_account
        self.login_frame = None
        self.login_entries = {}

    def create_page(self):
        # Create root frame for login
        login_page = tk.Frame(self.root, bg="#E5E5E5")
        login_page.grid(row=0, column=0, sticky="nsew")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Left Panel
        left_frame = create_left_panel(
            login_page,
            "Welcome Back",
            "app/assets/register.png",
            "Secure and easy banking experience.\nRegister now to explore more features.",
        )

        # Right Panel (Login Form)
        right_frame = tk.Frame(login_page, bg="#EEEEEE", width=450)
        right_frame.grid(row=0, column=1, sticky="nsew",)
        login_page.grid_columnconfigure(1, weight=1)

        title_label = tk.Label(
            right_frame,
            text="Login to Your Account",
            fg="#1E1F47",
            bg="#EEEEEE",
            font=("Calibri", 18, "bold"),
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(170,40))

        # Login Fields
        login_fields = [
            ("Username or Email", "Username/Email"),
            ("Password", "Password"),
        ]
        entries = {}

        # Place fields using grid
        for idx, (field, placeholder) in enumerate(login_fields):
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
                show="*" if placeholder == "Password" else "",
            )

            entry.grid(row=idx + 1, column=1, padx=(0, 40), pady=10, sticky="ew")
            entries[placeholder] = entry

        right_frame.grid_columnconfigure(1, weight=1)

        # Login Button
        login_button = tk.Button(
            right_frame,
            text="Login",
            background="#1E1F47",
            foreground="white",
            font=("Calibri", 14, "bold"),
            command=self.validate_login,
            border=1,
            cursor="hand2",
            relief="flat",
            highlightthickness=0,
            bd=0,
        )
        login_button.grid(
            row=len(login_fields) + 2,
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
            text="Don't have an account? Register",
            fg="#5855E5",
            bg="#EEEEEE",
            font=("Calibri", 10),
            cursor="hand2",
            pady=27,
        )
        footer_label.bind("<Button-1>", self.switch_to_registration)
        footer_label.grid(row=len(login_fields) + 3, column=0, columnspan=2, pady=20)

        # Store references
        self.login_frame = login_page
        self.login_entries = entries

    def validate_login(self):
        """Validate login form inputs"""
        username = self.login_entries["Username/Email"].get()
        password = self.login_entries["Password"].get()

        # Basic validation checks
        errors = []
        if not username or username == "Username/Email":
            errors.append("Username is required")

        if not password or password == "Password":
            errors.append("Password is required")

        if errors:
            error_message = "\n".join(errors)
            messagebox.showerror("Login Error", error_message)
        else:
            # Create a user object for the logged-in user
            # In a real application, you would fetch this from a database
            # user = User(name=username, phone_number="N/A", address="N/A", gender=Gender.Male, user_id=1)
            userAccount= c.execute("SELECT * FROM Account WHERE acc_user_name = ? AND acc_password = ?", (username, password))
            userAccount = userAccount.fetchone()
            user = c.execute("SELECT * FROM User WHERE user_id = ?", (userAccount[1],))
            user = user.fetchone()
            user_obj = User(user[1], user[2], user[3], user[0], user[4])
            # print(userAccount)
            # print(user)
            if user is None:
                messagebox.showerror("Login Error", "Invalid username or password")
            else:
                messagebox.showinfo("Login", "Login Successful!")
                self.switch_to_account(user_obj)
                self.destroy()
            

    def destroy(self):
        """Destroy the login frame if it exists"""
        if self.login_frame:
            self.login_frame.destroy()
