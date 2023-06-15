import json
lista_cadastros = []
proximo_id = 1


def escreva(msg):
    tamanho_linha = len(msg) + 20
    linha = '~' * tamanho_linha

    print(linha)
    print(f'{msg:^{tamanho_linha}}')
    print(linha)


def login():
    # Listas com usuarios e senhas correspondentes ao indice
    usuarios = ['admin', 'user1', 'user2']
    senhas = [1234, 5678, 9012]

    #Loop para validação de login
    while True:
        try:
            login = input("login: ")
            senha = int(input("Senha: "))
        except ValueError:
            print("Usuario ou Senha Inválidos")
            continue

        if login in usuarios and senha == senhas[usuarios.index(login)]:
            print("Acesso Permitido")
            return True
        else:
            print("Acesso negado")


def menu():
    while True:
        print("\033[0;30;43m", end='')
        escreva("MENU")
        print("\033[m")
        print('''Escolha uma das Opções

    1 - Cadastrar
    2 - Exibir Lista
    3 - Excluir
    4 - Atualiar
    5 - Sair''')
        try:

            rsp = int(input(">>>>>> ".strip()))

            if rsp == 1:
                cadastrar()
            elif rsp == 2:
                exibir()
            elif rsp == 3:
                escreva("EXCLUIR CADASTRO!")
                id = int(input("Digite o ID do cadastro a ser excluido!"))
                excluir(id)
            elif rsp == 4:
                id = int(input("Digite o ID do cadastro a ser Atualizado!"))
                atualizar(id)
            elif rsp == 5:
                break
            elif rsp != (1, 2, 3, 4, 5):
                print("Opção indisponivel, Tente novamente!")
                continue

        except ValueError:
            print("Tente Novamente, Valor Inválido")


def obter_resposta():

    while True:
        rsp = str(input('Quer continuar? [S/N]')).upper()[0].strip()
        if rsp == 'S':
            return True
        elif rsp == 'N':
            return False
        else:
            print('Opção inválida.')


def carregar_dados():
    global lista_cadastros
    try:
        with open('dados.json', 'r') as arquivo:
            dados = json.load(arquivo)
            #global lista_cadastros
            lista_cadastros = dados
            global proximo_id
            proximo_id = max([cadastro["_id_"]for cadastro in lista_cadastros]) + 1
    except FileNotFoundError:
        pass


def salvar_dados():
    with open('dados.json', 'w') as arquivo:
        json.dump(lista_cadastros, arquivo, indent=4)


def cadastrar():

    global proximo_id
    escreva("NOVO CADASTRO")
    while True:
        global nome
        global idade
        while True:
            try:
                nome = str(input('Digite um nome: ').strip().capitalize())
                if not nome:
                    raise ValueError('ERRO: O nome não pode estar vazio')
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                idade = int(input('Digite sua idade: ').strip())
                break
            except ValueError:
                print('ERRO: Digite um número inteiro!!!')

        cadastro = dict()
        cadastro["_id_"] = proximo_id
        cadastro["_nome_"] = nome
        cadastro["_idade_"] = idade
        lista_cadastros.append(cadastro.copy())

        if not obter_resposta():
            break

        proximo_id += 1


def exibir():
    escreva("LISTA DE CADASTRO")
    print("ID".ljust(4),"NOME".ljust(19),"IDADE")
    print("~~"*19)
    for cadastro in lista_cadastros:
        _id_ = str(cadastro.get("_id_")).ljust(5)
        nome = str(cadastro.get("_nome_")).ljust(20)
        idade = str(cadastro.get("_idade_")).ljust(3) + " Anos"

        valores = [f"{str(valor) + ' Anos':>10}"for valor in cadastro.values()]
        #print('         '.join(valores))

        print(f"{_id_}{nome}{idade}")
    print("\n")


def atualizar(id):

    for cadastro in lista_cadastros:
        if cadastro["_id_"] == id:
            escreva("ATUALIZAR CADASTRO")
            while True:
                try:
                    nome = str(input('Digite um nome: ').strip().capitalize())
                    if not nome:
                        raise ValueError('ERRO: O nome não pode estar vazio')
                    break
                except ValueError as e:
                    print(e)
            while True:
                try:
                    idade = int(input('Digite sua idade: ').strip())
                    break
                except ValueError:
                    print('ERRO: Digite um número inteiro!!!')

            cadastro["_nome_"] = nome
            cadastro["_idade_"] = idade

            salvar_dados()
            escreva("Cadastro Atualizado com Sucesso")
            return
    escreva("Nenhum Cadastro Encontrado com esse ID!")


try:
    carregar_dados()
except json.JSONDecodeError:
    print("Erro ao carregar os dados do arquivo JSON.")

#cadastrar()
#exibir()

try:
    salvar_dados()
except json.JSONDecodeError:
    print("Erro ao salvar os dados no arquivo JSON.")


def excluir(id):

    global lista_cadastros
    for cadastro in lista_cadastros:
        if cadastro['_id_'] == id:
            lista_cadastros.remove(cadastro)
            escreva("Cadastro Removido Com Sucesso!")
            return
    escreva("Nenhum cadastro encontrado com esse ID!")
