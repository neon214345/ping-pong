import pygame


class GameSprite(sprite.Sprite):
    SPRITE_SIZE = (65, 65)

    def __init__(self, image_path, pos, speed, size=SPRITE_SIZE):
        super().__init__()
        self.image = transform.scale(
            image.load(image_path),
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