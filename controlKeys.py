import pygame

pygame.init()

clk = pygame.time.Clock()

size = width,height = 389, 187
screen = pygame.display.set_mode(size)
background_image = pygame.image.load("sn.jpg").convert()
background_image = pygame.transform.scale(background_image, (width, height))
frameRect = pygame.Rect((0, 0), (width, height))

crosshair = pygame.Surface((10,10))
pygame.draw.circle(crosshair, pygame.Color("black"),(5,5),5,0)

crosshairb = pygame.Surface((10,10))
pygame.draw.circle(crosshairb, pygame.Color("red"),(5,5),5,0)

while True:

    pygame.event.pump()
    
    screen.blit(background_image, (0, 0))

    Keys = pygame.key.get_pressed()

    if Keys[pygame.K_x]: screen.blit(crosshair, (298, 70))

    if Keys[pygame.K_a]: screen.blit(crosshair, (330, 96))

    if Keys[pygame.K_z]: screen.blit(crosshair, (260, 96))

    if Keys[pygame.K_s]: screen.blit(crosshair, (298, 115))

    x = -1 if Keys[pygame.K_LEFT] else 1 if Keys[pygame.K_RIGHT] else 0

    y = -1 if Keys[pygame.K_UP] else 1 if Keys[pygame.K_DOWN] else 0

    screen.blit(crosshairb, ((x*20)+93-5, (y*20)+99-5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.flip()

    clk.tick(60)
