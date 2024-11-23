"""composants/obstacles.py"""
from abc import ABC, abstractmethod
import random
import pygame

cell_size = 10


class Obstacle(ABC):
    """Base abstract class for all obstacles"""
    def __init__(self, position, size):
        self.position = position  # [x, y]
        self.size = size  # [width, height]
        self.color = pygame.Color(255, 0, 0)  # Red by default
    
    @abstractmethod
    def update(self):
        """Update obstacle state - to be implemented by subclasses"""
        pass
    
    def get_bounds(self):
        """Return the bounds of the obstacle"""
        return (self.position[0], self.position[1], 
                self.position[0] + self.size[0], 
                self.position[1] + self.size[1])
    
    def collides_with_point(self, point):
        """Check if a point collides with the obstacle"""
        bounds = self.get_bounds()
        return (bounds[0] <= point[0] <= bounds[2] and 
                bounds[1] <= point[1] <= bounds[3])
    
    def collides_with(self, position, size):
        """Check if a given position collides with the obstacle."""
        return not (
            position[0] + size[0] <= self.position[0] or
            position[0] >= self.position[0] + self.size[0] or
            position[1] + size[1] <= self.position[1] or
            position[1] >= self.position[1] + self.size[1]
        )
    
    def draw(self, surface):
        """Draw the obstacle on the given surface"""
        pygame.draw.rect(surface, self.color, 
                        pygame.Rect(self.position[0], self.position[1], 
                                  self.size[0], self.size[1]))

class StaticObstacle(Obstacle):
    """Immovable obstacles like buildings or barriers"""
    def __init__(self, position, size):
        super().__init__(position, size)
        self.color = pygame.Color(139, 69, 19)  # Brown color for static obstacles
    
    def update(self):
        """Static obstacles don't move, so no update needed"""
        pass

class DynamicObstacle(Obstacle):
    """Movable obstacles like other vehicles."""
    def __init__(self, position, size, velocity, bounds):
        super().__init__(position, size)
        self.velocity = velocity  # [vx, vy]
        self.bounds = bounds  # [xmin, ymin, xmax, ymax]
        self.color = pygame.Color(255, 0, 0)  # Red for dynamic obstacles

    def update(self, obstacles):
        """Update the position of the dynamic obstacle while avoiding collisions."""
        # Predict the next position
        next_position = [
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1]
        ]

        # Check collisions with bounds
        if next_position[0] < self.bounds[0] or next_position[0] + self.size[0] > self.bounds[2]:
            self.velocity[0] = -self.velocity[0]  # Reverse horizontal direction
        if next_position[1] < self.bounds[1] or next_position[1] + self.size[1] > self.bounds[3]:
            self.velocity[1] = -self.velocity[1]  # Reverse vertical direction

        # Check collisions with other obstacles
        for obstacle in obstacles:
            if obstacle is not self and obstacle.collides_with(next_position, self.size):
                self.velocity[0] = -self.velocity[0]  # Reverse direction on collision
                self.velocity[1] = -self.velocity[1]
                return  # Stop updating if collision occurs

        # Update position if no collisions
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
