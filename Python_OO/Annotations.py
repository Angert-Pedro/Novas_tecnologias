from Contas.Conta import Conta
from Contas.Cliente import Cliente
from Contas.Historico import Historico



pedro = Cliente('Pedro' , 'Elias', '111111-1')
conta_pedro = Conta('123-4',pedro,540.00)

print(f"{pedro.nome}")
print(f"{conta_pedro.numero}")

print(conta_pedro.extrato())
conta_pedro.deposita(500.00)
print(conta_pedro.extrato())


gustavo = Cliente('Gustavo', 'Silva', '2222-2')
conta_gustavo = Conta('123-5',gustavo, 500.00)

print(conta_gustavo.extrato())

conta_pedro.transfere(conta_gustavo,300.0)

print(conta_pedro.extrato())
print(conta_gustavo.extrato())


conta_pedro.historico.imprime()
conta_gustavo.historico.imprime()
