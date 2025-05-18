# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 
    
    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Set the groups as containers for Player
    Player.containers = (updatable, drawable)
    
    # Create player - it will automatically add itself to the containers
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update all updatable objects
        updatable.update(dt)
        
        # Clear the screen
        screen.fill("black")
        
        # Draw all drawable objects
        for entity in drawable:
            entity.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()