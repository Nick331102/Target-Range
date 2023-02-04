import pygame 
import sys          
 # Initialize the game engine
pygame.init()
# Set the height and width of the screen
screen = pygame.display.set_mode((800, 500))
# create the clock object.  determines how fast the screen updates
clock = pygame.time.Clock()
# load the images
wood_bg = pygame.image.load("Wood_BG.png")
land_bg = pygame.image.load("Land_BG.png")
water_bg = pygame.image.load("Water_BG.png")
cloud_1 = pygame.image.load("Cloud1.png")
cloud_2 = pygame.image.load("Cloud2.png")

land_position_y = 370
land_speed = 1

# Loop until the user clicks the close button.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Copy images to screen:
    screen.blit(wood_bg, (0, 0))
    screen.blit(land_bg,(0,land_position_y))
    screen.blit(water_bg,(0, 420))
    screen.blit(cloud_1,(100, 5))
    screen.blit(cloud_2,(500, 10))
    screen.blit(cloud_1,(300, 20))
    screen.blit(cloud_2,(200, 15))
    
    land_position_y -= land_speed
    
    # make land_bg move yp and down.  subtrating from land_position_y makes it move up.  Adding makes it move down
    if land_position_y == 340 or land_position_y == 370:
        land_speed *= -1
    
     # Set the screen background
    pygame.display.update()
    # game will run at 120 frames per second. Stops the game from running too fast
    clock.tick(60)


