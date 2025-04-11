import pygame
import sys
import random
import math

rojo = (255, 0, 0)
azul = (0, 0, 255)
amarillo = (255, 255, 0)
verde = (0, 255, 0)
rosado = (255, 192, 203)
negro = (0,0,0)
amarillo = (0,255,0)
blanco = (255,255,255)
naranja = (255,165,0)
cian = (0,255,255)
PI = math.pi

ventana = pygame.display.set_mode((400,400))
pygame.display.set_caption("dibujar formas con pygame")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 3
YY = 100



#bucle principal del juego
while 1: 
    clock.tick(50)
    #ciclo para la detección de los eventos del juego
    for event in pygame.event.get():
        #si se hace clicl en el botón de cerrar la ventana, el juego termina
        if event.type == pygame.QUIT:
            sys.exit()
    
    #rellenar la ventana de color 
    ventana.fill(negro)

    # dibujar formas con el módulo pygame.drae

    #dibujar una linea
    pygame.draw.line(ventana,rojo,(100,100),(300,300))
    pygame.draw.line(ventana,rojo,(100,300),(300,100))

    #dibujar uan linea continua 
    #true: crea un poligono
    puntos1=[(0,0), (50,100), (100,50), (250,200), (400,400)]
    puntos2=[(200,0), (400,200), (200,400), (0,200)]
    pygame.draw.lines(ventana,azul,True,puntos1)
    pygame.draw.lines(ventana,rojo,True,puntos2)
    #dibujar un rectangulo 
    #rectangulo relleno en la coodernada esquina sup.izq(200,200()y de ancho 200 y altura 100
    pygame.draw.rect(ventana,rosado,(200,200,200,100))
    pygame.draw.rect(ventana,verde, ((100,100), (150,200)), 1)


    #dibuja un póligono 
    puntos3 = [(200,200),(250,300),(300,325),(400,350)]
    pygame.draw.polygon(ventana,amarillo,puntos3,1)

    #dibuja un círculo 
    #centro del circulo: (300,100)
    #radio del círculo:100
    #grosor contorno círculo:1
    pygame.draw.circle(ventana,blanco, (300,100), 50, 1)

    #dibujar un elipse
    pygame.draw.ellipse(ventana,naranja, (100,150,200,100), 1)

    # Arco de circunferencia 
    pygame.draw.arc(ventana, cian, (300,25,180,150), PI/2, PI,1)

    #Texto
    #Fuente de tipo Arial, tamaño 35, negrilla y cursiva.
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    #texto = fuente_arial.render("Sistemas Guanenta", 1, blanco)
    #ventana.blit(texto,(50,50))

    #actualiza la visualización de la ventana
    pygame.display.flip()
###################################
#Fin del bucle principal del juego
###################################