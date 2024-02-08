import abc

class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self,valor: float) -> float: 
        ...

    def depositar(self,valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(Depósito de {valor})')
        return self.saldo 

    def detalhes(self, msg: str = '') -> None:
        print(f'Saldo: {self.saldo: .2f} {msg}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(Saque de {valor})')
            return self.saldo 
        
        print(f'Saque de {valor} negada.')

class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float = 0):  #atributo a mais para ter o limite
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_max = -self.limite

        if valor_pos_saque >= limite_max:
            self.saldo -= valor
            self.detalhes(f'(Saque de {valor})')
            return self.saldo 
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'
        
        print(f'Saque de {valor} negada.')
        print(f'Seu Limite é de {-self.limite: .2f}')
        self.detalhes(f'(Saque de {valor} negado!)')




if __name__ == '__main__':
    contapoupaca_1 = ContaPoupanca(111, 222)
    contapoupaca_1.sacar(1)
    contapoupaca_1.depositar(1)
    contapoupaca_1.sacar(1)
    print('###')

    contacorrente_1 = ContaCorrente(111, 222, 0, 100)
    contacorrente_1.sacar(1)
    contacorrente_1.depositar(1)
    contacorrente_1.sacar(1)
    contacorrente_1.sacar(1)
    contacorrente_1.sacar(98)
    contacorrente_1.sacar(1)
    print('###')