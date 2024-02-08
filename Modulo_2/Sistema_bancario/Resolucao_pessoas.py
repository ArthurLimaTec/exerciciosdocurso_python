import Resolucao_contas

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade 

    @property   #não há, de fato, necessidade de usar neste caso. 
    def nome(self):         #feito apenas para treinar.
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome
    
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: Resolucao_contas.Conta | None = None

if __name__ == "__main__":
    cliente_1 = Cliente('Arthur', 26)
    cliente_1.conta = Resolucao_contas.ContaCorrente(111,222,0,0)
    cliente_2 = Cliente('Fernanda', 42)
    cliente_2.conta = Resolucao_contas.ContaCorrente(154,352,100,100)
       
    print(cliente_1)
    print(cliente_1.conta)
    print(cliente_2)
    print(cliente_2.conta)