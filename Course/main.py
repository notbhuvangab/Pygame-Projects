import pygame,os,sys
from pygame.locals import *

red = [255,0,0]

#Pygame Initializartion

pygame.init()

#setup window
window = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake game andi idhi')

#Set up da drawing surface
screen = pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption("Paammu")
pygame.display.flip()


while True:
	for event in pygame.event.get():
		print (event)
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()	