from .Historico import Historico
class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.numero = numero #É o This do java, o self é o próprio objeto
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico


    def deposita(self,valor):
        self.saldo +=valor
        self.historico.transacoes.append(f"Depósito de {valor}")


    def saca(self,valor):
        if(self.saldo <valor):
            return False
        else:
            self.saldo -=valor
            self.historico.transacoes.append(f"Saque de {valor}")
            return True


    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))
        self.historico.transacoes.append(f"tirou extrato -saldo de {self.saldo}")

    def transfere(self, destino, valor):
        retirou = self.saca(valor)
        if(retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f"transferencia de {valor} para conta {destino.numero}")
            return True
