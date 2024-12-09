import pygame
import sys
from player import Player, NPC
from maps import map_data, TILE_SIZE, tile_images
from ai import generate

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption("RPG")

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# text = generate("You are an NPC that dictates the story of the grand RPG adventure the protagonist begins. There is a dungeon map, plains map which we are in, and a inside a building map to work with.", "Hello! Introduce me to the world!")
text = "Sample text"
# npc = NPC(text.content)
npc = NPC(text)
all_sprites.add(npc)

def draw_map():
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            screen.blit(tile_images[tile], (x * TILE_SIZE, y * TILE_SIZE))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            if abs(player.rect.centerx - npc.rect.centerx) < 100 and abs(player.rect.centery - npc.rect.centery) < 100:
                if not npc.show_bubble:
                    npc.toggle_bubble()
                else:
                    npc.next_chunk()
    
    draw_map()
    all_sprites.update()
    all_sprites.draw(screen)
    npc.draw_text_bubble(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
