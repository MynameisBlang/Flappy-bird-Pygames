import pygame
from random import randint
class Pipe(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        # spawn bottom pipe
        if type == 'pipe1':
            global y_position
            y_position = randint(1100, 1400)
            pipe1 = pygame.image.load('flappy bird maybe/pipe.png').convert_alpha()
            self.pipe = pygame.transform.scale(pipe1, (200, 700))
            self.pipesurf = self.pipe
            self.image = self.pipesurf
            self.rect = self.image.get_rect(midbottom = (700, y_position))
        # spawn top pipe
        elif type == 'pipe2':
            pipe2 = pygame.image.load('flappy bird maybe/pipe.png').convert_alpha()
            self.pipe = pygame.transform.scale(pipe2, (200, 700))
            self.pipe_rotate = pygame.transform.rotate(self.pipe, 180)
            self.pipesurf = self.pipe_rotate
            y_position -= 1650               
            self.image = self.pipesurf
            self.rect = self.image.get_rect(midtop = (700, y_position))
    # movement and state of the pipe
    def update(self):
        self.rect.x -= 4
        self.destroy()
    
    def destroy(self):
        if self.rect.x == -200:
            self.kill()