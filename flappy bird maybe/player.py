import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        # loading the images for the player model
        bird_frame1 = pygame.image.load('flappy bird maybe/flying/frame-1.png').convert_alpha()
        bird_frame2 = pygame.image.load('flappy bird maybe/flying/frame-2.png').convert_alpha()
        bird_frame3 = pygame.image.load('flappy bird maybe/flying/frame-3.png').convert_alpha()
        bird_frame4 = pygame.image.load('flappy bird maybe/flying/frame-4.png').convert_alpha()
        bird_scaled_frame1= pygame.transform.scale(bird_frame1, (110, 70))
        bird_scaled_frame2= pygame.transform.scale(bird_frame2, (110, 70))
        bird_scaled_frame3= pygame.transform.scale(bird_frame3, (110, 70))
        bird_scaled_frame4= pygame.transform.scale(bird_frame4, (110, 70))
        # creating a list and to simulate the animation effect
        self.player_fly = [bird_scaled_frame1,bird_scaled_frame2, bird_scaled_frame3,bird_scaled_frame4]
        self.player_index = 0
        self.image = self.player_fly[self.player_index]
        self.rect = self.image.get_rect(midbottom = (100,400))
        self.gravity = 0
    # getting player input
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gravity = -7
    def apply_gravity(self):
        self.gravity += 0.5
        self.rect.y +=self.gravity
        if self.rect.bottom >= 800:
            self.rect.bottom = 800
        elif self.rect.top <= 0:
            self.rect.top = 0

    def animation_state(self):
        self.player_index += 0.1
        if self.player_index >= len(self.player_fly):
            self.player_index = 0
        self.image = self.player_fly[int(self.player_index)]



    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()