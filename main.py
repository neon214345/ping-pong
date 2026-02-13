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
    def __init__(self, image_path, pos, speed, size, control: dict):
        super().__init__(image_path, pos, speed, size)
        self.control = control

    def update(self, keys):
        if keys[self.control['Up']]:
            self.rect.y -= self.speed
        if keys[self.control['Down']]:
            self.rect.y += self.speed

window = pygame.display.set_mode(SCREEN_SIZE)

timer = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font(None, FONT_SIZE)
lose1 = font.render(PLAYER1_LOSE_TEXT, True, FONT_COLOR)
lose2 = font.render(PLAYER2_LOSE_TEXT, True, FONT_COLOR)

player1 = Player(PLAYER_IMG, PLAYER1_POS, PLAYER_SPEED, PLAYER_SIZE, PLAYER1_CONTROL)
player2 = Player(PLAYER_IMG, PLAYER2_POS, PLAYER_SPEED, PLAYER_SIZE, PLAYER2_CONTROL)

ball = GameSprite(BALL_IMG, BALL_POSE, BALL_SPEED, BALL_SIZE)
ball_dx = 3
ball_dy = 3

entity = [player1, player2, ball]

run = True
pause = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if not pause:
        window.fill(SCREEN_COLOR)
        for en in entity:
            en.draw(window)
        keys = pygame.key.get_pressed()
        player1.update(keys)
        player2.update(keys)


        ball.rect.x += ball_dx
        ball.rect.y += ball_dy

        if pygame.sprite.collide_rect(player1, ball):

            ball_dx = abs(ball_dx)
        if pygame.sprite.collide_rect(player2, ball):
            ball_dx = -abs(ball_dx)

        if ball.rect.y < 0:
            ball_dy = abs(ball_dy)
        
        if ball.rect.y > SCREEN_SIZE[1] - BALL_SIZE[1]:
            ball_dy = -abs(ball_dy)
        
        if ball.rect.x < 0:
            pause = True
            window.blit(lose1, FONT_POSE)

        if ball.rect.x > SCREEN_SIZE[0] - BALL_SIZE[0]:
            pause = True
            window.blit(lose2, FONT_POSE)

    pygame.display.update()
    timer.tick(TICK_RATE)

