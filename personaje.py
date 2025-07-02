import pygame
import constantes
class Personaje():
    
    def __init__(self, x, y, animation):
        
        # -- Voltear al personaje, dependiendo de que tecla se use
        self.flip = False
        
        # -- Cargar la animacion del personaje, segun los sprites que hallamos puesto
        self.animation = animation
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animation[self.frame_index]
        self.shape = pygame.Rect(0,0, constantes.WIDTH_PLAYER, constantes.HEIGHT_PLAYER)
        self.shape.center = (x, y)
    
    def update(self):
        cooldow_animation = 100
        self.image = self.animation[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldow_animation:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
            if self.frame_index >= len(self.animation):
                self.frame_index = 0
        
    def draw(self, interfaz):
        image_flip = pygame.transform.flip(self.image, self.flip, flip_y=False)
        
        interfaz.blit(image_flip, self.shape)
        #pygame.draw.circle(interfaz, (255, 255, 0), self.shape.center, self.shape.width // 2,)
        
    def movimiento(self, delta_x, delta_y):
        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y
        if delta_x < 0:
            self.flip = True
            
        if delta_x > 0:
            self.flip = False
            
        
        
            
    