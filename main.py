from ui import ChurchManagementApp
import tkinter as tk
import database

if __name__ == "__main__":
    database.connect()
    root = tk.Tk()
    app = ChurchManagementApp(root)
    root.mainloop()
