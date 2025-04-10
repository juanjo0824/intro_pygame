import random
import pygame
import sys 

rojo = (255, 0,00)
azul = (0,0,255)
verde = (25, 245, 19)
cafe = (99, 64, 6)
amarillo = (255, 236, 0)
morado = (166, 0, 255)

pygame.init()

ventana = pygame.display.set_mode((500,500))

pygame.display.set_caption("Los  cuadrados que robota")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTOS = 3
YY = 300
MOVIMIENTOS = 3

while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)

    XX = XX + MOVIMIENTOS
    YY = YY + MOVIMIENTOS


    if XX >= 450:
        XX = 450
        MOVIMIENTOS = -4
    elif XX <= 0:
        XX = 0
        MOVIMIENTOS = 4
    if YY >= 450:
        YY = 450
        MOVIMIENTOS = -4
    elif YY <= 0:
        YY = 0
        MOVIMIENTOS = 4

    pygame.draw.rect(ventana, rojo, (XX, 00,  50, 50))
    pygame.draw.rect(ventana, amarillo, (XX, 450, 50, 50))
    pygame.draw.rect(ventana, morado, (XX, XX, 50, 50))
    pygame.draw.rect(ventana, verde,(00, YY, 50, 50))
    pygame.draw.rect(ventana, cafe,(450, YY, 50, 50))
    color_alaetorio=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    pygame.draw.rect(ventana,color_alaetorio,(200,200,100,100))
    pygame.display.flip() 

