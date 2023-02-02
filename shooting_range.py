import pygame 
import sys          
 # Initialize the game engine
pygame.init()
# Set the height and width of the screen
screen = pygame.display.set_mode((800, 500))
# create the clock object.  determines how fast the screen updates
clock = pygame.time.Clock()
# load background image
wood_bg = pygame.image.load("Wood_BG.png")
# Loop until the user clicks the close button.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Copy image to screen:
    screen.blit(wood_bg, (0, 0))
    # Set the screen background
    pygame.display.update()
    # game will run at 120 frames per second. Stops the game from running too fast
    clock.tick(120)


