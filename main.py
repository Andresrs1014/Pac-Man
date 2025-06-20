import pygame
import sys
import constantes
from personaje import Personaje
from personaje_2 import Personaje_2
from obstacle import Obstacle


pygame.init()


obstacle = Obstacle(constantes.color_obstacle, 200, 100, 500, 400)
player = Personaje(50, 50)
player_2 = Personaje_2(100, 100)
clock = pygame.time.Clock()


window = pygame.display.set_mode((constantes.WINDOW_WIDTH, constantes.WINDOW_HEIGHT))

running = True

move_down = False
move_up = False
move_right = False
move_left = False

while running:
    
    window.fill(constantes.COLOR_BG)
    window.blit(obstacle.image, obstacle.rect)  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
            
    delta_x = 0
    delta_y = 0
    delta_x2 = 0
    delta_y2 = 0
    
    if keys[pygame.K_LEFT]:
        delta_x = -constantes.PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        delta_x = constantes.PLAYER_SPEED
    if keys[pygame.K_UP]:
        delta_y = -constantes.PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        delta_y = constantes.PLAYER_SPEED    
        
        
    if keys[pygame.K_a]:
        delta_x2 = -constantes.PLAYER_SPEED
    if keys[pygame.K_d]:
        delta_x2 = constantes.PLAYER_SPEED
    if keys[pygame.K_w]:
        delta_y2 = -constantes.PLAYER_SPEED
    if keys[pygame.K_s]:
        delta_y2 = constantes.PLAYER_SPEED    
    
    
    
            
        
    player.movimiento(delta_x, delta_y)
    player_2.movimiento(delta_x2, delta_y2)
    player.draw(window)
    player_2.draw(window)
    
            
    clock.tick(constantes.FPS)       
    pygame.display.update()
            
            
pygame.quit()