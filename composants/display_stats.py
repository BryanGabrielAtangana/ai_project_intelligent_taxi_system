import pygame

def display_stats(surface, taxis, passengers):
    font = pygame.font.SysFont("Arial", 18)
    stats = [
        f"Taxis: {len(taxis)}",
        f"Passengers Waiting: {len(passengers)}"
    ]
    for i, stat in enumerate(stats):
        text_surface = font.render(stat, True, pygame.Color(255, 255, 255))
        surface.blit(text_surface, (10, 10 + i * 20))
