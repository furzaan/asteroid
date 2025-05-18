import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent class's constructor with x, y, and PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)
        
        # Initialize rotation to 0
        self.rotation = 0
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # Override the parent's draw method (required)
        # We'll implement actual drawing logic later
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def update(self, dt):
        # Override the parent's update method (required)
        # We'll implement actual update logic later
        pass
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Rotate left (counterclockwise): use negative dt
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # Rotate right (clockwise): use positive dt
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
    def move(self, dt):
        # Create a vector pointing forward (0, 1) and rotate it by the player's rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        
        # Multiply by speed and dt, then add to position
        self.position += forward * PLAYER_SPEED * dt