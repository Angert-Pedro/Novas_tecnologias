#Faça um programa que controle uma agenda (utilize dicionário).
#Com as funções apaga(), altera(), lista_nomes(), busca(), grava(), menu().
#Depois faça as seguintes melhorias:

agenda = {'lucas':'98329-4938','flavio':'92849-3928','luiza':'92843-3423', \
          'roberto':'98374-2342'}

print(agenda)

#chave_apaga = str(input("Insira o nome ")).lower()



def apaga(chave):
    del agenda[chave]

#apaga(chave_apaga)

def altera(chave, valor):
    agenda[chave] = (valor)
    print(agenda[chave])

#altera('lucas','99999-9999')

def lista_nomes():
    for nomes in agenda.keys():
        print(nomes, end=' ')
#lista_nomes()

#chave_busca = str(input("Insira o nome de alguem: ")).lower()
def busca(chave):
    if chave in agenda:
        print(f"A pessoa {chave} tem o número :{agenda[chave]}")
    else:
        print("Erro, insira um nome valido!")

#busca(chave_busca)

chave = str(input("Insira o nome a ser adicionado")).lower()
valor = str(input(f"Insira o numero {chave}")).lower()

def gravar(chave,valor):
    if chave in agenda:
        print("Erro, já tem uma entrada com esse nome")
    else:
        agenda[chave] = valor

gravar(chave,valor)

#Exibir a posição de cada elemento
def exibirPosicao():
    i=0
    for contatos in agenda:
        print(contatos,"-", i)
        i+=1
exibirPosicao()


def menu():
    print(f"A agenda tem {len(agenda)} contatos")


print(agenda)

print(f"O tamanho da agenda 'e {len(agenda)}")
