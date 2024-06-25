import pygame
import sys 
import random
from constant import *


def ball_animation():
    global BALL_SPEED_X
    global BALL_SPEED_Y
    global player_score
    global opponent_score
    
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y
    
    if ball.bottom >= SCREEN_HEIGHT or ball.top <= 0:
        BALL_SPEED_Y *= -1
    if ball.left <= 0:
        player_score += 1
        ball_restart()
    if ball.right >= SCREEN_WIDTH:
        opponent_score += 1
        ball_restart()
        
    if ball.colliderect(player) or ball.colliderect(opponent):
        BALL_SPEED_X *= -1

def player_animation():    
    player.y += player_speed
    
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT


def ball_restart():
    global BALL_SPEED_X
    global BALL_SPEED_Y
    
    ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    BALL_SPEED_Y *= random.choice((1, -1))
    BALL_SPEED_X *= random.choice((1, -1))
    
        
def opponent_animation():
    if opponent.top <= ball.y:
        opponent.top += opponent_speed
    if opponent.bottom >= ball.y:
        opponent.bottom -= opponent_speed
        
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

ball = pygame.Rect(SCREEN_WIDTH / 2 - 15, SCREEN_HEIGHT / 2 - 15, 30, 30)
player = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT / 2 - 70, 10, 140)
opponent = pygame.Rect(20, SCREEN_HEIGHT / 2 - 70, 10, 140)

player_speed = 0
opponent_speed = 7

player_score = 0
opponent_score = 0

game_font = pygame.font.Font('freesansbold.ttf', 28)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += PLAYER_SPEED
            if event.key == pygame.K_UP:
                player_speed -= PLAYER_SPEED
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= PLAYER_SPEED
            if event.key == pygame.K_UP:
                player_speed += PLAYER_SPEED 
            
    ball_animation()
    player_animation()
    opponent_animation()
    
    screen.fill(BG_COLOR)
    pygame.draw.aaline(surface=screen, color=LIGHT_GREY, start_pos=(SCREEN_WIDTH/2, 0), end_pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT))
    pygame.draw.rect(surface=screen, color=LIGHT_GREY, rect=player)
    pygame.draw.rect(surface=screen, color=LIGHT_GREY, rect=opponent)
    pygame.draw.ellipse(surface=screen, color=LIGHT_GREY, rect=ball)
    
    player_text = game_font.render(f'{player_score}', True, LIGHT_GREY)
    screen.blit(player_text, (570, 290))
    
    opponent_text = game_font.render(f'{opponent_score}', True, LIGHT_GREY)
    screen.blit(opponent_text, (515, 290))
    
    pygame.display.update()
    clock.tick(FPS)
