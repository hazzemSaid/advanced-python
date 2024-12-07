import tkinter as tk
from registration import RegistrationPage
from login import LoginPage


class BankSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank System")
        self.root.geometry("900x530")
        self.root.configure(bg="#E5E5E5")
        self.root.resizable(False, False)

        # Create page instances
        self.registration_page = RegistrationPage(self.root, self.switch_to_login)
        self.login_page = LoginPage(self.root, self.switch_to_registration)

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
