from typing import override

from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame


class Shot(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    @override
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen ,"white", self.position, SHOT_RADIUS)

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
