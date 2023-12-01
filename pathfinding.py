from queue import PriorityQueue
from game_constants import ROWS, COLS

def a_star(maze, start, end):
    def h(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)

    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()[1]

        if current == end:
            break

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next = (current[0] + dx, current[1] + dy)
            print(f'ROWS: {ROWS}, COLS: {COLS}, next[0]: {next[0]}, next[1]: {next[1]}')
            print(len(maze), len(maze[0]))  # print the actual dimensions of the maze
            if (0 <= next[0] < ROWS and 0 <= next[1] < COLS and
                    maze[next[1]][next[0]] == 0):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + h(end, next)
                    frontier.put((priority, next))
                    came_from[next] = current

    return came_from, cost_so_far

def retrieve_path(came_from, start, end):
    current = end
    path = []

    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()

    return path