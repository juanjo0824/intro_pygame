import pygame
import sys
import random
import math

negro = (0,0,0)
blanco = (255,255,255)
cian = (0,255,255)
naranja = (255,165,0)
verde = (0, 255, 0)
amarillo = (240, 255, 0)
rojo = (194, 11, 11)
dorado = (213, 173, 25) 
marron = (218, 113, 15)
azul = (2, 6, 149) 
aguamarina = (4, 253, 91)
color_alaetorio=(random.randint(0,255),random.randint(0,255),random.randint(0,255))


#Colores del tren

aguamarina_tren = (4, 253, 91)
dorado_tren = (213, 173, 25) 
amarillo_tren = (240, 255, 0)
naranja_tren = (255,165,0)
rojo_tren = (255, 0, 0)
cafe_tren = (207, 130, 43)
azul_tren = (47, 91, 239)
verde_tren = (20, 175, 67)
negro_tren = (0,0,0)
blanco_tren = (255,255,255)
pygame.init()

ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("tren")

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill(aguamarina)

    fuente_arial = pygame.font.SysFont("Arial", 30, 1, 1)
    texto = fuente_arial.render("Colegio San Jose de Guanenta", 1, blanco)
    ventana.blit(texto, (35, 30))

    fuente_arial = pygame.font.SysFont("Arial", 20, 1, 0)
    texto = fuente_arial.render("Especialidad Sistemas", 1, rojo)
    ventana.blit(texto, (150, 70))

    YY = 230
    MOVIMIENTO = 10

    YY = YY + MOVIMIENTO

    if YY >= 150:
        YY = 150
        MOVIMIENTO = -10
    elif YY <= 0:
        YY = 0
        MOVIMIENTO = 10

    # sol
    pygame.draw.circle(ventana, rojo, (90, YY), 30, 0)
    pygame.draw.circle(ventana, amarillo, (90, YY), 25, 0)


    #frente(ciculo)
    pygame.draw.circle(ventana, negro_tren, (135, 360), 50, 0)

    # Tren
    pygame.draw.rect(ventana, azul_tren, ((150, 300), (250, 130)), 100)
    pygame.draw.rect(ventana, dorado, ((290, 200), (100, 80)), 0)
    pygame.draw.rect(ventana, azul_tren, ((270, 200), (130, 100)), 20)


    fuente_arial = pygame.font.SysFont("Arial", 20, 1, 0)
    texto = fuente_arial.render("Juanjo", 1, negro)
    ventana.blit(texto, (180, 360))


    pygame.draw.rect(ventana,blanco, ((50,100), (400,390)), 1)

    #techo 
    pygame.draw.rect(ventana, rojo_tren, ((260, 180), (150, 30)), 0)
    pygame.draw.rect(ventana, naranja_tren, ((280, 150), (110, 30)), 0)

    #Frente

    pygame.draw.rect(ventana, negro, ((130, 310), (20, 110)), 0)
    pygame.draw.rect(ventana, negro, ((110, 300), (30, 130)), 0)

    #popa
    pygame.draw.rect(ventana, negro_tren, ((155, 250), (40, 50)), 0)
    pygame.draw.rect(ventana, amarillo_tren, ((140, 250), (70, 20)), 0)

    #llantas
    pygame.draw.circle(ventana, dorado_tren, (200, 440), 35, 0)
    pygame.draw.circle(ventana, rojo_tren, (280, 440), 35, 0)
    pygame.draw.circle(ventana, cafe_tren, (360, 440), 35, 0)

    pygame.draw.rect(ventana, negro, ((200, 430), (70, 20)), 0)
    pygame.draw.rect(ventana, negro, ((290, 430), (70, 20)), 0)

    # Personita
    pygame.draw.circle(ventana, amarillo, (335, 245), 35, 0)

    # Ojos
    pygame.draw.circle(ventana, blanco, (320, 240), 12, 0)
    pygame.draw.circle(ventana, blanco, (350, 240), 12, 0)

    # Pupilas
    pygame.draw.circle(ventana, marron, (350, 240), 6, 0)
    pygame.draw.circle(ventana, negro, (320, 240), 6, 0)

    # Boca
    pygame.draw.circle(ventana, rojo, (335, 260), 9, 0)

    # Cejas
    pygame.draw.line(ventana, marron, (320, 220), (330, 230), 3)
    pygame.draw.line(ventana, verde, (350, 220), (340, 230), 3)

    pygame.display.flip()