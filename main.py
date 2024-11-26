import pygame
import random
from composants.taxi import Taxi
from composants.obstacle import StaticObstacle, DynamicObstacle
from composants.control_center import ControlCenter
from composants.taxi_stop import TaxiStop

# Constants
car_speed = 15
window_x = 1400
window_y = 740
cell_size = 10

# Colors
black = pygame.Color(40, 40, 40)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

# Initialize pygame
pygame.init()
pygame.display.set_caption('Projet IA : Taxi Intelligent')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

# Static buildings (obstacles)
buildings = [
    StaticObstacle([300, 200], [100, 100]),
    StaticObstacle([800, 400], [150, 80]),
    StaticObstacle([500, 600], [120, 90]),
    StaticObstacle([200, 500], [100, 120]),
    StaticObstacle([900, 300], [140, 100]),
    StaticObstacle([1000, 100], [180, 150]),
    StaticObstacle([400, 100], [130, 90])
]

# Generate dynamic vehicles (moving obstacles)
moving_vehicles = []
for _ in range(5):  # 5 dynamic vehicles total
    position = [random.randrange(0, window_x // cell_size) * cell_size, 
                random.randrange(0, window_y // cell_size) * cell_size]
    direction = [random.choice([-1, 1]), random.choice([-1, 1])]  # Random initial direction
    moving_vehicles.append(DynamicObstacle(position, [20, 20], direction, [0, 0, window_x, window_y]))

# Initialize taxi stops
taxi_stops = [TaxiStop([random.randrange(0, window_x // cell_size) * cell_size, 
                        random.randrange(0, window_y // cell_size) * cell_size]) for _ in range(5)]

# Initialize taxis
taxis = []
for _ in range(3):  # 3 taxis for the demo
    start_position = [random.randrange(0, window_x // cell_size) * cell_size, 
                      random.randrange(0, window_y // cell_size) * cell_size]
    destination = [random.randrange(0, window_x // cell_size) * cell_size, 
                   random.randrange(0, window_y // cell_size) * cell_size]
    taxis.append(Taxi(start_position, destination, buildings + moving_vehicles))

# Create the control center
control_center = ControlCenter(taxis, taxi_stops)

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update dynamic obstacles (moving vehicles)
    for vehicle in moving_vehicles:
        vehicle.update(buildings + moving_vehicles)

    # Update taxis and their passengers
    control_center.update()

    # Rendering
    game_window.fill(black)

    # Draw static obstacles (buildings)
    for building in buildings:
        pygame.draw.rect(game_window, building.color, pygame.Rect(building.position[0], building.position[1], building.size[0], building.size[1]))

    # Draw dynamic obstacles (moving vehicles)
    for vehicle in moving_vehicles:
        pygame.draw.rect(game_window, vehicle.color, pygame.Rect(vehicle.position[0], vehicle.position[1], vehicle.size[0], vehicle.size[1]))

    # Draw taxis
    for taxi in taxis:
        pygame.draw.rect(game_window, green, pygame.Rect(taxi.position[0], taxi.position[1], cell_size, cell_size))

    # Draw taxi stops
    for stop in taxi_stops:
        pygame.draw.circle(game_window, white, (stop.position[0], stop.position[1]), 10)

    pygame.display.update()
    fps.tick(car_speed)
