import pygame
import sys 

rojo = (255, 0,00)
azul = (0,0,255)

pygame.init()

ventana = pygame.display.set_mode((400,400))

pygame.display.set_caption("El cuadrado que robota")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTOS = 3 

while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)

    XX = XX + MOVIMIENTOS

    if XX >= 320:
        XX = 320
        MOVIMIENTOS = -3
    elif XX <= 0:
        XX = 0
        MOVIMIENTOS:3

    pygame.draw.rect(ventana, rojo, (XX, 200, 80, 80))
    pygame.display.flip() 