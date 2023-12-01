# MazeAI
Personally Designed A* Search Algorithm Maze - the application uses Pygame for graphical representation of the maze, the start and target points, and the path found.

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

## A* Algorithm Mechanism in Our Implementation

The A* search algorithm used in our maze is implemented in the function a_star(maze, start, end). Here's a breakdown of the code that ties back to the original mechanism of the A* algorithm:

The heuristic function h(p1, p2) represents h(n) in our A* algorithm. It calculates the Manhattan distance between two points p1 and p2. This is an estimate of the cost from n to the goal.

The frontier is our priority queue in the A* algorithm. It stores nodes on the frontier of the search, with the priority being the lowest cost function f(n) = g(n) + h(n). It is initialized with the start node with a cost of 0.

The dictionary came_from keeps track of the path from the start node to any node n, serving the purpose of maintaining a tree of paths originating at the start node.

The dictionary cost_so_far keeps track of g(n), the cost of the path from the start node to n. It is initialized with the start node having a cost of 0.

Inside the while loop, the node current with the lowest f(n) value is removed from the frontier, and we check if the goal has been reached.

If current is not the goal, we calculate next, the potential future positions from current. We then update g(n) and h(n) for these next nodes, add them to the frontier if they are valid (not a wall and within the maze), and update came_from for path tracking.

The function retrieve_path(came_from, start, end) is used to reconstruct the path from the start to the goal using the came_from dictionary. It starts at the goal and follows the path backwards to the start, adding each node to path. This follows the principle of A* where the least-cost path from a given initial node to one goal node is found.

## Usage

To run the application:
1. Ensure you have the necessary dependencies installed. This includes Python and Pygame.

2. Clone this repository to your local machine.

3. Navigate to the cloned directory via the terminal.

4. Run python main.py.
   
When the application is running, you'll see the maze displayed in a new window. The start point, target point, and the shortest path between them (calculated using the A* search algorithm) are highlighted.
