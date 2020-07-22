#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import random
from typing import Tuple, Union, List, Optional

import pygame

PointSpeed = Tuple[float, float]
PolylinePoint = Tuple['Vec2d', PointSpeed]

SCREEN_DIM = (800, 600)


class Vec2d:
    """A 2-dimensional vector defined by x and y coordinates.

    Supports basic vector arithmetic operations, such as addition,
    subtraction, and scalar multiplication.

    - int_pair() returns a tuple of vector's integer coordinates.
    """

    def __init__(self, x: float, y: float) -> None:
        """Initialize vector with given coordinates."""
        self.x = x
        self.y = y

    def __add__(self, other: 'Vec2d') -> 'Vec2d':
        """Return the sum of two vectors"""
        if not isinstance(other, type(self)):
            return NotImplemented
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vec2d') -> 'Vec2d':
        """Return subtraction of two vectors"""
        if not isinstance(other, Vec2d):
            return NotImplemented
        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, float]) -> 'Vec2d':
        """Return a vector multiplied by number"""
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Vec2d(self.x * other, self.y * other)

    def __rmul__(self, other: Union[int, float]) -> 'Vec2d':
        """Return a vector multiplied by number"""
        return self.__mul__(other)

    def __eq__(self, other: object) -> bool:
        """Return true if vectors are equal"""
        if not isinstance(other, type(self)):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __len__(self) -> int:
        """Return the length of a vector"""
        return int(math.sqrt(self.x * self.x + self.y * self.y))

    def __repr__(self) -> str:
        return f'Vec2d({self.x}, {self.y})'

    def int_pair(self) -> Tuple[int, int]:
        """Return vector's coordinates as a tuple of integers"""
        return int(self.x), int(self.y)


class Polyline:
    """A polyline containing a list of points with their speed.

    - A polyline can be drawn using draw_points()
    """

    def __init__(
            self, points: Optional[List[PolylinePoint]] = None
    ) -> None:
        """Initialize Polyline object from given list of points

        :param points: List of vector-points and speeds
        """
        self.points = points or []

    def draw_points(
            self,
            style: str = 'points',
            width: int = 3,
            color: Tuple[int, int, int] = (255, 255, 255)
    ) -> None:
        """Draw points of a polyline on the screen

        :param style: Style of drawing object. Options: 'points', 'line'
        :param width: Width of the drawing object
        :param color: Color in RGB
        """

    def set_points(self) -> None:
        """Recalculate coordinates of points"""

    def add_point(
            self, point: Vec2d, speed: PointSpeed = (0.5, 0.5)
    ) -> None:
        """Add a point to polyline

        :param point: Vec2d point object
        :param speed: Speed of the point
        """


class Knot(Polyline):
    """Knot object that makes a smoothed polyline"""

    def __init__(
            self, points: Optional[List[PolylinePoint]] = None, steps: int = 1
    ) -> None:
        """Initialize Knot object from given list of points

        :param points: Base points of polyline
        :param steps: Number of smoothing steps
        """
        super().__init__(points)
        self.step = steps

    def get_knot(self) -> List[PolylinePoint]:
        """Return list of knot points"""

    def _get_knot_points(self) -> List[PolylinePoint]:
        """Return list of knot points based on polyline points"""

    def _get_knot_point(
            self, alpha: int, degree: Optional[int] = None
    ) -> PolylinePoint:
        """Return next smoothing point in n-degree curve calculated
        recursively from polyline points with given angle `alpha`
        between points.

        :param alpha: Angle between curve points
        :param degree: Curve degree
        """


# =======================================================================================
# Функции для работы с векторами
# =======================================================================================

def sub(x, y):
    """"возвращает разность двух векторов"""
    return x[0] - y[0], x[1] - y[1]


def add(x, y):
    """возвращает сумму двух векторов"""
    return x[0] + y[0], x[1] + y[1]


def length(x):
    """возвращает длину вектора"""
    return math.sqrt(x[0] * x[0] + x[1] * x[1])


def mul(v, k):
    """возвращает произведение вектора на число"""
    return v[0] * k, v[1] * k


def vec(x, y):
    """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
    координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
    return sub(y, x)


# =======================================================================================
# Функции отрисовки
# =======================================================================================
def draw_points(points, style="points", width=3, color=(255, 255, 255)):
    """функция отрисовки точек на экране"""
    if style == "line":
        for p_n in range(-1, len(points) - 1):
            pygame.draw.line(gameDisplay, color,
                             (int(points[p_n][0]), int(points[p_n][1])),
                             (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)

    elif style == "points":
        for p in points:
            pygame.draw.circle(gameDisplay, color,
                               (int(p[0]), int(p[1])), width)


def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# Функции, отвечающие за расчет сглаживания ломаной
# =======================================================================================
def get_point(points, alpha, deg=None):
    if deg is None:
        deg = len(points) - 1
    if deg == 0:
        return points[0]
    return add(mul(points[deg], alpha), mul(get_point(points, alpha, deg - 1), 1 - alpha))


def get_points(base_points, count):
    alpha = 1 / count
    res = []
    for i in range(count):
        res.append(get_point(base_points, i * alpha))
    return res


def get_knot(points, count):
    if len(points) < 3:
        return []
    res = []
    for i in range(-2, len(points) - 2):
        ptn = []
        ptn.append(mul(add(points[i], points[i + 1]), 0.5))
        ptn.append(points[i + 1])
        ptn.append(mul(add(points[i + 1], points[i + 2]), 0.5))

        res.extend(get_points(ptn, count))
    return res


def set_points(points, speeds):
    """функция перерасчета координат опорных точек"""
    for p in range(len(points)):
        points[p] = add(points[p], speeds[p])
        if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
            speeds[p] = (- speeds[p][0], speeds[p][1])
        if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
            speeds[p] = (speeds[p][0], -speeds[p][1])


# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    points = []
    speeds = []
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(event.pos)
                speeds.append((random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        draw_points(points)
        draw_points(get_knot(points, steps), "line", 3, color)
        if not pause:
            set_points(points, speeds)
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
