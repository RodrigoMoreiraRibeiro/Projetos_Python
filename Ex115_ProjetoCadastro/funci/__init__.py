import json
lista_cadastros = []
proximo_id = 1


def escreva(msg):
    tamanho_linha = len(msg) + 20
    linha = '~' * tamanho_linha

    print(linha)
    print(f'{msg:^{tamanho_linha}}')
    print(linha)


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
    for cadastro in lista_cadastros:
        _id_ = str(cadastro.get("_id_")).ljust(5)
        nome = str(cadastro.get("_nome_")).ljust(15)
        idade = str(cadastro.get("_idade_")) + " Anos"

        valores = [f"{str(valor) + ' Anos':>10}"for valor in cadastro.values()]
        #print('         '.join(valores))
        print(f"{_id_}{nome}{idade}")

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
