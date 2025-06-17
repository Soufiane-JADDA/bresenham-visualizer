from bresenham import Point
from graphics import Graphics

def main():
    gfx = Graphics(square_size=15)

    # Draw lines in different octant's
    gfx.draw_line(Point(0, 0), Point(8, 5), color='red')    # Octant 1
    gfx.draw_line(Point(0, 0), Point(9, 13), color='red')   # Octant 2
    # gfx.draw_line(Point(0, 0), Point(-8, 5))   # Octant 4
    # gfx.draw_line(Point(0, 0), Point(0, 10))   # Vertical line

    # Draw a circle centered at origin
    gfx.draw_circle(Point(0, 0), 20, color='green')

    # Keep window open
    gfx.finish()

if __name__ == "__main__":
    main()
