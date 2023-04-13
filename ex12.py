agenda = {}

while True:
    nome = input("Digite o nome da pessoa: ")
    if nome == '':
        break
    
    telefone = input("Digite o telefone: ")
    
    #Adiciona o telefone ao dicionário
    agenda[nome] = telefone 
    
#Pesquisa um telefone na segunda 
nome_pesquisa = input("Digite o nome pra pesquisar: ")
if nome_pesquisa in agenda:
    print("Telefone de", nome_pesquisa,":", agenda[nome_pesquisa])
else:
    print("Nome não encontado na agenda.")