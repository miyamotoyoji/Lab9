from models.conta import Conta


class BancoDados:
    """Banco de dados simulado: guarda as contas em uma lista na memória."""

    def __init__(self):
        self._contas: list[Conta] = []

    def proximo_numero(self) -> int:
        return len(self._contas) + 1

    def salvar(self, conta: Conta) -> None:
        self._contas.append(conta)

    def buscar_por_cpf(self, cpf: str) -> Conta | None:
        for conta in self._contas:
            if conta.cliente.cpf == cpf:
                return conta
        return None

    def listar(self) -> list[Conta]:
        return list(self._contas)
