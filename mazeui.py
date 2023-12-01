import pygame
import os
from maze import Maze
from game_constants import PLAYER_POS

# Define constants
CELL_SIZE = 50
ROWS, COLS = len(Maze.maze), len(Maze.maze[0])
WIDTH, HEIGHT = CELL_SIZE * COLS, CELL_SIZE * ROWS

# Load images
FLOOR_IMG = pygame.image.load(os.path.join('assets', 'floor.png'))
WALL_IMG = pygame.image.load(os.path.join('assets', 'wall.png'))
PLAYER_IMG = pygame.image.load(os.path.join('assets', 'player.png'))
# AI_IMG = pygame.image.load(os.path.join('assets', 'ai.png'))  # Commented out

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            x, y = j * CELL_SIZE, i * CELL_SIZE
            if cell == 0:
                win.blit(FLOOR_IMG, (x, y))
            elif cell == 1:
                win.blit(WALL_IMG, (x, y))

def draw(win, grid, player_pos):
    draw_grid(win, grid)
    # Draw player
    x, y = player_pos[0] * CELL_SIZE, player_pos[1] * CELL_SIZE
    win.blit(PLAYER_IMG, (x, y))
    # Don't draw AI
    # x, y = ai_pos[0] * CELL_SIZE, ai_pos[1] * CELL_SIZE
    # win.blit(AI_IMG, (x, y))

def main(win, grid, player_pos):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(win, grid, player_pos)
        pygame.display.update()

    pygame.quit()

# Initialize Pygame
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Start the game
main(WIN, Maze.maze, PLAYER_POS)