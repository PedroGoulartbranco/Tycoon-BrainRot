import pygame

pygame.init()
tela = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()
rodando = True

fonte = pygame.font.Font(None, 40)

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.fill("blue")

    pygame.draw.rect(tela, "white", (50, 300, 300, 50), 0, 0)
    pygame.draw.rect(tela, "white", (50, 400, 300, 50), 0, 0)

    texto_logar = fonte.render("Logar", True, "black")
    texto_novo_jogador = fonte.render("Novo Player", True, "black")
    texto_menu = fonte.render("Menu", True, "black")

    tela.blit(texto_logar, (160, 315))
    tela.blit(texto_novo_jogador, (130, 415))

    pygame.display.flip()

    clock.tick(60)  

pygame.quit()