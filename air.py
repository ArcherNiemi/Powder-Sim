import block
import pygame

AIR_COLOR = (173, 216, 230)

class Air(block.Block):
    def __init__(self, location):
        self.color = AIR_COLOR
        super().__init__(location)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.location[0], self.location[1], self.size, self.size))
    
    def move(self, block_locations):
        downLocation = (self.location[0], self.location[1] + self.size)
        downLeftLocation = (self.location[0] - self.size, self.location[1] + self.size)
        downRightLocation = (self.location[0] + self.size, self.location[1] + self.size)
        leftLocation = (self.location[0] - self.size, self.location[1])
        rightLocation = (self.location[0] + self.size, self.location[1])
        upLocation = (self.location[0], self.location[1] - self.size)
        upLeftLocation = (self.location[0] - self.size, self.location[1] - self.size)
        upRightLocation = (self.location[0] + self.size, self.location[1] - self.size)

        locations = (downLocation, downLeftLocation, downRightLocation, leftLocation, rightLocation, upLocation, upLeftLocation, upRightLocation)

        for i in range(len(locations)):
            if(not(locations[i] in block_locations) and locations[i][1] < 800 and locations[i][0] >= 0 and locations[i][0] < 800):
                self.location = locations[i]
                break
        