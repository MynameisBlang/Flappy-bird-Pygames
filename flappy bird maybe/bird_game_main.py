import pygame
from sys import exit
from random import randint, choice
from player import *
from pipe import *

# initiation of game
pygame.init()
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption('Wannabe Flappy Bird')
clock = pygame.time.Clock()
game_active = False
# score and time
time = 0
score_time = 0
def score():
    game_time = int(pygame.time.get_ticks()/ 3000) - time
    return game_time

# background
sky = pygame.image.load('flappy bird maybe/graphics/Sky.png').convert()
sky_scaled = pygame.transform.scale(sky,(600, 800))

# font
font = pygame.font.Font('flappy bird maybe/graphics/Pixeltype.ttf', 50)
text_surface = font.render('Not Flappy Bird', False, 'White')
text_rect = text_surface.get_rect(center = (300, 100))
instruction_text = font.render('Space to start flying', False, 'White')
instruction_text_rect = instruction_text.get_rect(center = (300, 650))

# player
player_surface = pygame.image.load('flappy bird maybe/flying/frame-1.png')
player_surface_scale= pygame.transform.scale(player_surface, (220, 173.6))
player_rect = player_surface_scale.get_rect(center = (300,400))
player = pygame.sprite.GroupSingle()
player.add(Player())

# pipes/obstacle
obstacle = pygame.sprite.Group()

# collision function
def collision():
    if pygame.sprite.spritecollide(player.sprite,obstacle, False):      
        obstacle.empty()
        return False
    else:
        return True

# events
obstacle_spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_spawn_timer, 1750)

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # spawning the pipes
        if game_active:
            if event.type == obstacle_spawn_timer:
                obstacle.add(Pipe('pipe1'))
                obstacle.add(Pipe('pipe2'))
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    time = int((pygame.time.get_ticks()/3000))
            
    if game_active:

        # drawing the characters and the background
        screen.blit(sky_scaled, (0,0))
        obstacle.draw(screen)
        player.draw(screen)

        # updating the state of the player and pipes
        player.update() 
        obstacle.update()
        game_active = collision()
        # keeping up the score
        score_time =  score()
    else:
        
        screen.fill('Black')
        screen.blit(player_surface_scale, player_rect)
        screen.blit(text_surface, text_rect)
        score_end = font.render(f'Your Score: {score_time}', False, 'White')
        score_end_rect = score_end.get_rect( center = (300, 650))
        if score_time == 0:
            screen.blit(instruction_text, instruction_text_rect)
        else:
            screen.blit(score_end, score_end_rect)


    pygame.display.update()
    clock.tick(60)