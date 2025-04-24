# coding: utf-8
import pyautogui
from time import sleep
import requests
from paises import paises_en_pt

club_id = 31  # Example club ID, replace with actual ID
url = f"https://transfermarkt-api.fly.dev/clubs/{club_id}/players"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for player in data['players']:
        nome = player['name']
        lado = player['foot']
        posicao = player['position']
        idade = player.get('age')

        # 1- Clicar e digitar o nome
        pyautogui.click(864,411, duration=0)
        pyautogui.write(nome)

        # 2- Clicar e selecionar o lado (pé direito ou esquerdo)
        if lado == 'right':
            print('Destro, etapa pulada') # Se for destro, essa etapa pode ser pulada
        elif lado == 'left':
            pyautogui.click(1073,446, duration=0)
            pyautogui.click(1073,485, duration=0)
        elif lado == False:
            print('Padronizado como destro, etapa pulada')

        # 3- Clicar e selecionar a posição
        if posicao == 'Goalkeeper':
            print('Goleiro, etapa pulada') # Se for goleiro, essa etapa pode ser pulada
        elif posicao == 'Left-Back':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,484, duration=0)
            # Para colocar do lado esquerdo:
            pyautogui.click(1073,446, duration=0)
            pyautogui.click(1073,485, duration=0)
        elif posicao == 'Right-Back':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,484, duration=0)
            # Para colocar do lado direito:
            pyautogui.click(1073,446, duration=0)
            pyautogui.click(1073,465, duration=0)

        elif posicao == 'Centre-Back' or posicao == 'Sweeper' or posicao == 'Defender':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,500, duration=0)

        elif posicao == 'Central Midfield' or posicao == 'Defensive Midfield' or posicao == 'Attacking Midfield' or posicao == 'Midfielder':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,520, duration=0)
        elif posicao == 'Left Midfield':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,520, duration=0)
            # Para colocar do lado esquerdo:
            pyautogui.click(1073,446, duration=0)
            pyautogui.click(1073,485, duration=0)
        elif posicao == 'Right Midfield':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,520, duration=0)
            # Para colocar do lado direito:
            pyautogui.click(1073,446, duration=0)
            pyautogui.click(1073,465, duration=0)

        elif posicao == 'Left Winger':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,540, duration=0)
            # Para colocar do lado esquerdo:
            pyautogui.click(1073,446, duration=0)
            pyautogui.click(1073,485, duration=0)
        elif posicao == 'Right Winger':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,540, duration=0)
            # Para colocar do lado direito:
            pyautogui.click(1073,446, duration=0)
            pyautogui.click(1073,465, duration=0)
        elif posicao == 'Centre-Forward' or posicao == 'Striker' or posicao == 'Second Striker':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,540, duration=0)

        # 4- Clicar e selecionar a nacionalidade
        nacionalidade_en = player.get('nationality')[0]
        nacionalidade_pt = paises_en_pt.get(nacionalidade_en, nacionalidade_en)
        pyautogui.click(878,486, duration=0)
        pyautogui.write(nacionalidade_pt)
        pyautogui.click(813,636, duration=0)

        # 5- Clicar e selecionar a característica 1
        # necessário pensar um método para selecionar a característica por meio de estatísticas mais avançadas disponíveis no TM
        # pyautogui.click(885,529, duration=1)

        # 6- Clicar e selecionar a característica 2
        # necessário pensar um método para selecionar a característica por meio de estatísticas mais avançadas disponíveis no TM
        # pyautogui.click(1109,529, duration=1)

        # 7- Clicar o mouse de acordo com a idade
        if idade is None:
            print('Sem idade, etapa pulada')
        else:
            try:
                if int(idade) == 20:
                    print('20 anos, etapa pulada') # Se tiver 20 anos, essa etapa pode ser pulada
                elif int(idade) < 20: # Se tiver menos de 20 anos:
                    for variable in range(20 - int(idade)):
                        print(variable)
                        pyautogui.click(848,556, duration=0)
                elif int(idade) > 20: # Se tiver mais de 20 anos:
                    for variable in range(int(idade) - 20):
                        print(variable)
                        pyautogui.click(1042,556, duration=0)
            except ValueError:
                print('Idade inválida, etapa pulada')

        # 8- Clicar no botão OK
        pyautogui.click(896,641, duration=0)
        sleep(1)