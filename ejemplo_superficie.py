# importamos la libreria pygame
import pygame
import random

# Inicializamos los modulos de pygame
pygame.init()

# Establecer titulo a la ventana 
pygame.display.set_caption("Surface")

# Establecemos las dimensiones de la ventana 
ventana = pygame.display.set_mode((400,400))

# definimos un color
rojo = random.randint(0,256)
verde = random.randint(0,256)
azul = random.randint(0,256)
color_aletorio = (rojo,verde,azul)

# Creamos una superficie

color_aletorio = pygame.Surface((200,200))

# Rellenamos la superficie de azul
color_aletorio.fill((rojo,verde,azul))

# Inserto o muevo  la superficie en la ventana
ventana.blit(color_aletorio, (100,100))

# Actualiza la visualización de la ventana
pygame.display.flip()

# Bucle del juego

while True: 
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()