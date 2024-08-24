import tkinter as tk
from tkinter import messagebox
import database

class ChurchManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Church Management System")

        # Labels
        tk.Label(root, text="Nome Completo").grid(row=0, column=0)
        tk.Label(root, text="Endereço").grid(row=1, column=0)
        tk.Label(root, text="Telefone").grid(row=2, column=0)
        tk.Label(root, text="Email").grid(row=3, column=0)
        tk.Label(root, text="Data de Nascimento").grid(row=4, column=0)
        tk.Label(root, text="Data de Batismo").grid(row=5, column=0)
        tk.Label(root, text="Data de Casamento").grid(row=6, column=0)

        # Entry widgets
        self.nome_text = tk.StringVar()
        self.endereco_text = tk.StringVar()
        self.telefone_text = tk.StringVar()
        self.email_text = tk.StringVar()
        self.data_nascimento_text = tk.StringVar()
        self.data_batismo_text = tk.StringVar()
        self.data_casamento_text = tk.StringVar()

        tk.Entry(root, textvariable=self.nome_text).grid(row=0, column=1)
        tk.Entry(root, textvariable=self.endereco_text).grid(row=1, column=1)
        tk.Entry(root, textvariable=self.telefone_text).grid(row=2, column=1)
        tk.Entry(root, textvariable=self.email_text).grid(row=3, column=1)
        tk.Entry(root, textvariable=self.data_nascimento_text).grid(row=4, column=1)
        tk.Entry(root, textvariable=self.data_batismo_text).grid(row=5, column=1)
        tk.Entry(root, textvariable=self.data_casamento_text).grid(row=6, column=1)

        # Buttons
        tk.Button(root, text="Adicionar", width=12, command=self.add_member).grid(row=7, column=0)
        tk.Button(root, text="Ver Todos", width=12, command=self.view_members).grid(row=7, column=1)
        tk.Button(root, text="Atualizar", width=12, command=self.update_member).grid(row=7, column=2)
        tk.Button(root, text="Deletar", width=12, command=self.delete_member).grid(row=7, column=3)

        # Listbox and Scrollbar
        self.listbox = tk.Listbox(root, height=10, width=50)
        self.listbox.grid(row=8, column=0, rowspan=6, columnspan=2)
        self.scrollbar = tk.Scrollbar(root)
        self.scrollbar.grid(row=8, column=2, rowspan=6)
        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.listbox.yview)
        self.listbox.bind('<<ListboxSelect>>', self.get_selected_row)

    def add_member(self):
        database.insert(self.nome_text.get(), self.endereco_text.get(), self.telefone_text.get(),
                        self.email_text.get(), self.data_nascimento_text.get(), 
                        self.data_batismo_text.get(), self.data_casamento_text.get())
        self.view_members()

    def view_members(self):
        self.listbox.delete(0, tk.END)
        for row in database.view():
            self.listbox.insert(tk.END, row)

    def get_selected_row(self, event):
        try:
            index = self.listbox.curselection()[0]
            self.selected_tuple = self.listbox.get(index)
            self.nome_text.set(self.selected_tuple[1])
            self.endereco_text.set(self.selected_tuple[2])
            self.telefone_text.set(self.selected_tuple[3])
            self.email_text.set(self.selected_tuple[4])
            self.data_nascimento_text.set(self.selected_tuple[5])
            self.data_batismo_text.set(self.selected_tuple[6])
            self.data_casamento_text.set(self.selected_tuple[7])
        except IndexError:
            pass

    def delete_member(self):
        database.delete(self.selected_tuple[0])
        self.view_members()

    def update_member(self):
        database.update(self.selected_tuple[0], self.nome_text.get(), self.endereco_text.get(), 
                        self.telefone_text.get(), self.email_text.get(), self.data_nascimento_text.get(), 
                        self.data_batismo_text.get(), self.data_casamento_text.get())
        self.view_members()

if __name__ == "__main__":
    database.connect()
    root = tk.Tk()
    app = ChurchManagementApp(root)
    root.mainloop()
