import pygame 
import sys     
import random     
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
crosshair = pygame.image.load("crosshair.png")
duck_surface = pygame.image.load("duck.png")

 # set crosshair_rect to the center of the screen   
crosshair_rect = crosshair.get_rect(center = (400, 250))


land_position_y = 370
land_speed = 1
water_position_y = 420
water_speed = .5    

# create a list of 8 duck_rect objects and place them randomly on the screen
duck_list = []
for duck in range(8):
    # randomly placed between 100 and 700 on the x axis and 100 and 250 on the y axis
    duck_position_x = random.randrange(100, 700)
    duck_position_y = random.randrange(100, 250)
    # duck
    # create a rect object that represents the size and position of the duck
    duck_rect = duck_surface.get_rect(center = (duck_position_x, duck_position_y)) 
    duck_list.append(duck_rect)


# Loop until the user clicks the close button.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center = event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for index,duct_rect in enumerate (duck_list):
                if crosshair_rect.colliderect(duct_rect):
                    del duck_list[index]
                    
            
    # Copy images to screen:
    screen.blit(wood_bg, (0, 0))
    screen.blit(land_bg,(0,land_position_y))
    screen.blit(water_bg,(0, water_position_y))
    for duct_rect in duck_list:
        screen.blit(duck_surface, duct_rect)
    screen.blit(cloud_1,(100, 5))
    screen.blit(cloud_2,(500, 10))
    screen.blit(cloud_1,(300, 20))
    screen.blit(cloud_2,(200, 15))
    screen.blit(crosshair, crosshair_rect)
    
    
    #When we subtract a negative number from a positive number, it is equivalent to adding a positive version of the negative number.  when land_speed is negative, it is equivalent to adding a positive version of land_speed and when land_speed is positive, it is equivalent to subtracting a positive version of land_speed so when land_posiiton_y is 340, land_speed becomes -1 and then 340 - (-1) is actually adding 1 to land_position_y.  When land_position_y is 370, land_speed becomes 1 and then 370 - 1 is actually subtracting 1 from land_position_y.
    land_position_y -= land_speed
    water_position_y -= water_speed
    
    # make land_bg move yp and down.  subtrating from land_position_y makes it move up.  Adding makes it move down
    if land_position_y <= 340 or land_position_y >= 370:
        land_speed *= -1
    # make water_ bg move up and down.
    if water_position_y <= 390 or water_position_y >= 420:
        water_speed *= -1
    
  
        
    
    # Set the screen background
    pygame.display.update()
    # game will run at 120 frames per second. Stops the game from running too fast
    clock.tick(120)


