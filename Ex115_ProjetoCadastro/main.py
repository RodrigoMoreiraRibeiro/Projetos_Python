import funci
import json
try:
    try:
        funci.carregar_dados()

    except json.JSONDecodeError:
        print("Erro ao carregar os dados do arquivo JSON.")

    funci.login()

    funci.menu()


    print("Voce saiu do Programa!")
    try:
        funci.salvar_dados()
    except json.JSONDecodeError:
        print("Erro ao salvar os dados no arquivo JSON.")

except KeyboardInterrupt:
    print("\n")
    funci.escreva("Voce forçou a interrupção do programa!")

