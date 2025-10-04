import block
import pygame

SAND_COLOR = (194, 178, 128)

class Sand(block.Block):
    def __init__(self, location):
        self.color = SAND_COLOR
        super().__init__(location)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.location[0], self.location[1], self.size, self.size))
    
    def move(self, block_locations):
        downLocation = (self.location[0], self.location[1] + self.size)
        leftLocation = (self.location[0] - self.size, self.location[1] + self.size)
        rightLocation = (self.location[0] + self.size, self.location[1] + self.size)

        locations = (downLocation, leftLocation, rightLocation)

        for i in range(len(locations)):
            if(not(locations[i] in block_locations) and locations[i][1] < 800 and locations[i][0] >= 0 and locations[i][0] < 800):
                self.location = locations[i]
                break
        