import pygame
import block
import metal
import stone
import sand
import water
import air

pygame.init()

WIDTH, HEIGHT = 800, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Powder Sim")

FPS = 60

BG_COLOR = (0,0,0)

SELECT_SIZE = 50

SELECT_BLOCK_SIZE = 30

BLOCKS = (("metal", metal.METAL_COLOR), ("stone", stone.STONE_COLOR), ("sand", sand.SAND_COLOR), ("water", water.WATER_COLOR), ("air", air.AIR_COLOR))

def main():
    clock = pygame.time.Clock()

    currentBlocks = []
    dragging = False
    selectedBlock = "metal"

    count = 0

    running = True

    while running:
        for event in pygame.event.get():
            mousepos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and mousepos[1] <= SELECT_SIZE:
                selectedBlock = selectBlock(mousepos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
        
        roundedpos = (round(mousepos[0] / block.BLOCK_SIZE) * block.BLOCK_SIZE, round(mousepos[1] / block.BLOCK_SIZE) * block.BLOCK_SIZE)
        
        if(dragging):
            locations = [block.location for block in currentBlocks]
            if(not(roundedpos in locations)):
                if(selectedBlock == BLOCKS[0][0]):
                    currentBlocks.append(metal.Metal(roundedpos))
                elif(selectedBlock == BLOCKS[1][0]):
                    currentBlocks.append(stone.Stone(roundedpos))
                elif(selectedBlock == BLOCKS[2][0]):
                    currentBlocks.append(sand.Sand(roundedpos))
                elif(selectedBlock == BLOCKS[3][0]):
                    currentBlocks.append(water.Water(roundedpos))
                elif(selectedBlock == BLOCKS[4][0]):
                    currentBlocks.append(air.Air(roundedpos))
        
        draw(currentBlocks)
        
        if(count % 4 == 0):
            locations = [block.location for block in currentBlocks]
            for i, object in enumerate(currentBlocks):
                object.move(locations)
                locations[i] = object.location



        clock.tick(FPS)
        count += 1
    pygame.quit()

def selectBlock(pos):
    if(pos[1] >= ((SELECT_SIZE - SELECT_BLOCK_SIZE)/2) and pos[1] <= ((SELECT_SIZE - SELECT_BLOCK_SIZE)/2) + SELECT_BLOCK_SIZE):
        for i in range(len(BLOCKS)):
            if(pos[0] >= (i * SELECT_SIZE) + ((SELECT_SIZE - SELECT_BLOCK_SIZE)/2) and pos[0] <= (i * SELECT_SIZE) + ((SELECT_SIZE - SELECT_BLOCK_SIZE)/2) + SELECT_BLOCK_SIZE):
                return BLOCKS[i][0]

def draw(currentBlocks):
    screen.fill(BG_COLOR)

    for i in range(len(currentBlocks)):
        currentBlocks[i].draw(screen)

    pygame.draw.rect(screen, (20,20,20), pygame.Rect(0,0,WIDTH,SELECT_SIZE))
    for i in range(len(BLOCKS)):
        pygame.draw.rect(screen, BLOCKS[i][1], pygame.Rect((i * SELECT_SIZE) + ((SELECT_SIZE - SELECT_BLOCK_SIZE)/2),((SELECT_SIZE - SELECT_BLOCK_SIZE)/2),SELECT_BLOCK_SIZE,SELECT_BLOCK_SIZE))

    pygame.display.flip()

if __name__ == "__main__":
    main()