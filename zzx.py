agenda = {'joao':["61978999898","02/04/1995"]}

def salvar(nome,telefone,data_nascimento):
    agenda[nome]=[telefone,data_nascimento]

def busca(nome):
    tel = agenda[nome][0]
    data = agenda[nome][1]
    return tel,data

def apagar(nome):
    del agenda[nome]

salvar("Igor","619616416351","05/08/5495")


print(agenda,end="\n\n\n\n")

apagar("Igor")
print(agenda)
