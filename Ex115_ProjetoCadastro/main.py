import funci
import json

try:
    funci.carregar_dados()

except json.JSONDecodeError:
    print("Erro ao carregar os dados do arquivo JSON.")


while True:
    
    funci.escreva("MENU")
    
    print('''Escolha uma das Opções
    
1 - Cadastrar
2 - Exibir Lista
3 - Excluir
4 - Sair''')
    try:

        rsp = int(input(">>>>>> ".strip()))

        if rsp == 1:
            funci.cadastrar()
        elif rsp == 2:
            funci.exibir()
        elif rsp == 3:
            funci.escreva("EXCLUIR CADASTRO!")
            id = int(input("Digite o ID do cadastro a ser excluido!"))
            funci.excluir(id)
        elif rsp == 4:
            break
        elif rsp != (1, 2, 3, 4):
            print("Número não disponivel, Tente novamente!")
            continue

    except ValueError:
        print("Tente Novamente, Valor Inválido")

try:
    funci.salvar_dados()
except json.JSONDecodeError:
    print("Erro ao salvar os dados no arquivo JSON.")


