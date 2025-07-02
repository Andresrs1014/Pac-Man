import pygame
import sys
import constantes
from personaje import Personaje
from obstacle import Obstacle




pygame.init()

font = pygame.font.Font('freesansbold.ttf', 20)
pygame.display.set_caption('Pac-Man')


'''' -- Escalado de imagen -- 

 Funcion para escalar todas las imagenes que pongamos en nuestra animacion. '''

def scalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image, size=(w*scale, h*scale))
    return new_image

# -- Animacion Personaje -- 

animation = []

for i in range(2):
    img =  pygame.image.load(f'assets/images/characters/Pac-Man/Pac-Man000{i}.png')
    img = scalar_img(img, constantes.SCALA_PLAYER)
    animation.append(img)
    





# -- Mapas -- 



# -- Obstaculos --

obstacle = Obstacle(constantes.color_obstacle, 200, 100, 500, 400)
obstacle_2 = Obstacle(constantes.color_obstacle_2, 300, 50, 200, 450)


# -- Personajes --
player = Personaje(50, 50, animation)



# -- FPS -- 
clock = pygame.time.Clock()


# -- Tamaño de la ventana -- 
window = pygame.display.set_mode((constantes.WINDOW_WIDTH, constantes.WINDOW_HEIGHT))

# -- Bucle Principal -- 
running = True
while running:



    
    
    # -- Dibujado --
    
    window.fill(constantes.COLOR_BG)
    window.blit(obstacle.image, obstacle.rect)
    window.blit(obstacle_2.image, obstacle_2.rect) 
    
    
    
    # -- Eventos de cierre -- 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    
    keys = pygame.key.get_pressed()
            
    # -- Movimiento Personajes -- 
            
    delta_x = 0
    delta_y = 0
    
    
    if keys[pygame.K_LEFT]:
        delta_x = -constantes.PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        delta_x = constantes.PLAYER_SPEED
    if keys[pygame.K_UP]:
        delta_y = -constantes.PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        delta_y = constantes.PLAYER_SPEED    
        
        
    
    

    

    
            
    
    
    # -- Importaciones clases Personajes --         
        
    player.movimiento(delta_x, delta_y) 
    player.draw(window)
    player.update()
    
    
            
    clock.tick(constantes.FPS)       
    pygame.display.update()
            
            
pygame.quit()