#Imports e recursos
import pygame
import random
pygame.init()
tamanho = (1000,592)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
icone = pygame.image.load("Recursos/icone.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("Corrida Maluca")
branco = (255,255,255)
preta = (0,0,0)
fundo = pygame.image.load("Recursos/fundo.png")
carroVermelho = pygame.image.load("Recursos/carro1.png")
carroAmarelo = pygame.image.load("Recursos/carro2.png")
carroAzul = pygame.image.load("Recursos/carro3.png")

#Movimentaações dos carros e aonde vão ficar na imagem
movXCarVermelho = 0
movXCarAmarelo = 0
movxcarAzul=0
posYCarVermelho = 50
posYCarAmarelo = 100
posycarAzul=180

#Músicas 
vitoria = pygame.mixer.Sound("Recursos/vitoria.mp3")
vitoria.set_volume(0.5)
pygame.mixer.music.load("Recursos/trilha.mp3")
pygame.mixer.music.play(-1) 
acabou = False
somDaVitoria = False

#Looping da corrida
while True:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            quit()
   
    tela.fill( branco )
    tela.blit(fundo, (0,0))
    tela.blit(carroVermelho, (movXCarVermelho,posYCarVermelho))
    tela.blit(carroAmarelo, (movXCarAmarelo,posYCarAmarelo))
    tela.blit(carroAzul, (movxcarAzul,posycarAzul))

    if not acabou :
        movXCarVermelho = movXCarVermelho + random.randint(0,10)
        movXCarAmarelo = movXCarAmarelo + random.randint(0,10)
        movxcarAzul=movxcarAzul+random.randint(0,10)
    else:
        pygame.mixer.music.stop()
        if somDaVitoria == False:
            pygame.mixer.Sound.play(vitoria)
            somDaVitoria = True


    fonte = pygame.font.Font(None, 20)
    texto = fonte.render(f"Distância Vermelho: {(movXCarAmarelo+movxcarAzul) - 1000 - movXCarVermelho}", True, (0, 0, 0),branco)
    tela.blit(texto, (800,0)) 

    fonte = pygame.font.Font(None, 20)
    texto = fonte.render(f"Distância Amarelo: {(movXCarVermelho + movxcarAzul) - 1000 - movXCarAmarelo}", True, (0, 0, 0),branco)
    tela.blit(texto, (800,20))   

    fonte = pygame.font.Font(None, 20)
    texto = fonte.render(f"Distância Azul: {(movXCarVermelho + movXCarAmarelo) - 1000 - movxcarAzul}", True, (0, 0, 0),branco)
    tela.blit(texto, (800,45))   

#Pisição de cada carrinho na segunda pista e movimentação
    if movXCarVermelho > 1000:
        movXCarVermelho = 0
        posYCarVermelho = 350
        
    if movXCarAmarelo > 1000:
        movXCarAmarelo = 0
        posYCarAmarelo = 400   

    if movxcarAzul > 1000:
        movxcarAzul = 0
        posycarAzul = 500       

            
#Determina quem ganhou     
    if posYCarVermelho == 350 and movXCarVermelho >= 900 and movXCarVermelho > movXCarAmarelo and movxcarAzul:
        tela.blit( (270,70))
        acabou = True
        
    elif posYCarAmarelo == 400 and movXCarAmarelo >= 900 and movXCarAmarelo > movXCarVermelho and movxcarAzul:
        tela.blit( (270,180))
        acabou = True

    elif posycarAzul == 500 and movxcarAzul >= 900 and movxcarAzul > movXCarAmarelo and movXCarVermelho:
        tela.blit( (270,80))
        acabou = True     
          

    
#fechamento de jogo   
    pygame.display.update()
    clock.tick(60)
pygame.quit()
    

