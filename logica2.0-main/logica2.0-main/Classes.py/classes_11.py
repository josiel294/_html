import os 
import time
os.system("cls || clear")

#Função para adicionar nomes
#Se a lista não tem conteúdo,retorna o valor: True (Verdadeiro)

def verificar_lista_vazia(lista_nomes):
    if not lista_nomes:
        print("\nA lista está vazia.")
        return True 
    return False

def adicionar(lista_nomes):
     nome = input("Digte o nome que deseja adicionar: ")
     lista_nomes.append(nome)
     print(f"\nO nome {nome} foi adicionado com sucesso !")

def mostrar(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        return
    
    print("\n = Lista de nomes =")
    for nome in lista_nomes:
        print(nome)

# Função para atualizar nomes
def atualizar(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        return

    print("\n = Lista de nomes =")
    for nome in lista_nomes:
        print(nome)
    nome_antigo = input("Digite o nome que deseja atualizar: ")
    if nome_antigo in lista_nomes:
        novo_nome = input(f"Digite o novo nome para {nome_antigo}:")
        indice = lista_nomes.index(nome_antigo)
        lista_nomes[indice] = novo_nome
        print(f"{nome_antigo} foi atualizado para {novo_nome} com sucesso !")
    else: 
        print(f"\nO {nome_antigo} não foi encontrado.")

#Função para excluir nomes.
def excluir(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        return      

    mostrar(lista_nomes)

    nome_remover = input("Digite o nome que desja remover:") #Mostrar  lista de usários.
    if nome_remover in  lista_nomes:
        lista_nomes.remove(nome_remover) 
        print(f"O nome {nome_remover} foi remmovido com sucesso ! ")
    else:
        print(f"\nO nome {nome_remover} não foi encontrado na lista>")                                                                                                                                       

# Cria a lista de nomes
nomes = []

#Menu
while True:
    print("= Gerenciador de nomes =")
    print("1 - Adicionar")
    print("2 - Listar nomes")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("5 - Sair")

    opcao = int(input("Digite uma das opções:"))

    match opcao:
        case 1:
            adicionar(nomes)
        case 2:
            mostrar(nomes)
        case 3:
            atualizar(nomes)
        case 4:
            excluir(nomes)
        case 5:
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção inválida. \nTente novamente.")
    if opcao != 5:
        time.sleep(2)
    os.system("cls  || clear")
