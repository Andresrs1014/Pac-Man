import pygame
import constantes
class Personaje_2():
    
    def __init__(self, x, y):
        self.shape = pygame.Rect(0, 0, constantes.WIDTH_PLAYER, constantes.HEIGHT_PLAYER)
        self.shape.center = (x, y)
        
    def draw(self, interfaz):
        pygame.draw.circle(
            interfaz,
            (255, 0, 0),
            self.shape.center,
            self.shape.width // 2
        )
        
    def movimiento(self, delta_x2, delta_y2):
        self.shape.x = self.shape.x + delta_x2
        self.shape.y = self.shape.y + delta_y2  