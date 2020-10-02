import pygame,sys
from pygame.locals import *

catx =400
caty =300
screen = 0

def myquit():

	pygame.quit()
	sys.exit(0)

def check_input(events):
	global catx,caty,screen

	for event in events:
		if event.type == QUIT:
			myquit()
		else:
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					myquit()
				elif event.key == K_LEFT :
					catx -=5;
					print("move rect left")
				elif event.key == K_RIGHT :
					catx +=5
					print("move rect right")
				elif event.key == K_UP :
					caty -=5
					print("move rect up")
				elif event.key == K_DOWN :
					caty +=5
					print("move rect down")
				else:
					print(event.key)
	screen.fill((0,0,0))
	pygame.draw.rect(screen,(255,255,255),(catx,caty,50,10))
	pygame.display.update()


def main():
	global screen

	pygame.init()

	SCREEN_WIDTH = 800
	SCREEN_SIZE = 600
	window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_SIZE))
	pygame.display.set_caption("Paamu - The game")
	screen = pygame.display.get_surface()

	pygame.display.update()

	while True:
		check_input(pygame.event.get())

main()