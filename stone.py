import block
import pygame

STONE_COLOR = (120, 120, 120)

class Stone(block.Block):
    def __init__(self, location):
        self.color = STONE_COLOR
        super().__init__(location)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.location[0], self.location[1], self.size, self.size))
    
    def move(self, block_locations):
        downLocation = (self.location[0], self.location[1] + self.size)
        if(not(downLocation in block_locations) and downLocation[1] < 810):
            self.location = downLocation