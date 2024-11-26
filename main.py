"""main.py"""
import pygame
import random

from composants.taxi import Taxi
from composants.obstacle import StaticObstacle, DynamicObstacle

car_speed = 15
window_x = 1400
window_y = 740
cell_size = 10

# Colors
black = pygame.Color(40, 40, 40)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

# Initialise pygame
pygame.init()
pygame.display.set_caption('Projet IA : Taxi Intelligent')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

obstacles = []

def generate_valid_position(obstacles, size):
    """Generate a valid position that does not overlap with obstacles."""
    while True:
        position = [
            random.randrange(0, (window_x // cell_size)) * cell_size,
            random.randrange(0, (window_y // cell_size)) * cell_size
        ]
        if not any(
            obstacle.collides_with(position, size) for obstacle in obstacles
        ):
            return position

# Static buildings
buildings = [
    StaticObstacle([300, 200], [100, 100]),
    StaticObstacle([800, 400], [150, 80]),
    StaticObstacle([500, 600], [120, 90]),
    StaticObstacle([200, 500], [100, 120]),
    StaticObstacle([900, 300], [140, 100]),
    StaticObstacle([1000, 100], [180, 150]),
    StaticObstacle([400, 100], [130, 90])
]
obstacles.extend(buildings)

# Generate initial positions for moving vehicles
moving_vehicles = []
for _ in range(5):  # 5 dynamic vehicles total
    position = generate_valid_position(buildings, [20, 20])
    direction = [random.choice([-1, 1]), random.choice([-1, 1])]  # Random initial direction
    moving_vehicles.append(DynamicObstacle(position, [20, 20], direction, [0, 0, window_x, window_y]))
obstacles.extend(moving_vehicles)

# Initialise taxi
start_position = [100, 50]

# Generate a valid destination point
destination = generate_valid_position(buildings, [cell_size, cell_size])
taxi = Taxi(start_position, destination, obstacles)

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update dynamic obstacles
    for vehicle in moving_vehicles:
        vehicle.update(obstacles)

    # Move the taxi
    taxi.move()

    # Check if Taxi reached destination
    if taxi.position == taxi.destination:
        taxi.update_destination()

    # Rendering
    game_window.fill(black)

    # Draw static obstacles
    for building in buildings:
        pygame.draw.rect(game_window, building.color, pygame.Rect(building.position[0], building.position[1], building.size[0], building.size[1]))

    # Draw dynamic obstacles
    for vehicle in moving_vehicles:
        pygame.draw.rect(game_window, vehicle.color, pygame.Rect(vehicle.position[0], vehicle.position[1], vehicle.size[0], vehicle.size[1]))

    # Draw taxi
    pygame.draw.rect(game_window, green, pygame.Rect(taxi.position[0], taxi.position[1], cell_size, cell_size))

    # Draw destination
    pygame.draw.rect(game_window, white, pygame.Rect(taxi.destination[0], taxi.destination[1], cell_size, cell_size))

    pygame.display.update()
    fps.tick(car_speed)
