import PySimpleGUI as sg
import requests as requests

from FunciFrase import Exibir_frase
from random import randint
import tempfile
import os

url = 'https://i.im.ge/2023/05/26/hIGgEW.heart1.png'

response = requests.get(url)
temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
temp_file.write(response.content)
temp_file.close()

temp_file_path = temp_file.name



random = randint(1, 400)
verde = 'green'
cinza = 'gray'
#caminho = "C:\Users\digom\PycharmProjects\CursoEmVideo\Projetos\heart.png"
sg.theme('DarkBlack')


layout = [  [sg.Canvas(background_color= 'gray', size=(10, 25))],
            [sg.Text('Leia uma Frase Bonita!', justification='center', text_color='black', background_color='gray', font='Arial')],
            [sg.Canvas(background_color=cinza, size=(10, 30))],
            [sg.Image(temp_file_path, background_color='gray')],
            [sg.Canvas(background_color= 'gray', size=(10, 10))],
            [sg.Button('Exibir Frase!', size=40, button_color='white')]]


window = sg.Window('Frases De Amor', layout, element_justification='center', size=(400, 400), background_color='gray')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == 'Exibir Frase!':
        sg.popup(f'{Exibir_frase()}', title='Frases De Amor', no_titlebar=False, text_color='white', auto_close=True, auto_close_duration=10,button_type=5, relative_location=(random, random))
        break

window.close()
os.remove(temp_file.name)
