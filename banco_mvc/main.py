import tkinter as tk

from controllers.conta_controller import ContaController
from models.banco_dados import BancoDados
from views.conta_view import ContaView


def main():
    root = tk.Tk()
    banco = BancoDados()
    view = ContaView(root)
    ContaController(banco, view)
    root.mainloop()


if __name__ == "__main__":
    main()
