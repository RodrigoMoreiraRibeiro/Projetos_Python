import PySimpleGUI as sg
from PIL import Image, ImageTk
import buttons
color = None

def log():
    global color
    sg.theme('Dark Blue 13')
    # Listas com usuarios e senhas correspondentes ao indice
    usuarios = ['admin', 'user1', 'user2']
    senhas = [1234, 5678, 9012]

    layout = [
        [sg.Text('Login')],
        [sg.Input(key='-LOGIN-')],
        [sg.Text('Senha')],
        [sg.Input(key='-SENHA-', password_char='*')],
        [sg.Canvas(background_color= color, size=(10, 10))],
        [sg.Button('Entrar')]
    ]

    window = sg.Window('Login', layout)

    # Loop para validação de login
    while True:
        event, values, = window.read()
        login = values['-LOGIN-']
        senha = values['-SENHA-']




        if event == 'Entrar':
            if login in usuarios and int(senha) == senhas[usuarios.index(login)]:
                sg.popup("Acesso Permitido")
                break
            else:
                sg.popup("Acesso negado")
                window['-LOGIN-'].Update('')
                window['-SENHA-'].Update('')

    window.close()


def menu():
    global color
    global window2
    color = None
    sg.theme('Dark Blue 13')

    caminho_imagem_fundo = 'projeto.png'

    menu_layout = [
        [sg.Button('', image_data=buttons.button_cadastrar_base, key='-CADASTRAR-',
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
         sg.Canvas(background_color=color, size=(100, 5)),
         sg.Button('', image_data=buttons.button_excluir_base, key='-EXCLUIR-',
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
         sg.Canvas(background_color=color, size=(100, 5)),
         sg.Button('', image_data=buttons.button_exibir_base, key='-EXCLUIR-',
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
         sg.Canvas(background_color=color, size=(100, 5)),
         sg.Button('', image_data=buttons.button_reg_base, key='-EXCLUIR-',
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)]

    ]

    menu2_layout = [
        [sg.Canvas(background_color=color, size=(100, 5))],
        [sg.Button('', image_data=buttons.button_sair_base, key='-EXCLUIR-',
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)]
    ]

    layout = [
        [sg.Canvas(background_color='black', size=(2300, 700), key='-CANVAS-')],
        [sg.Column(menu_layout, justification='center', element_justification='center', k='-COL1-')],
        [sg.Column(menu2_layout, justification='center', element_justification='center', k='-COL2-')]
    ]

    window = sg.Window('Menu', layout, resizable=True, finalize=True, element_justification='center')
    window.maximize()

    # Carregar a imagem de fundo usando a biblioteca Pillow
    imagem_fundo_pil = Image.open(caminho_imagem_fundo)
    imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo_pil)

    # Exibir a imagem de fundo no Canvas
    canvas = window['-CANVAS-']
    canvas.Widget.pack(expand=True, fill='both')
    canvas.Widget.create_image(0, 0, anchor='nw', image=imagem_fundo_tk)

    while True:
        event, values = window.read()

        if event == '-CADASTRAR-':
            layout = [
                [sg.Text('Nome')],
                [sg.Input(key='-NOME-')],
                [sg.Text('Idade')],
                [sg.Input(key='-IDADE-', password_char='*')],
                [sg.Canvas(background_color=color, size=(2, 10))],
                [sg.Button('Cadastrar', key='-CADASTRAR-'), sg.Canvas(background_color=color, size=(2, 5)),
                 sg.Button('Voltar', key='-VOLTAR-')]

            ]

            window2 = sg.Window('Cadastrar Funcionário', layout)

            # Loop para validação de login
            while True:
                event, values, = window2.read()

                nome = values['-NOME-']
                idade = values['-IDADE-']

                if event == '-VOLTAR-':
                    window2.close()
                    break
        if event == sg.WINDOW_CLOSED:
            window2.close()
            break

    window.close()
    window2.close()

'''def cadastrar():


    layout = [
        [sg.Text('Nome')],
        [sg.Input(key='-NOME-')],
        [sg.Text('Idade')],
        [sg.Input(key='-IDADE-', password_char='*')],
        [sg.Button('Cadastrar', key='-CADASTRAR-'),sg.Canvas(background_color=color, size=(2, 2)), sg.Button('Voltar', key='-VOLTAR-')]


    ]

    window = sg.Window('Cadastrar Funcionário', layout)

    # Loop para validação de login
    while True:
        event, values, = window.read()

        nome = values['-NOME-']
        idade = values['-IDADE-']

        if event == '-VOLTAR-':
            window.close()
            break'''

#log()
menu()



#[sg.Canvas(background_color= color, size=(15, 10))],
'''sg.Canvas(background_color= color, size=(1112, 10)),'''
#[sg.Canvas(background_color=color, size=(15, 230))]
'''sg.Canvas(background_color= color, size=(1112, 10))'''
#[sg.Canvas(background_color= color, size=(15, 270))],