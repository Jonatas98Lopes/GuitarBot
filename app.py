import pyautogui as pg
import webbrowser
from funcoes import *


# Perguntar ao usuário qual música ele quer jogar.
# # cancao = pg.prompt(text='Qual a música que deseja jogar?', title='Música:')
cancao = 'Somewhere I Belong'
# Perguntar ao usuário em qual nível de dificuldade ele quer jogar.

# dificuldade = pg.confirm(text='Em qual nível de dificuldade quer jogar?', title='Nível de dificuldade:', buttons=['Fácil', 'Médio', 'Difícil', 'Expert'])
dificuldade = 'Fácil'

# Acessar o site: https://guitarflash.com/?lg=pt
webbrowser.open('https://guitarflash.com/?lg=pt')
repousar()
# Pesquisar a música que deseja no campo: "Buscar por"

# Apertar no botão jogar
pg.click(x=885, y=408, duration=1.5)
pausar()

pg.click(x=1266, y=588, duration=1.5)
pausar()

# Digitar a música
digitar_caracteres_especiais(cancao)
pausar()

# Clicar Enter
pg.press("enter")
pausar()

#SE A MÚSICA ESTIVER NO SITE:

musica_encontrada = pg.locateCenterOnScreen('./images/sem_imagem.png')
if musica_encontrada is None:
  	# Clicar na música
	pg.click(x=882, y=644, duration=1.5)
	pausar()

  	#Ajustar a página.
	pg.dragTo(1324,269, button='middle', duration=0.8)
	pausar()
	pg.click(1216,344, duration=1.5)
	pg.scroll(-500)
	pausar()
  	# Apertar no botão dificuldade
	pg.click(x=1267, y=672, duration=1.5)
	pausar()

	pg.dragTo(x=1204, y=672, button='middle', duration=1)
	pausar()
  	# Definir o nível de dificuldade
	if dificuldade == 'Fácil':
		pg.click(755,559, duration=1.5)
	elif dificuldade == 'Médio':
		pg.click(918,561, duration=1.5)
	elif dificuldade == 'Difícil':
		pg.click(1099,558, duration=1.5)
	else:
		pg.click(1267,558, duration=1.5)
  	# Esperar o jogo a carregar.
	repousar()

  	# Clicar na tecla: space.
	pg.press("space")
	pausar()
  	# Tentar identificar o botões
	fim_jogo = pg.locateCenterOnScreen('./images/fimDoJogo.png')
	
	botao_verde = pg.locateCenterOnScreen('./images/greenButton.png')
	botao_vermelho = pg.locateCenterOnScreen('./images/redButton.png')
	botao_amarelo = pg.locateCenterOnScreen('./images/yellowButton.png')
	botao_azul = pg.locateCenterOnScreen('./images/blueButton.png')
	botao_laranja = pg.locateCenterOnScreen('./images/orangeButton.png')
	while fim_jogo is None:

		if botao_verde is None:
			pg.press("a")
		if botao_vermelho is None:
			pg.press("s")
		if botao_amarelo is None:
			pg.press("j")
		if botao_azul is None:
			pg.press("k")
		if botao_laranja is None:
			pg.press("l")
	pg.alert(text=f'Parábens! Você conseguiu tocar a música {cancao} perfeitamente.', title='Programa encerrado:', button='Ok')
else:
	pg.alert(text='Desculpe! O Guitar Flash não possui a música que você está procurando.', title='Alerta! Música não encontrada:', button='Ok')	
 	# Se encontrar a imagem 'fim do jogo', encerre o processo.



