import tkinter as tk
from app import BankSystemApp


def main():
    root = tk.Tk()
    app = BankSystemApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
