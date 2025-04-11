import pygame
import sys
import random
import math

negro = (0,0,0)
blanco = (255,255,255)
rojo =  (255, 15, 0)
cian = (0,255,255)
color_alaetorio=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

pygame.init()

ventana = pygame.display.set_mode((500,500))
pygame.display.set_caption("Las lineas locas")

loco1 = random.randint(50,400)
loco2 = random.randint(100,4000)
loco3 = random.randint(50,400)
loco4 = random.randint(350,400)

clock = pygame.time.Clock()

while True:

    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ventana.fill(negro)

    fuente_arial = pygame.font.SysFont("Arial", 30,1,1)
    texto = fuente_arial.render("Colegio San Jose De Guanenta", 1,rojo)
    ventana.blit(texto,(35,30))

    fuente_arial = pygame.font.SysFont("Arial", 20,1,0)
    texto = fuente_arial.render("Especialidad Sistemas", 1, blanco)
    ventana.blit(texto,(150,70))

    fuente_arial = pygame.font.SysFont("Arial", 20,0,0)
    texto = fuente_arial.render("Juan Jose Delgado Benitez", 1, blanco)
    ventana.blit(texto,(10,470))


    pygame.draw.rect(ventana,blanco, ((50,100), (400,350)), 1)

    for i in range(100):

        loco1 = random.randint(50,450)
        loco2 = random.randint(100,450)
        loco3 = random.randint(50,450)
        loco4 = random.randint(100,450)

        color_alaetorio=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

        
        pygame.draw.line(ventana, color_alaetorio,(loco1,loco2), (loco3,loco4))


    pygame.display.flip()



