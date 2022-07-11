from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
interface=[
    [sg.Text('Usuario'),sg.Input(key='usuario',size=(20,1))],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*',size=(20,1))],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]
jannela=sg.Window('Telade Login', interface)

while True:
    eventos,valores=jannela.read()
    if eventos ==sg.WINDOW_CLOSED:
        break
    if eventos =='Entrar':
        if valores['usuario']=='yasmin'and valores['senha']=='123456':
         print('Bem vindo ao nosso Curso!')