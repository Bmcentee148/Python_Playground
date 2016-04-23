# Opens a blank pygame window. Good to use as a template for new programs.
# @author Brian McEntee

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

BG_COLOR = WHITE

pygame.init()

# Set width and height of the screen
WIDTH = 700
HEIGHT = 500
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

# Loop until user clicks the closed button
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

RECT_WIDTH = 25
RECT_HEIGHT = 50
START_POSITION = [50,50]
speed = [4, 4] # [x_change, y_change]
rect_position = START_POSITION


# Class Definitions
class Block(pygame.sprite.Sprite) :

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

    def update(self) :
        
        rect_position[0] += speed[0]
        rect_position[1] += speed[1]

        if rect_position[0] > WIDTH - RECT_WIDTH or rect_position[0] < 0 :
            speed[0] *= -1
        if rect_position[1] > HEIGHT - RECT_HEIGHT or rect_position[1] < 0 :
            speed[1] *= -1

        self.rect.move(speed)
        
my_block = Block(BLACK, 50, 50)
blocksprite = pygame.sprite.RenderPlain(my_block)
# --------- Main Program Loop -------------
while not done :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            done = True

    # ----- Game Logic Goes Here -----
    #update_rect_position()
    blocksprite.update()
    # ----- Screen Clearing Code Goes Here -----

    screen.fill(BG_COLOR)

    # ----- Drawing Code Goes Here -----
    #pygame.draw.rect(screen, BLACK, 
      #  [rect_position[0], rect_position[1], RECT_WIDTH, RECT_HEIGHT])

    blocksprite.draw(screen)
    # ----- Update Screen With What Was Drawn
    pygame.display.flip()

    # ----- Limit to 60 frames a second
    clock.tick(60)

# Close the window and quit
pygame.quit()
