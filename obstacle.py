import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self,size, color, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.recet = self.image.get_rect(topleft = (x, y))

shape = [
            'XXXXXXXXXXXx'
            'XXXXXXXXXxxx'
            'XXXXXXxxxxxx'
            'XXXXXXXXXxxx'
            'XXXXXXXXXXXX'
]