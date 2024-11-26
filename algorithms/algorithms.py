"""algorithms.py"""

import heapq

window_x = 1400
window_y = 740
cell_size = 10

def a_star(start, goal, obstacles=None):
    """
    Calculate the shortest path from start to goal using the A* algorithm.
    Includes diagonal movement and obstacle avoidance.
    
    Args:
        start: Tuple of (x, y) starting position
        goal: Tuple of (x, y) goal position
        obstacles: List of Obstacle instances to avoid
    """
    if obstacles is None:
        obstacles = []
        
    def heuristic(a, b):
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])
        return max(dx, dy) + (2**0.5 - 1) * min(dx, dy)
    
    def is_valid_position(pos):
        # Check window bounds
        if not (0 <= pos[0] < window_x and 0 <= pos[1] < window_y):
            return False
        
        # Check obstacle collisions
        for obstacle in obstacles:
            if obstacle.collides_with_point(pos):
                return False
        return True
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        
        # Explore neighbors (including diagonals)
        neighbors = [
            (current[0] + cell_size, current[1]),
            (current[0] - cell_size, current[1]),
            (current[0], current[1] + cell_size),
            (current[0], current[1] - cell_size),
            (current[0] + cell_size, current[1] + cell_size),
            (current[0] + cell_size, current[1] - cell_size),
            (current[0] - cell_size, current[1] + cell_size),
            (current[0] - cell_size, current[1] - cell_size)
        ]
        
        for neighbor in neighbors:
            if not is_valid_position(neighbor):
                continue
                
            is_diagonal = (neighbor[0] != current[0] and neighbor[1] != current[1])
            movement_cost = 2**0.5 if is_diagonal else 1
            
            tentative_g_score = g_score[current] + movement_cost
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return []  # No path found