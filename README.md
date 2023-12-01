# MazeAI
A* Search Algorithm Maze - the application uses Pygame for graphical representation of the maze, the start and target points, and the path found.

## Features
Maze UI: 

The application provides a graphical user interface that displays the maze. The maze is randomly generated each time the program runs.

A* Pathfinding: 

The application uses the A* search algorithm to find the shortest path from the start point to the target point. This path is highlighted in green.

Pygame Interface: 

The application uses Pygame, a set of Python modules designed for writing video games, for its graphical user interface.

## Project Structure

README.md: The markdown file provides a detailed description of the project, its features, and instructions on how to set up and run the project.

game_constants.py: This Python script defines all the constants used across the project. This could include things like default sizes, colors, or other constants.

main.py: This is the primary entry point for the application. It handles the initialization and the main game loop.

maze.py: This Python script contains the logic for generating and managing the maze. It may include classes or functions for creating the maze, checking if a path is blocked, etc.

mazeui.py (WIP): This Python script is responsible for rendering the maze to the screen using Pygame. It may include classes or functions for drawing the walls, paths, and other elements of the maze.

pathfinding.py: This Python script contains the implementation of the pathfinding algorithm (such as A*). It is likely to include functions for calculating the shortest path from the start point to the end point in the maze.

## Usage

To run the application:
1. Ensure you have the necessary dependencies installed. This includes Python and Pygame.

2. Clone this repository to your local machine.

3. Navigate to the cloned directory via the terminal.

4. Run python main.py.
   
When the application is running, you'll see the maze displayed in a new window. The start point, target point, and the shortest path between them (calculated using the A* search algorithm) are highlighted.
