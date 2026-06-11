import pygame
import sys
import random

pygame.init()

WIDTH=800
HEIGHT=800

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CATCH THE TARGET")

#player = green rect
xp=100
yp=100
player_rect=pygame.Rect(100,100,100,100)

#target = red circle
target_rect=pygame.Rect(500,400,50,50)
xt = random.randrange(0,700)
yt = random.randrange(0,700)

score=0
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,36)
bigfont=pygame.font.SysFont(None,72)

#timer
start_time = pygame.time.get_ticks()

running=True
gameover=False

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running =False
    
    elapsed=(pygame.time.get_ticks()-start_time)/1000
    tl=60-elapsed
    if tl<=0:
        gameover=True
    if not gameover:
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            xp+=5
        if keys[pygame.K_LEFT]:
            xp-=5
        if keys[pygame.K_UP]:
            yp-=5
        if keys[pygame.K_DOWN]:
            yp+=5

        player_rect = pygame.Rect(xp, yp, 100, 100)
        target_rect = pygame.Rect(xt, yt, 50, 50)

        if player_rect.colliderect(target_rect):
            score+=1
            xt,yt=random.randrange(0,700), random.randrange(0,700)

        screen.fill((0,0,0))

        pygame.draw.rect(screen,(0,255,0),(xp,yp,100,100))

        pygame.draw.rect(screen,(255,0,0),(xt,yt,50,50))

        
        text1 = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(text1, (600, 10))
        text2=font.render(f"Time Left: {tl}",True,(255,255,255))
        screen.blit(text2,(600,50))

        
        clock.tick(60)
    else:
        screen.fill((0, 0, 0))
        over_text = bigfont.render("GAME OVER", True, (255, 0, 0))
        final_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
        screen.blit(over_text, (250, 250))
        screen.blit(final_text, (320, 340))

    pygame.display.update()

pygame.quit()
sys.exit()

