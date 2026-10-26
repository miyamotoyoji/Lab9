import tkinter as tk
from tkinter import messagebox


class ContaView:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Banco - Cadastro de Contas")
        self.root.resizable(False, False)

        cadastro = tk.LabelFrame(root, text="Criar Conta", padx=10, pady=10)
        cadastro.pack(fill="x", padx=10, pady=(10, 5))

        tk.Label(cadastro, text="Nome:").grid(row=0, column=0, sticky="w")
        self.entrada_nome = tk.Entry(cadastro, width=35)
        self.entrada_nome.grid(row=0, column=1, pady=2)

        tk.Label(cadastro, text="CPF:").grid(row=1, column=0, sticky="w")
        self.entrada_cpf = tk.Entry(cadastro, width=35)
        self.entrada_cpf.grid(row=1, column=1, pady=2)

        tk.Label(cadastro, text="Saldo Inicial (R$):").grid(row=2, column=0, sticky="w")
        self.entrada_saldo = tk.Entry(cadastro, width=35)
        self.entrada_saldo.grid(row=2, column=1, pady=2)

        self.botao_criar = tk.Button(cadastro, text="Criar Conta")
        self.botao_criar.grid(row=3, column=0, columnspan=2, pady=(8, 0))

        consulta = tk.LabelFrame(root, text="Consultar Conta", padx=10, pady=10)
        consulta.pack(fill="x", padx=10, pady=5)

        tk.Label(consulta, text="CPF:").grid(row=0, column=0, sticky="w")
        self.entrada_consulta = tk.Entry(consulta, width=25)
        self.entrada_consulta.grid(row=0, column=1, padx=5)
        self.botao_consultar = tk.Button(consulta, text="Consultar")
        self.botao_consultar.grid(row=0, column=2)

        dados = tk.LabelFrame(root, text="Dados da Conta", padx=10, pady=10)
        dados.pack(fill="both", padx=10, pady=(5, 10))
        self.texto_dados = tk.Label(dados, text="Nenhuma conta exibida.", justify="left",
                                    font=("Consolas", 10), anchor="w", width=45)
        self.texto_dados.pack(fill="x")

    # Entradas: o Controller registra o que fazer quando os botões são clicados
    def ao_criar_conta(self, callback) -> None:
        self.botao_criar.config(command=lambda: callback(
            self.entrada_nome.get(), self.entrada_cpf.get(), self.entrada_saldo.get()))

    def ao_consultar_conta(self, callback) -> None:
        self.botao_consultar.config(command=lambda: callback(self.entrada_consulta.get()))

    # Saídas
    def exibir_conta(self, conta) -> None:
        cpf = conta.cliente.cpf
        cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        saldo = f"{conta.saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        self.texto_dados.config(text=(
            f"Conta nº: {conta.numero}\n"
            f"Cliente:  {conta.cliente.nome}\n"
            f"CPF:      {cpf_formatado}\n"
            f"Saldo:    R$ {saldo}"
        ))

    def exibir_erro(self, mensagem: str) -> None:
        messagebox.showerror("Erro", mensagem)

    def limpar_campos(self) -> None:
        for entrada in (self.entrada_nome, self.entrada_cpf, self.entrada_saldo):
            entrada.delete(0, tk.END)
