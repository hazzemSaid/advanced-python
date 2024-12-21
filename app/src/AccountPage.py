import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from classes.Account import Account
from classes.User import User, Gender
from utils import create_left_panel


class AccountPage:
    def __init__(self, root):
        self.root = root
        self.account_frame = None
        self.user = None
        self.balance_value = None

    def set_user(self, user):
        self.user = user

    def create_page(self):
        # Create root frame for account page
        account_page = tk.Frame(self.root, bg="#E5E5E5")
        account_page.grid(row=0, column=0, sticky="nsew")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Left Panel
        left_frame = create_left_panel(
            account_page,
            "Account Overview",
            "app/assets/account.png",
            "Secure and easy banking experience.\nRegister now to explore more features.",
        )

        # Right Panel
        right_frame = tk.Frame(account_page, bg="#EEEEEE", width=450)
        right_frame.grid(row=0, column=1, sticky="nsew")
        account_page.grid_columnconfigure(1, weight=3)

        # Load the photo
        self.photo = tk.PhotoImage(file="app/assets/profile-icon.png")

        # Title
        title_label = tk.Label(
            right_frame,
            image=self.photo,  # Retain reference to prevent garbage collection
            bg="#EEEEEE",
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Balance Section
        balance_frame = tk.Frame(right_frame, bg="#FFFFFF", bd=2, relief="ridge")
        balance_frame.grid(row=1, column=0, columnspan=2, pady=10, padx=20, sticky="ew")
        right_frame.grid_columnconfigure(0, weight=1)

        # Main balance label
        balance_label = tk.Label(
            balance_frame,
            text="Account Balance:",
            font=("Calibri", 14),
            bg="#FFFFFF",
            anchor="w",
        )
        balance_label.pack(side="left", padx=10, pady=5)

        # Balance value label
        self.balance_value = tk.Label(
            balance_frame,
            text="$0.00",
            font=("Calibri", 14, "bold"),
            bg="#FFFFFF",
            fg="#1E1F47",
        )
        self.balance_value.pack(side="right", padx=10, pady=5)

        #account labels
        reg_fields = [
            ("Username", ""),
            ("User Id", ""),
            ("Your Email", ""),
            ("Phone Number", ""),
            ("Card Number", ""),
            ("Pin", ""),
        ]

        # Place fields using grid
        for idx, (label_text, value) in enumerate(reg_fields):
            label = tk.Label(
                right_frame,
                text=label_text,
                font=("Calibri", 12),
                bg="#EEEEEE",
            )
            label.grid(row=idx + 2, column=0, padx=(40, 10), pady=10, sticky="w")

            value_label = tk.Label(
                right_frame,
                text=value,
                font=("Calibri", 12, "bold"),
                bg="#EEEEEE",
            )
            value_label.grid(row=idx + 2, column=1, padx=(0, 40), pady=10, sticky="w")

        right_frame.grid_columnconfigure(1, weight=1)

        # Footer (Optional)
        footer_label = tk.Label(
            right_frame,
            text="Need assistance? Contact Support",
            fg="#5855E5",
            bg="#EEEEEE",
            font=("Calibri", 10),
            cursor="hand2",
        )
        footer_label.grid(row=len(reg_fields) + 3, column=0, columnspan=2, pady=20)

   