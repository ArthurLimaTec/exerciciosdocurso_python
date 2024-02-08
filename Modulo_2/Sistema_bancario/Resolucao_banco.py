import Resolucao_contas
import Resolucao_pessoas

class Banco:
    def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[Resolucao_pessoas.Pessoa] | None = None,
            contas: list[Resolucao_contas.Conta] | None = None
            ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []


    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False
    
    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False


    def autenticar(self, cliente: Resolucao_pessoas.Pessoa, conta: Resolucao_contas.Conta):
        return self._checa_agencia(conta) and \
                self._checa_cliente(cliente) and \
                self._checa_conta(conta) and \
                self._checa_se_conta_e_do_cliente(cliente, conta)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'
    


if __name__ == "__main__":
    cliente_1 = Resolucao_pessoas.Cliente('Arthur', 26)
    cc1 = Resolucao_contas.ContaCorrente(111,222,0,0)
    cliente_1.conta = cc1
    cliente_2 = Resolucao_pessoas.Cliente('Fernanda', 42)
    cp1 = Resolucao_contas.ContaPoupanca(112,352,100)
    cliente_2.conta = cp1
       
    banco = Banco()
    banco.clientes.extend([cliente_1, cliente_2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111,222])

    if banco.autenticar(cliente_1, cc1):
        cc1.depositar(10)
        print(cliente_1.conta)

    print(banco)