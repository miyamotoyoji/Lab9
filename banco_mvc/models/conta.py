from decimal import Decimal
from models.cliente import Cliente


class Conta:
    def __init__(self, numero: int, cliente: Cliente, saldo_inicial: Decimal):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo_inicial
