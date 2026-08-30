from typing import override

import pygame
from .circleshape import CircleShape
from .constants import ASTEROID_MIN_RADIUS, LINE_WIDTH, ASTEROID_MAX_RADIUS
from utils.logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)

            new_vector1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
            new_vector2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = new_vector1 * 1.2
            asteroid2.velocity = new_vector2 * 1.2
