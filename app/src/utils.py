import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


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
        self.bind("<Key>", self._remove_placeholder_on_type)

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


def create_left_panel(parent, title, image_path, description):
    """Create a consistent left panel for registration and login pages"""

    # Left Panel (Dashboard Info)
    left_frame = tk.Frame(parent, bg="#1E1F47", width=450)
    left_frame.grid(row=0, column=0, sticky="ns")

    logo_label = tk.Label(
        left_frame,
        text=title,
        fg="white",
        bg="#1E1F47",
        font=("Calibri", 20, "bold"),
    )
    logo_label.grid(row=0, column=0, pady=(40, 10), padx=20)

    dashboard_image = Image.open(image_path)
    dashboard_image = dashboard_image.resize((200, 200), Image.Resampling.LANCZOS)
    dashboard_image_tk = ImageTk.PhotoImage(dashboard_image)

    dashboard_image_label = tk.Label(left_frame, image=dashboard_image_tk, bg="#1E1F47")
    dashboard_image_label.image = dashboard_image_tk
    dashboard_image_label.grid(row=1, column=0, pady=20)

    description_label = tk.Label(
        left_frame,
        text=description,
        fg="white",
        bg="#1E1F47",
        font=("Calibri", 12),
        justify="center",
    )
    description_label.grid(row=2, column=0, pady=20, padx=10)

    return left_frame
