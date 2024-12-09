import pygame
import sys
import math
from maps import map_data, TILE_SIZE, tile_images

screen_width, screen_height = 800, 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0)) 
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        movement = [0, 0]
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            movement[0] -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            movement[0] += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            movement[1] -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            movement[1] += 1
        
        
        if movement[0] and movement[1]:
            movement[0] /= math.sqrt(2)
            movement[1] /= math.sqrt(2)
        
        movement[0] *= self.speed
        movement[1] *= self.speed

        collision = self.is_collision(movement)
        if not collision:
            self.rect.x += movement[0]
            self.rect.y += movement[1]

    def is_collision(self, movement):
        new_rect = self.rect.move(movement[0], movement[1])

        corners = [
            (new_rect.left, new_rect.top),
            (new_rect.right, new_rect.top),
            (new_rect.left, new_rect.bottom),
            (new_rect.right, new_rect.bottom),
            (new_rect.centerx, new_rect.centery)
        ]

        for corner in corners:
            tile_x = int(corner[0] // TILE_SIZE)
            tile_y = int(corner[1] // TILE_SIZE)

            if tile_x < 0 or tile_x >= len(map_data[0]) or tile_y < 0 or tile_y >= len(map_data):
                return True
            if map_data[tile_y][tile_x] == 0:
                return True

        return False

class NPC(pygame.sprite.Sprite):
    def __init__(self, text):
        super().__init__()
        self.image = pygame.Surface((50, 50)) 
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.text = text
        self.show_bubble = False
        self.text_chunks = self.chunk_text(self.text)
        self.current_chunk = 0
    
    def chunk_text(self, text, max_length=100):
        words = text.split()
        chunks = []
        current_chunk = ""
        
        for word in words:
            if len(current_chunk + " " + word) <= max_length:
                current_chunk += " " + word if current_chunk else word
            else:
                chunks.append(current_chunk)
                current_chunk = word
        
        if current_chunk:
            chunks.append(current_chunk)
        
        return chunks

    def draw_text_bubble(self, screen):
        if not self.show_bubble:
            return
        
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text_chunks[self.current_chunk], True, (255, 255, 255))
        text_width, text_height = text_surface.get_size()

        bubble_width = text_width + 20
        bubble_height = text_height + 20
        
        if bubble_width < 100:
            bubble_width = 100  
        
        bubble_x = self.rect.centerx - bubble_width // 2
        bubble_y = self.rect.top - bubble_height - 10  

        pygame.draw.rect(screen, (0, 0, 0), (bubble_x, bubble_y, bubble_width, bubble_height))  
        pygame.draw.rect(screen, (255, 255, 255), (bubble_x, bubble_y, bubble_width, bubble_height), 2)

        screen.blit(text_surface, (bubble_x + 10, bubble_y + 10))

    def toggle_bubble(self):
        self.show_bubble = not self.show_bubble
    
    def next_chunk(self):
        if self.current_chunk < len(self.text_chunks) - 1:
            self.current_chunk += 1
        else:
            self.current_chunk = 0  
            self.toggle_bubble()