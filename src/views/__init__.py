from graphics import *

SCALE = 50

MATERIALS_COLOR = {"stone": "darkgrey",
                   "sheep": color_rgb(149,200,89),
                   "brick": color_rgb(183,117,73),
                   "wood":  "darkgreen",
                   "wheat": "gold",
                   "desert": "beige"}

class Display:
    def __init__(self, title = "Catan", size = (800, 800)):
        # Window Height / Width
        self.width = size[0]
        self.height = size[1]
        self.w_offset = size[0]/2
        self.h_offset = size[1]/2

        # Create the Window
        self.window = GraphWin(title, size[0], size[1], autoflush = False)

    """
    Drawing Functions
    """
    def drawBoard(self, board):
         for hexagon in board.hexagons.values():
            self.drawHexagon(hexagon)

    def drawHexagon(self, hexagon):
        self._drawPolygon(MATERIALS_COLOR[hexagon.resource], *[v.pos for v in hexagon.vertices])

    def drawPath(self, *points):
        map(self._drawLine, zip(points, points[1:]))

    """
    Lifecycle Functions
    """
    def update(self):
        self.window.update()

    def wait(self):
        self.window.getMouse()

    def close(self):
        self.window.close()

    """
    Helper Functions
    """
    def _drawPolygon(self, color, *points):
        _shape = Polygon(map(self._makePoint, points))
        _shape.setFill(color)
        _shape.draw(self.window)

    def _drawLine(self, A, B):
        _line = Line(self._makePoint(A), self._makePoint(B))
        _line.setArrow("last")
        _line.draw(self.window)

    def _makePoint(self, pos):
        return Point(self.w_offset + SCALE * pos[0], self.h_offset - SCALE * pos[1])

if __name__ == "__main__":
    display = Display()

    display._drawPolygon("grey", (0,0), (0,100), (100,100), (100,0))

    display.wait()
    display.close()

