import pygame, wx
from pygame.locals import *
from wx import *
pygame.init()

def main():
	white = (255,255,255)
	black = (0,0,0)
	savenumber = 1
	red = (255,0,0)
	green = (0,255,0)
	blue = (0,0,255)
	userColor = (0,0,0)
	go = True
	draw = False
	erase = False
	radius = 25
	color = black
	(rx,ry) = (0,25)
	(gx,gy) = (0,60)
	(bx,by) = (0,95)
	keepGoing2 = True
	mouseOn = False
	redX = 0
	greenX = 0
	blueX = 0
	userColor = (redX,greenX,blueX)

	pygame.mouse.set_cursor(*pygame.cursors.broken_x)

	screen = pygame.display.set_mode((640,480))
	pygame.display.set_caption("Jpaint")
	screen.fill(white)
	while go == True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					color = black
				if event.key == pygame.K_LEFT:
					color = red
				if event.key == pygame.K_UP:
					color = green
				if event.key == pygame.K_RIGHT:
					color = blue
				if event.key == K_c:
					screen.fill(white)


				if event.key == K_s:
					saveName = 'pic{0}.jpg'.format(savenumber)
					savenumber += 1
					pygame.image.save(screen,saveName)


				if event.key == K_e:
					color = white

				if event.key == K_f:
					screen.fill(color)
				
			if pygame.mouse.get_pressed() == (1,0,0):
				(x,y) = pygame.mouse.get_pos()
				draw = True
				pygame.draw.circle(screen,color,(x,y),radius)

			if pygame.mouse.get_pressed() == (0,0,1):
				(x,y) = pygame.mouse.get_pos()
				erase = True
				pygame.draw.circle(screen,white,(x,y),radius)

			if pygame.mouse.get_pressed() == (0,1,0):
				screen.fill(white);

			if event.type == MOUSEBUTTONUP:
				draw = False
				erase = False

			if event.type == MOUSEMOTION:
				if draw:
					(x,y) = pygame.mouse.get_pos()
					pygame.draw.circle(screen,color,(x,y),radius)
				
			pygame.display.flip()

			if event.type == QUIT:
				go = False
main()