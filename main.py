import pygame

pygame.init()
tela = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
rodando = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tela.fill("white")
    pygame.display.flip()

    clock.tick(60)  

pygame.quit()