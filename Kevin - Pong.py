import pygame, random

#NEED TO DO, C TO CONINUTE, Q TO QUIT, LINE 102

W = 400
H = 600
FPS = 60
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
PINK = (255, 73, 176)
RED = (255,0,0)

print(pygame.init())
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Kevin - Pong 2025")

font = pygame.font.Font(None, 16)  #setting up font family, and font size
lives = 3
livesText = font.render("Lives: " + str(lives), True, WHITE) #setting up what you want to print/display
livesTextRect = livesText.get_rect() #making a rectangle for the text
livesTextRect.center = (W//2, 10) #set the text location

score = 0
scoreText =  font.render("Score: " + str(score), True, WHITE)
scoreTextRect = scoreText.get_rect()
scoreTextRect.center = (W//2,30)

ballsize = 10
ballx = ballsize
bally = ballsize
ballspeedx = 5
ballspeedy = 5

pw = 80
ph = 20
px = W/2 - pw/2
py = 570
pspeed = 0
movementspeed = 5

gameContinue = True
while gameContinue == True:

    for event in pygame.event.get():
        #print(event)

        if event.type == pygame.QUIT:
            gameContinue = False
            
        #=====CONTROLS=====
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            pspeed = movementspeed
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            pspeed = movementspeed * - 1
        else:
            pspeed = 0

#====PADDLE=====
    px += pspeed
    if px < 0:
        px = 5
    if px > W-pw:
        px = W-pw-5

#====BALL======

    ballx += ballspeedx
    if ballx > W-ballsize or ballx < 0+ballsize:
        ballspeedx = -ballspeedx

    bally += ballspeedy
    
    #ball-top collision
    if bally < 0+ballsize:
        ballspeedy = -ballspeedy

    #ball-bottom collision
    if bally > H-ballsize:
        bally = ballsize
        ballx = ballsize
        lives -= 1
        livesText = font.render("Lives: " + str(lives), True, WHITE) #setting up what you want to print/display
        livesTextRect = livesText.get_rect() #making a rectangle for the text
        livesTextRect.center = (W//2, 10) #set the text location
        screen.blit(livesText, livesTextRect)
        if lives == 0:
            gamePaused = True
            while gamePaused == True:
                gameoverText = font.render("C to continue, Q to quit", True, RED, WHITE) #setting up what you want to print/display
                gameoverTextRect = gameoverText.get_rect() #making a rectangle for the text
                gameoverTextRect.center = (W//2, H//2)
                screen.blit(gameoverText, gameoverTextRect)
                pygame.display.update()
                
                for event in pygame.event.get():
                    if pygame.key.get_pressed()[pygame.K_q]:
                        gameContinue = False
                        gamePaused = False
                    if pygame.key.get_pressed()[pygame.K_c]:
                        lives = 3
                        score = 0
                        ballx = ballsize
                        bally = ballsize
                        ballspeedx = 5
                        ballspeedy = 5

                        livesText = font.render("Lives: " + str(lives), True, WHITE)
                        livesTextRect = livesText.get_rect() 
                        scoreText =  font.render("Score: " + str(score), True, WHITE)
                        scoreTextRect = scoreText.get_rect()

                        livesTextRect.center = (W//2, 10)
                        scoreTextRect.center = (W//2,30)

                        screen.blit(livesText, livesTextRect)
                        screen.blit(scoreText, scoreTextRect)
                        
                        gamePaused = False
                        
    #ball-paddle collision
    if bally > py - ballsize and ballx > px and ballx < px + pw:
        bally = py - ballsize
        ballspeedy = -ballspeedy
        ballspeedx = random.randint(0,5)
        score += 1
        scoreText =  font.render("Score: " + str(score), True, WHITE)
        scoreTextRect = scoreText.get_rect()
        scoreTextRect.center = (W//2,30)
        
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (px,py,pw,ph))
    pygame.draw.circle(screen, PINK, (ballx,bally), ballsize)
    screen.blit(livesText, livesTextRect) #blit is another type of render, specifc object at a time.
    screen.blit(scoreText, scoreTextRect)
    pygame.display.update() #render
    clock.tick(FPS)

pygame.quit()
sys.exit()
