import tkinter as tk
from RegistrationPage import RegistrationPage
from LoginPage import LoginPage
from AccountPage import AccountPage


class BankSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank System")
        self.root.geometry("900x530")
        self.root.configure(bg="#E5E5E5")
        self.root.resizable(False, False)

        # Create page instances
        self.account_page = AccountPage(self.root)
        self.registration_page = RegistrationPage(self.root, self.switch_to_login, self.switch_to_account)
        self.login_page = LoginPage(self.root, self.switch_to_registration, self.switch_to_account)

        # Start with registration page
        self.registration_page.create_page()

    def switch_to_login(self, event=None):
        """Switch to login page"""
        # Destroy registration page if it exists
        self.registration_page.destroy()
        # Create login page
        self.login_page.create_page()

    def switch_to_registration(self, event=None):
        """Switch to registration page"""
        # Destroy login page if it exists
        self.login_page.destroy()
        # Create registration page
        self.registration_page.create_page()

    def switch_to_account(self, user=None):
        """Switch to account page"""
        # Destroy login page if it exists
        self.login_page.destroy()
        # Set user information
        if user:
            self.account_page.set_user(user)
        # Create account page
        self.account_page.create_page()