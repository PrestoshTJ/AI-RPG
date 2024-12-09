import pygame
import sys

#Dungeon Map



#Building Map


#Plains Map

screen_width, screen_height = 800, 608
TILE_SIZE = 32

tiles_x = screen_width // TILE_SIZE
tiles_y = screen_height // TILE_SIZE

plain_map = [
    [0 if (x == 0 or x == tiles_x - 1 or y == 0 or y == tiles_y - 1) else 1 for x in range(tiles_x)] 
    for y in range(tiles_y)
]

plain_map[11][16] = 0

map_data = plain_map

TILE_SIZE = 32
tile_images = {
    0: pygame.Surface((TILE_SIZE, TILE_SIZE)),
    1: pygame.Surface((TILE_SIZE, TILE_SIZE)),
    2: pygame.Surface((TILE_SIZE, TILE_SIZE))
}

tile_images[0].fill((0, 0, 0))
tile_images[1].fill((51, 204, 51))  

