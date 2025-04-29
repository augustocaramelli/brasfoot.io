import pyautogui
from time import sleep
import requests
import random
from paises import paises_en_pt
import pyperclip

club_id = 64779  # Example club ID, replace with actual ID
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
        pyperclip.copy(nome)
        pyautogui.hotkey('ctrl', 'v')

        # 2- Clicar e selecionar o lado (pé direito ou esquerdo)
        if lado == 'right':
            print('Destro, etapa pulada') # Se for destro, essa etapa pode ser pulada
        elif lado == 'left':
            pyautogui.click(1073,446, duration=0)
            pyautogui.click(1073,485, duration=0)
        elif lado == False:

            lista = ['right', 'left']
            lado = random.choice(lista)
            if lado == 'right':
                print('Destro randomizado')
            elif lado == 'left':
                pyautogui.click(1073,446, duration=0)
                pyautogui.click(1073,485, duration=0)
                print('Canhoto randomizado')

        # 3- Clicar e selecionar a posição e as características
        if posicao == 'Goalkeeper':
            print('Goleiro, etapa pulada') # Se for goleiro, essa etapa pode ser pulada

            lista = ['Col', 'DPe', 'Ref', 'SGo']
            caracteristicas = random.sample(lista, 2)
            print(nome, caracteristicas)
            if caracteristicas[0] == 'Col':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,545, duration=0)
            elif caracteristicas[0] == 'DPe':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,565, duration=0)
            elif caracteristicas[0] == 'Ref':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,585, duration=0)
            elif caracteristicas[0] == 'SGo':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,600, duration=0)
            
            if caracteristicas[1] == 'Col':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,545, duration=0)
            elif caracteristicas[1] == 'DPe':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,565, duration=0)
            elif caracteristicas[1] == 'Ref':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,585, duration=0)
            elif caracteristicas[1] == 'SGo':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,600, duration=0)

                
        elif posicao == 'Left-Back':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,484, duration=0)
            # Para colocar do lado esquerdo:
            pyautogui.click(1073,446, duration=0)
            pyautogui.click(1073,485, duration=0)

            lista = ['Cru', 'Des', 'Mar', 'Pas', 'Vel']
            caracteristicas = random.sample(lista, 2)
            print(nome, caracteristicas)
            if caracteristicas[0] == 'Cru':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,590, duration=0)
            elif caracteristicas[0] == 'Des':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,605, duration=0)
            elif caracteristicas[0] == 'Mar':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,660, duration=0)
            elif caracteristicas[0] == 'Pas':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,680, duration=0)
            elif caracteristicas[0] == 'Vel':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,715, duration=0)

            if caracteristicas[1] == 'Cru':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,590, duration=0)
            elif caracteristicas[1] == 'Des':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,605, duration=0)
            elif caracteristicas[1] == 'Mar':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,660, duration=0)
            elif caracteristicas[1] == 'Pas':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,680, duration=0)
            elif caracteristicas[1] == 'Vel':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,715, duration=0)
            

        elif posicao == 'Right-Back':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,484, duration=0)
            # Para colocar do lado direito:
            pyautogui.click(1073,446, duration=0)
            pyautogui.click(1073,465, duration=0)

            lista = ['Cru', 'Des', 'Mar', 'Pas', 'Vel']
            caracteristicas = random.sample(lista, 2)
            print(nome, caracteristicas)
            if caracteristicas[0] == 'Cru':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,590, duration=0)
            elif caracteristicas[0] == 'Des':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,605, duration=0)
            elif caracteristicas[0] == 'Mar':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,660, duration=0)
            elif caracteristicas[0] == 'Pas':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,680, duration=0)
            elif caracteristicas[0] == 'Vel':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,715, duration=0)

            if caracteristicas[1] == 'Cru':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,590, duration=0)
            elif caracteristicas[1] == 'Des':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,605, duration=0)
            elif caracteristicas[1] == 'Mar':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,660, duration=0)
            elif caracteristicas[1] == 'Pas':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,680, duration=0)
            elif caracteristicas[1] == 'Vel':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,715, duration=0)


        elif posicao == 'Centre-Back' or posicao == 'Sweeper' or posicao == 'Defender':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,500, duration=0)

            lista = ['Cab', 'Des', 'Mar', 'Res']
            caracteristicas = random.sample(lista, 2)
            print(nome, caracteristicas)
            if caracteristicas[0] == 'Cab':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,570, duration=0)
            elif caracteristicas[0] == 'Des':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,605, duration=0)
            elif caracteristicas[0] == 'Mar':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,660, duration=0)
            elif caracteristicas[0] == 'Res':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,695, duration=0)

            if caracteristicas[1] == 'Cab':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,570, duration=0)
            elif caracteristicas[1] == 'Des':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,605, duration=0)
            elif caracteristicas[1] == 'Mar':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,660, duration=0)
            elif caracteristicas[1] == 'Res':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,695, duration=0)


        elif posicao == 'Defensive Midfield':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,520, duration=0)

            lista1 = ['Cab', 'Des', 'Mar', 'Res']
            caracteristica1 = random.choice(lista1)
            lista2 = ['Cab', 'Des', 'Fin', 'Mar', 'Pas', 'Res', 'Vel']
            caracteristica2 = random.choice(lista2)
            if caracteristica1 == caracteristica2:
                while caracteristica1 == caracteristica2:
                    caracteristica2 = random.choice(lista2)
            print(nome, caracteristica1, caracteristica2)

            if caracteristica1 == 'Cab':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,570, duration=0)
            elif caracteristica1 == 'Des':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,605, duration=0)
            elif caracteristica1 == 'Mar':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,660, duration=0)
            elif caracteristica1 == 'Res':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,695, duration=0)

            if caracteristica2 == 'Cab':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,570, duration=0)
            elif caracteristica2 == 'Des':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,605, duration=0)
            elif caracteristica2 == 'Fin':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,645, duration=0)
            elif caracteristica2 == 'Mar':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,660, duration=0)
            elif caracteristica2 == 'Pas':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,680, duration=0)
            elif caracteristica2 == 'Res':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,695, duration=0)
            elif caracteristica2 == 'Vel':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,715, duration=0)


        elif posicao == 'Attacking Midfield':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,520, duration=0)

            lista = ['Arm', 'Dri', 'Fin', 'Pas']
            caracteristicas = random.sample(lista, 2)
            print(nome, caracteristicas)
            if caracteristicas[0] == 'Arm':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,555, duration=0)
            elif caracteristicas[0] == 'Dri':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,625, duration=0)
            elif caracteristicas[0] == 'Fin':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,645, duration=0)
            elif caracteristicas[0] == 'Pas':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,680, duration=0)

            if caracteristicas[1] == 'Arm':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,555, duration=0)
            elif caracteristicas[1] == 'Dri':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,625, duration=0)
            elif caracteristicas[1] == 'Fin':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,645, duration=0)
            elif caracteristicas[1] == 'Pas':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,680, duration=0)


        elif posicao == 'Central Midfield' or posicao == 'Midfielder':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,520, duration=0)

            lista = ['Arm', 'Des', 'Dri', 'Fin', 'Mar', 'Pas', 'Vel']
            caracteristicas = random.sample(lista, 2)
            print(nome, caracteristicas)

            if caracteristicas[0] == 'Arm':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,555, duration=0)
            elif caracteristicas[0] == 'Des':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,605, duration=0)
            elif caracteristicas[0] == 'Dri':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,625, duration=0)
            elif caracteristicas[0] == 'Fin':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,645, duration=0)
            elif caracteristicas[0] == 'Mar':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,660, duration=0)
            elif caracteristicas[0] == 'Pas':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,680, duration=0)
            elif caracteristicas[0] == 'Vel':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,715, duration=0)

            if caracteristicas[1] == 'Arm':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,555, duration=0)
            elif caracteristicas[1] == 'Des':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,605, duration=0)
            elif caracteristicas[1] == 'Dri':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,625, duration=0)
            elif caracteristicas[1] == 'Fin':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,645, duration=0)
            elif caracteristicas[1] == 'Mar':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,660, duration=0)
            elif caracteristicas[1] == 'Pas':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,680, duration=0)
            elif caracteristicas[1] == 'Vel':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,715, duration=0)


        elif posicao == 'Left Midfield':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,520, duration=0)
            # Para colocar do lado esquerdo:
            pyautogui.click(1073,446, duration=0)
            pyautogui.click(1073,485, duration=0)

            lista = ['Dri', 'Fin', 'Pas', 'Vel']
            caracteristicas = random.sample(lista, 2)
            print(nome, caracteristicas)
            if caracteristicas[0] == 'Dri':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,625, duration=0)
            elif caracteristicas[0] == 'Fin':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,645, duration=0)
            elif caracteristicas[0] == 'Pas':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,680, duration=0)
            elif caracteristicas[0] == 'Vel':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,715, duration=0)

            if caracteristicas[1] == 'Dri':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,625, duration=0)
            elif caracteristicas[1] == 'Fin':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,645, duration=0)
            elif caracteristicas[1] == 'Pas':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,680, duration=0)
            elif caracteristicas[1] == 'Vel':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,715, duration=0)


        elif posicao == 'Right Midfield':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,520, duration=0)
            # Para colocar do lado direito:
            pyautogui.click(1073,446, duration=0)
            pyautogui.click(1073,465, duration=0)

            lista = ['Dri', 'Fin', 'Pas', 'Vel']
            caracteristicas = random.sample(lista, 2)
            print(nome, caracteristicas)
            if caracteristicas[0] == 'Dri':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,625, duration=0)
            elif caracteristicas[0] == 'Fin':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,645, duration=0)
            elif caracteristicas[0] == 'Pas':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,680, duration=0)
            elif caracteristicas[0] == 'Vel':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,715, duration=0)

            if caracteristicas[1] == 'Dri':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,625, duration=0)
            elif caracteristicas[1] == 'Fin':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,645, duration=0)
            elif caracteristicas[1] == 'Pas':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,680, duration=0)
            elif caracteristicas[1] == 'Vel':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,715, duration=0)


        elif posicao == 'Left Winger':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,540, duration=0)
            # Para colocar do lado esquerdo:
            pyautogui.click(1073,446, duration=0)
            pyautogui.click(1073,485, duration=0)

            lista = ['Dri', 'Fin', 'Pas', 'Vel']
            caracteristicas = random.sample(lista, 2)
            print(nome, caracteristicas)
            if caracteristicas[0] == 'Dri':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,625, duration=0)
            elif caracteristicas[0] == 'Fin':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,645, duration=0)
            elif caracteristicas[0] == 'Pas':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,680, duration=0)
            elif caracteristicas[0] == 'Vel':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,715, duration=0)

            if caracteristicas[1] == 'Dri':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,625, duration=0)
            elif caracteristicas[1] == 'Fin':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,645, duration=0)
            elif caracteristicas[1] == 'Pas':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,680, duration=0)
            elif caracteristicas[1] == 'Vel':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,715, duration=0)


        elif posicao == 'Right Winger':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,540, duration=0)
            # Para colocar do lado direito:
            pyautogui.click(1073,446, duration=0)
            pyautogui.click(1073,465, duration=0)

            lista = ['Dri', 'Fin', 'Pas', 'Vel']
            caracteristicas = random.sample(lista, 2)
            print(nome, caracteristicas)
            if caracteristicas[0] == 'Dri':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,625, duration=0)
            elif caracteristicas[0] == 'Fin':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,645, duration=0)
            elif caracteristicas[0] == 'Pas':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,680, duration=0)
            elif caracteristicas[0] == 'Vel':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,715, duration=0)

            if caracteristicas[1] == 'Dri':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,625, duration=0)
            elif caracteristicas[1] == 'Fin':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,645, duration=0)
            elif caracteristicas[1] == 'Pas':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,680, duration=0)
            elif caracteristicas[1] == 'Vel':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,715, duration=0)


        elif posicao == 'Centre-Forward' or posicao == 'Striker':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,540, duration=0)

            lista = ['Cab', 'Dri', 'Fin', 'Res']
            caracteristicas = random.sample(lista, 2)
            print(nome, caracteristicas)
            if caracteristicas[0] == 'Cab':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,570, duration=0)
            elif caracteristicas[0] == 'Dri':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,625, duration=0)
            elif caracteristicas[0] == 'Fin':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,645, duration=0)
            elif caracteristicas[0] == 'Res':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,695, duration=0)

            if caracteristicas[1] == 'Cab':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,570, duration=0)
            elif caracteristicas[1] == 'Dri':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,625, duration=0)
            elif caracteristicas[1] == 'Fin':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,645, duration=0)
            elif caracteristicas[1] == 'Res':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,695, duration=0)


        elif posicao == 'Second Striker':
            pyautogui.click(862,443, duration=0)
            pyautogui.click(862,540, duration=0)

            lista = ['Dri', 'Fin', 'Pas', 'Res']
            caracteristicas = random.sample(lista, 2)
            print(nome, caracteristicas)
            if caracteristicas[0] == 'Dri':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,625, duration=0)
            elif caracteristicas[0] == 'Fin':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,645, duration=0)
            elif caracteristicas[0] == 'Pas':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,680, duration=0)
            elif caracteristicas[0] == 'Res':
                pyautogui.click(880,525, duration=0)
                pyautogui.click(880,695, duration=0)

            if caracteristicas[1] == 'Dri':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,625, duration=0)
            elif caracteristicas[1] == 'Fin':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,645, duration=0)
            elif caracteristicas[1] == 'Pas':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,680, duration=0)
            elif caracteristicas[1] == 'Res':
                pyautogui.click(1100,525, duration=0)
                pyautogui.click(1100,695, duration=0)


        # 4- Clicar e selecionar a nacionalidade
        nacionalidade_en = player.get('nationality')[0]
        nacionalidade_pt = paises_en_pt.get(nacionalidade_en, nacionalidade_en)

        if nacionalidade_en == 'N/A':
            print('Sem nacionalidade, etapa pulada')
        else:
            pyautogui.click(878,486, duration=0)
            pyautogui.write(nacionalidade_pt)
            pyautogui.click(813,636, duration=0)

        # 5- Clicar o mouse de acordo com a idade
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
        sleep(0)