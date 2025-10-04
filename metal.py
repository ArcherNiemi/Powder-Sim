import block
import pygame

METAL_COLOR = (60,60,60)

class Metal(block.Block):
    def __init__(self, location):
        self.color = METAL_COLOR
        super().__init__(location)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.location[0], self.location[1], self.size, self.size))
    
    def move(self, block_locations):
        pass