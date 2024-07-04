import csv
from anao import Anao

def escreveArquivo(nome, tamanho, etnia, origem, personalidade, preco):
    with open('anoe.csv', 'a', newline='') as csvfile:
        escreve_anao = csv.writer(csvfile, delimiter=',')
        escreve_anao.writerow([nome, tamanho, etnia, origem, personalidade, preco])
        print("### Anão ", nome, "adicionado com sucesso! ###")

anoes = []
print("### BEM VINDO A TELA DE ANÔES ###")
while(True):
    print("\nNOVO USUÁRIO:")
    nome = input("Digite o nome do anão: \n")
    personalidade = input("Solicite a personalidade: \n")
    origem = input("Solicite a origem: \n")
    etnia = input("Etnia: \n")
    preco = float(input("Preco:"))
    tamanho = float(input("tamanho"))
    novoAnao = Anao(nome, tamanho, etnia, origem, personalidade, preco)
    
    escreveArquivo(nome, tamanho, etnia, origem, personalidade, preco)
    anoes.append(novoAnao)
    # TESTE PARA VER SE O SISTEMA FUNCIONA:
    for anao in anoes:
        print(anao.nome, " - ")


    

