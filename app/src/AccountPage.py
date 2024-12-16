import tkinter as tk
from tkinter import messagebox
import re
from classes.Account import Account

from classes.User import User, Gender
from utils import PlaceholderEntry, create_left_panel


# from .classes import Account

class AccountPage:
    def __init__(self, root):
        self.root = root
        self.account_frame = None
        self.user = None

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

        # Title
        title_label = tk.Label(
            right_frame,
            text="Hi " + (self.user.get_name() if self.user else "Guest") + "!",
            fg="#1E1F47",
            bg="#EEEEEE",
            font=("Calibri", 18, "bold"),
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Balance Section
        balance_frame = tk.Frame(right_frame, bg="#FFFFFF", bd=2, relief="ridge")
        balance_frame.grid(row=1, column=0, columnspan=2, pady=10, padx=20, sticky="ew")
        right_frame.grid_columnconfigure(
            0, weight=1
        )  # Ensure balance fills available width
        balance_label = tk.Label(
            balance_frame,
            text="Account Balance:",
            font=("Calibri", 14),
            bg="#FFFFFF",
            anchor="w",
        )
        balance_label.pack(side="left", padx=10, pady=5)

        self.balance_value = tk.Label(
            balance_frame,
            text="$0.00",
            font=("Calibri", 14, "bold"),
            bg="#FFFFFF",
            fg="#1E1F47",
        )
        self.balance_value.pack(side="right", padx=10, pady=5)

        # Recent Transactions Section this is an optinal section
        transactions_frame = tk.Frame(right_frame, bg="#FFFFFF", bd=2, relief="ridge", height=600)
        transactions_frame.grid(
            row=2, column=0, pady=55, padx=20, sticky="nsew",
        )
        transactions_label = tk.Label(
            transactions_frame,
            text="Recent Transactions",
            font=("Calibri", 14),
            bg="#FFFFFF",
        )
        transactions_label.pack(anchor="w", padx=10, pady=5)

        self.transactions_list = tk.Listbox(
            transactions_frame,
            font=("Calibri", 12),
            height=6,
            bg="#EEEEEE",
            fg="#1E1F47",
        )
        self.transactions_list.pack(fill="both", expand=True, padx=10, pady=5)

        # Add Placeholder Transactions (Mock Data)
        for transaction in [
            "Transaction 1",
            "Transaction 2",
            "Transaction 3",
            "Transaction 4",
            "Transaction 5",
            "Transaction 6",
            "Transaction 7",
            "Transaction 8",
            "Transaction 9",
            "Transaction 10",
        ]:
            self.transactions_list.insert(tk.END, transaction)

        # Action Buttons: Deposit and Withdraw
        actions_frame = tk.Frame(right_frame, bg="#EEEEEE")
        actions_frame.grid(row=3, column=0, columnspan=2, pady=10, padx=20)

        deposit_button = tk.Button(
            actions_frame,
            text="Deposit",
            font=("Calibri", 12),
            bg="#4CAF50",
            fg="white",
            relief="raised",
            command=self.deposit_money,
        )
        deposit_button.pack(side="left", padx=10)

        withdraw_button = tk.Button(
            actions_frame,
            text="Withdraw",
            font=("Calibri", 12),
            bg="#F44336",
            fg="white",
            relief="raised",
            command=self.withdraw_money,
        )
        withdraw_button.pack(side="right", padx=10)

        # Footer (Optional)
        footer_label = tk.Label(
            right_frame,
            text="Need assistance? Contact Support",
            fg="#5855E5",
            bg="#EEEEEE",
            font=("Calibri", 10),
            cursor="hand2",
        )
        footer_label.grid(row=4, column=0, columnspan=2, pady=20)

    def deposit_money(self):
        """Handle deposit functionality."""
        # Replace this with logic from the Account class
        amount = self.get_amount_from_user("Deposit Amount")
        if amount is not None:
            messagebox.showinfo("Deposit", f"Successfully deposited ${amount:.2f}")
            self.update_balance_display(amount, is_deposit=True)

    def withdraw_money(self):
        """Handle withdraw functionality."""
        # Replace this with logic from the Account class
        amount = self.get_amount_from_user("Withdraw Amount")
        if amount is not None:
            messagebox.showinfo("Withdraw", f"Successfully withdrew ${amount:.2f}")
            self.update_balance_display(amount, is_deposit=False)

    def get_amount_from_user(self, action_name):
        """Prompt user for an amount to deposit/withdraw."""
        amount = tk.simpledialog.askfloat(
            action_name, f"Enter the amount to {action_name.lower()}:"
        )
        if amount and amount > 0:
            return amount
        else:
            messagebox.showerror("Error", "Please enter a valid amount.")
            return None

    def update_balance_display(self, amount, is_deposit=True):
        """Update the displayed balance based on deposit/withdraw."""
        current_balance = float(self.balance_value["text"].strip("$"))
        new_balance = (
            current_balance + amount if is_deposit else current_balance - amount
        )
        self.update_balance(new_balance)

    def update_balance(self, balance):
        """Update the displayed balance"""
        self.balance_value.config(text=f"${balance:.2f}")

    def update_transactions(self, transactions):
        """Update the transactions list"""
        self.transactions_list.delete(0, tk.END)
        for transaction in transactions:
            self.transactions_list.insert(tk.END, transaction)

    def destroy(self):
        """Destroy the account frame if it exists"""
        if self.account_frame:
            self.account_frame.destroy()
