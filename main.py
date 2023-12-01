import pygame
import sys
from game_constants import *
from pathfinding import a_star, retrieve_path
from maze import Maze

# Draw the game
def draw(win, maze, path):
    # Draw maze
    maze.draw(win, SIZE)

    # Draw path
    for node in path:
        pygame.draw.rect(win, GREEN, (node[0]*SIZE, node[1]*SIZE, SIZE, SIZE))

    pygame.display.update()

def main(win, width):
    pygame.init()
    clock = pygame.time.Clock()

    maze = Maze()
    came_from, cost_so_far = a_star(maze.maze, AI_POS, PLAYER_POS)

    # Check if a path exists
    if PLAYER_POS in came_from:
        path = retrieve_path(came_from, AI_POS, PLAYER_POS)
    else:
        print("No path found!")
        return

    while True:
        draw(win, maze, path)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)

WIN = pygame.display.set_mode((WIDTH, WIDTH))
main(WIN, WIDTH)