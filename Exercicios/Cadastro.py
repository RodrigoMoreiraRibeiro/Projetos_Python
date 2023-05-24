import datetime as dt
import json


cadastro = dict()
lista = list()


hj = dt.date.today()

#inacabado
while True:

    cadastro['nome'] = str(input('Nome: ').capitalize())
    cadastro['idade'] = int(input('Ano de Nascimento: '))

    rsp = int(input('Carteira de Trabalho (0 não tem): '))

# Se não tiver Trabalho = Dados da pessoa

    if rsp == 0:

        with open('teste.json', 'r') as trans:
            lista = json.load(trans)
        print(f'''
        Nome: {cadastro["nome"]}
        Idade: {hj.year - cadastro["idade"]}
        Ctps: Não Possui''')
        break

# Se tiver Trabalho = Dados da pessoa

    if rsp != 0:

        with open('teste.json', 'r') as trans:
            lista = json.load(trans)
        hj = dt.date.today()
        cadastro['contratação'] = int(input('Ano Da Contratação: '))
        cadastro['salario'] = int(input('Sálario: R$ '))
        cadastro['idade'] = cadastro['idade']
        cadastro['aposentadoria'] = cadastro['contratação'] + 35
        anos = hj.year - cadastro["contratação"]
        print(f'''
        Nome: {cadastro["nome"]}
        Idade: {hj.year - cadastro["idade"]}
        Ctps: {rsp}
        Contratação: {cadastro["contratação"]}
        Salário: R${cadastro["salario"]:.2f}
        Aposentadoria: Trabalha à {anos} anos\n
        Irá se aposentar com {cadastro["aposentadoria"] - cadastro["idade"]} anos ''')

        break




# Adicionando o que está no dicionario para a lista
lista.append(cadastro)


#Jogando para o Arquivo Json
with open('teste.json', 'w') as trans:
    json.dump(lista, trans, indent='\t', ensure_ascii=False)





