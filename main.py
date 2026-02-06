import pygame
from constant import *


class GameSprite(pygame.sprite.Sprite):
    SPRITE_SIZE = (65, 65)

    def __init__(self, image_path, pos, speed, size=SPRITE_SIZE):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(image_path),
            size
        )
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.speed = speed

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed


window = pygame.display.set_mode(SCREEN_SIZE)
window.fill(SCREEN_COLOR)

timer = pygame.time.Clock()

player1 = Player(PLAYER_IMG, PLAYER1_POS, PLAYER_SPEED, PLAYER_SIZE)
player2 = Player(PLAYER_IMG, PLAYER2_POS, PLAYER_SPEED, PLAYER_SIZE)

ball = GameSprite(BALL_IMG, BALL_POSE, BALL_SPEED, BALL_SIZE)

entity = [player1, player2, ball]

run = True
pause = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if not pause:
        for en in entity:
            en.draw(window)
    pygame.display.update()
    timer.tick(TICK_RATE)

