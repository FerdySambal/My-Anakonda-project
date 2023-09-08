import PySimpleGUI as sg

layout = [[sg.Button('Klik saya')]]

window = sg.Window('Contoh program PySimpleGUI', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Klik Saya':
        print('Tombol diklik')

window.close()