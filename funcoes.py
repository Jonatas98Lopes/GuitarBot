import pyperclip, pyautogui
from time import sleep
from random import randint
import tkinter as tk

def digitar_caracteres_especiais(frase):
	"""
  Essa função nos permite digitar textos com caracteres especiais como: à, á, é, ç...
  
  Ela aceita um único parametro chamado 'frase' onde frase é uma string.
  """
	pyperclip.copy(frase)
	pyautogui.hotkey('ctrl', 'v')
	
def pausar():
	"""
  Faz o programa ficar parado de 2 até 10 segundos. O tempo em que o programa ficará pausado é definido aleatoriamente.
  
  Esta função não aceita parâmetros.
  """
	sleep(randint(2, 10))
	
def repousar():
	"""
  Faz o programa ficar parado de 20 até 30 segundos. O tempo em que o programa ficará pausado é definido aleatoriamente.
  
  Esta função não aceita parâmetros.
  """
	sleep(randint(20, 30))

def parar_temporariamente():
	"""
  Faz o programa ficar parado de 24 até 30 horas. O tempo em que o programa ficará pausado é definido aleatoriamente.
  
  Esta função não aceita parâmetros.
  """
	sleep(randint(86400, 108000))
	
def informar_fim_do_programa(mensagem):
	"""
	Exibe uma mensagem personalizada ao usuário. Essa mensagem dura 10 segundos na tela e logo desaparace.

	Essa função só aceita um argumento que é a mensagem a ser exibida ao usuário.
	"""
	janela = tk.Tk()
	janela.title("Informação")
	janela.geometry('500x100')

	label = tk.Label(janela, text=mensagem)

	label.pack(pady=20)
	janela.after(10 * 1000, janela.destroy) 
	janela.mainloop()