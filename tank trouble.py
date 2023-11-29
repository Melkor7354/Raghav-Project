import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tank Trouble")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up tank
tank_size = 50
tank_x, tank_y = width // 2, height // 2
tank_speed = 5

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle tank movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and tank_x > 0:
        tank_x -= tank_speed
    if keys[pygame.K_RIGHT] and tank_x < width - tank_size:
        tank_x += tank_speed
    if keys[pygame.K_UP] and tank_y > 0:
        tank_y -= tank_speed
    if keys[pygame.K_DOWN] and tank_y < height - tank_size:
        tank_y += tank_speed

    # Draw background
    screen.fill(white)

    # Draw tank
    pygame.draw.rect(screen, black, (tank_x, tank_y, tank_size, tank_size))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)