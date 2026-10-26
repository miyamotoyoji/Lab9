from decimal import Decimal, InvalidOperation

from models.banco_dados import BancoDados
from models.cliente import Cliente
from models.conta import Conta


class ContaController:
    def __init__(self, banco: BancoDados, view):
        self.banco = banco
        self.view = view
        self.view.ao_criar_conta(self.criar_conta)
        self.view.ao_consultar_conta(self.consultar_conta)

    def criar_conta(self, nome: str, cpf: str, saldo_texto: str) -> None:
        nome = nome.strip()
        cpf = "".join(c for c in cpf if c.isdigit())

        if not nome:
            self.view.exibir_erro("Informe o nome do cliente.")
            return
        if len(cpf) != 11:
            self.view.exibir_erro("O CPF deve ter 11 dígitos.")
            return
        if self.banco.buscar_por_cpf(cpf):
            self.view.exibir_erro("Já existe uma conta para este CPF.")
            return
        try:
            saldo = Decimal(saldo_texto.strip().replace(",", ".") or "0")
        except InvalidOperation:
            self.view.exibir_erro("Saldo inicial inválido.")
            return
        if saldo < 0:
            self.view.exibir_erro("O saldo inicial não pode ser negativo.")
            return

        cliente = Cliente(nome, cpf)
        conta = Conta(self.banco.proximo_numero(), cliente, saldo)
        self.banco.salvar(conta)

        self.view.limpar_campos()
        self.view.exibir_conta(conta)

    def consultar_conta(self, cpf: str) -> None:
        cpf = "".join(c for c in cpf if c.isdigit())
        conta = self.banco.buscar_por_cpf(cpf)
        if conta is None:
            self.view.exibir_erro("Nenhuma conta encontrada para este CPF.")
            return
        self.view.exibir_conta(conta)
