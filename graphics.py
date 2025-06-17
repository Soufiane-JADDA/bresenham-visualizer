import turtle as tt
from bresenham import Point, Bresenham

class Graphics:
    def __init__(self, square_size=10):
        self.square_size = square_size
        self.screen = tt.Screen()
        self.screen.title("Bresenham Drawing")
        self.pen = tt.Turtle()
        self.pen.hideturtle()
        self.pen.width(1)
        self.pen.speed(0)
        self.draw_grid()

    def draw_grid(self):
        self.pen.penup()
        self.pen.color("lightgrey")
        spacing = self.square_size
        width = self.screen.window_width() // 2
        height = self.screen.window_height() // 2

        for x in range(-width, width + spacing, spacing):
            self.pen.goto(x, -height)
            self.pen.setheading(90)
            self.pen.pendown()
            self.pen.forward(2 * height)
            self.pen.penup()

        for y in range(-height, height + spacing, spacing):
            self.pen.goto(-width, y)
            self.pen.setheading(0)
            self.pen.pendown()
            self.pen.forward(2 * width)
            self.pen.penup()

        self.pen.color("black")

    def draw_square(self, x, y, color='red'):
        """Draw a square at (x, y) with given size."""
        x *= self.square_size
        y *= self.square_size
        self.pen.penup()
        self.pen.goto(x, y)
        self.pen.pendown()
        self.pen.fillcolor(color)
        self.pen.begin_fill()
        for _ in range(4):
            self.pen.forward(self.square_size)
            self.pen.right(90)
        self.pen.end_fill()


    def draw_line(self, point_a: Point, point_b: Point, color='red'):
        """Draw a line between two points using Bresenham's algorithm."""
        bresenham = Bresenham()
        points = bresenham.trace_line(point_a, point_b)
        for point in points:
            self.draw_square(point.x, point.y, color)

    def draw_circle(self, center: Point, radius: int, color='red'):
        """Draw a circle with given center and radius."""
        bresenham = Bresenham()
        points = bresenham.trace_circle(center, radius)
        for point in points:
            self.draw_square(point.x, point.y, color)

    def finish(self):
        self.screen.mainloop()
