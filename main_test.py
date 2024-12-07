import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Root Window
root = tk.Tk()
root.title("Bank System")
root.geometry("900x500")
root.configure(bg="#E5E5E5")

# Left Panel (Dashboard Info)
left_frame = tk.Frame(root, bg="#1E1F47", width=450)
left_frame.grid(
    row=0, column=0, sticky="ns"
)  # Align to the left and stretch vertically

logo_label = tk.Label(
    left_frame,
    text="Register Now",
    fg="white",
    bg="#1E1F47",
    font=("Calibri", 20, "bold"),
)
logo_label.grid(row=0, column=0, pady=(40, 10), padx=20)

image_path = "./assets/register.png"
dashboard_image = Image.open(image_path)
dashboard_image = dashboard_image.resize((200, 200), Image.Resampling.LANCZOS)
dashboard_image_tk = ImageTk.PhotoImage(dashboard_image)

dashboard_image_label = tk.Label(left_frame, image=dashboard_image_tk, bg="#1E1F47")
dashboard_image_label.image = (
    dashboard_image_tk  # Keep a reference to avoid garbage collection
)
dashboard_image_label.grid(row=1, column=0, pady=20)

description_label = tk.Label(
    left_frame,
    text="Secure and easy banking experience.\nRegister now to explore more features.",
    fg="white",
    bg="#1E1F47",
    font=("Calibri", 12),
    justify="center",
)
description_label.grid(row=2, column=0, pady=20, padx=10)

# Right Panel (Registration Form)
right_frame = tk.Frame(root, bg="#EEEEEE", width=450)
right_frame.grid(row=0, column=1, sticky="nsew")  # Align to the right and stretch

# Ensure the right panel stretches properly
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

title_label = tk.Label(
    right_frame,
    text="Create Your Account",
    fg="#1E1F47",
    bg="#EEEEEE",
    font=("Calibri", 18, "bold"),
)
title_label.grid(row=0, column=0, columnspan=2, pady=20)


# Form Fields
class PlaceholderEntry(ttk.Entry):
    def __init__(self, master=None, placeholder="", color="grey", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self["foreground"]

        # Add placeholder and bind necessary events
        self._add_placeholder()
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
        self.bind("<Key>", self._remove_placeholder_on_type)  # Changed from <KeyPress>

    def _add_placeholder(self, e=None):
        """Add placeholder if entry is empty."""
        if not self.get():
            self.insert(0, self.placeholder)
            self["foreground"] = self.placeholder_color

    def _clear_placeholder(self, e=None):
        """Clear placeholder if it exists."""
        if self.get() == self.placeholder:
            self.delete(0, "end")
            self["foreground"] = self.default_fg_color

    def _remove_placeholder_on_type(self, e=None):
        """Clear placeholder when typing starts."""
        if self.get() == self.placeholder:
            self.delete(0, "end")
            self["foreground"] = self.default_fg_color


fields = [
    ("Enter Name", "Name"),
    ("Username", "Username"),
    ("Your Email", "Email"),
    ("Phone Number", "Phone"),
    ("Password", "Password"),
    ("Confirm Password", "Confirm Password"),
]
entries = {}

# Place fields using grid
for idx, (field, placeholder) in enumerate(fields):
    label = tk.Label(
        right_frame, text=field, fg="#1E1F47", bg="#EEEEEE", font=("Calibri", 12)
    )
    label.grid(row=idx + 1, column=0, padx=(40, 10), pady=10, sticky="w")

    entry = PlaceholderEntry(
        right_frame,
        font=("Calibri", 12),
        placeholder=placeholder,
    )

    entry.grid(row=idx + 1, column=1, padx=(0, 40), pady=10, sticky="ew")
    entries[placeholder] = entry


# Ensure the second column expands dynamically
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
    row=len(fields) + 1, column=0, columnspan=2, padx=40, pady=10, sticky="w"
)

# Register Button
register_button = tk.Button(
    right_frame,
    text="Register",
    background="#1E1F47",
    foreground="white",
    font=("Calibri", 14, "bold"),
    command=lambda: print("Registering User..."),
    border=1,
    cursor="hand2",
    relief="flat",
    highlightthickness=0,
    bd=0,
)

register_button.grid(
    row=len(fields) + 2, column=0, columnspan=2, pady=20, padx=40, ipadx=10, ipady=5
)

# Footer
footer_label = tk.Label(
    right_frame,
    text="Already have an account? Sign In",
    fg="#5855E5",
    bg="#EEEEEE",
    font=("Calibri", 10),
)
footer_label.grid(row=len(fields) + 3, column=0, columnspan=2, pady=20)

# Run Application
root.mainloop()
