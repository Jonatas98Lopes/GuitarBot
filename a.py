import pyautogui as pg
from time import sleep
import threading

def pressionar_botao_verde():
	while True:
		botao_verde = pg.pixelMatchesColor(793,606, (0,152,0))
		if botao_verde:
			pg.press("a")
			
	

def pressionar_botao_vermelho():
	while True:
		botao_vermelho = pg.pixelMatchesColor(886,608, (255,0,0))
		if botao_vermelho:
			pg.press("s")
			


def pressionar_botao_amarelo():
	while True:
		botao_amarelo = pg.pixelMatchesColor(977,608, (244,244,2))
		if botao_amarelo:
			pg.press("j")
			
	
def pressionar_botao_azul():
	while True:
		botao_azul = pg.pixelMatchesColor(1069,606, (0,152,255))
		if botao_azul:
			pg.press("k")
			
	

def pressionar_botao_laranja():
	while True:
		botao_laranja = pg.pixelMatchesColor(1155,605, (255,101,0))
		if botao_laranja:
			pg.press("l") 
			

""" for i in range(10):
	nivel = pg.locateCenterOnScreen('./images/greenButton.png')
	print(nivel)
	nivel = pg.locateCenterOnScreen('./images/redButton.png')
	print(nivel)
	nivel = pg.locateCenterOnScreen('./images/yellowButton.png')
	print(nivel)
	nivel = pg.locateCenterOnScreen('./images/blueButton.png')
	print(nivel)
	nivel = pg.locateCenterOnScreen('./images/orangeButton.png')
	print(nivel)
 """
pg.click(1302,431, duration=0.8)



t1 = threading.Thread(target=pressionar_botao_verde)
t2 = threading.Thread(target=pressionar_botao_vermelho)
t3 = threading.Thread(target=pressionar_botao_amarelo)
t4 = threading.Thread(target=pressionar_botao_azul)
t5 = threading.Thread(target=pressionar_botao_laranja) 

t1.start()
t2.start()
t3.start()
t4.start()
t5.start() 


t1.join()
t2.join()
t3.join()
t4.join()
t5.join() 
		
	