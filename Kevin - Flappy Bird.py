import pygame, os

W = 144
H = 256

game_folder = os.path.dirname(__file__)

bg_img = pygame.image.load(os.path.join(game_folder, 'images', 'sprite_000.png'))

print(pygame.init())

screen = pygame.display.set_mode((W,H))

gameContinue = True
while gameContinue == True:
    for event in pygame.event.get():
        print(event)


quit()
