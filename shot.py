import pygame
from circleshape import *
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, angle):
        super().__init__(x, y, SHOT_RADIUS)
        velocity = pygame.math.Vector2(0,1)
        velocity = velocity.rotate(angle)
        velocity *= PLAYER_SHOOT_SPEED
        self.velocity = velocity
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        