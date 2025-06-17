class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f"({self.x}, {self.y})"

class Bresenham:
    def __init__(self):
        pass

    def trace_line(self, point_a, point_b):
        """Draw a line between point_a and point_b using Bresenham's algorithm."""
        if not isinstance(point_a, Point) or not isinstance(point_b, Point):
            raise ValueError("Points must be instances of Point class")
        if point_a.x == point_b.x and point_a.y == point_b.y:
            return [Point(point_a.x, point_a.y)]

        points = []
        x0, y0 = point_a.x, point_a.y
        x1, y1 = point_b.x, point_b.y
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        points.append(Point(x0, y0))
        while x0 != x1 or y0 != y1:
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy
            points.append(Point(x0, y0))

        return points

    def trace_circle(self, center, radius):
        """Draw a circle with given center and radius using Bresenham's algorithm."""
        if not isinstance(center, Point):
            raise ValueError("Center must be an instance of Point class")
        if radius <= 0:
            raise ValueError("Radius must be positive")

        points = []
        x = 0
        y = radius
        d = 3 - 2 * radius

        # Generate points for one octant and mirror to others
        def add_symmetric_points(cx, cy, x, y):
            points.extend([
                Point(cx + x, cy + y), Point(cx - x, cy + y),
                Point(cx + x, cy - y), Point(cx - x, cy - y),
                Point(cx + y, cy + x), Point(cx - y, cy + x),
                Point(cx + y, cy - x), Point(cx - y, cy - x)
            ])

        add_symmetric_points(center.x, center.y, x, y)
        while x <= y:
            if d > 0:
                d += 4 * (x - y) + 10
                y -= 1
            else:
                d += 4 * x + 6
            x += 1
            add_symmetric_points(center.x, center.y, x, y)

        return points
