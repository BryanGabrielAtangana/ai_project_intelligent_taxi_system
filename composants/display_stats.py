import pygame

class DisplayStats:
    def __init__(self, font_size=20):
        """Initialize the stats display."""
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', font_size)

    def render(self, surface, stats):
        """
        Render statistics on the screen.
        Args:
            surface: The Pygame surface to draw on.
            stats: Dictionary of stats to display.
        """
        y_offset = 10
        for key, value in stats.items():
            text = f"{key}: {value}"
            rendered_text = self.font.render(text, True, pygame.Color(255, 255, 255))
            surface.blit(rendered_text, (10, y_offset))
            y_offset += 30
