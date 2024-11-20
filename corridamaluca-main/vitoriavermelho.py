
import pygame
import random
tamanho = (1000,592)
tela = pygame.display.set_mode( tamanho )
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
icone = pygame.image.load("Recursos/icone.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("Corrida Maluca")
branco = (255,255,255)
vitoriaCarVermelho = pygame.image.load("Recursos/vitoriavermelho.jpg")
