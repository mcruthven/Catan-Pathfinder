from graphics import *

SCALE = 50.0

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
        self.window.setBackground(color_rgb(96,172,226))

    """
    Drawing Functions
    """
    def drawBoard(self, board):
         for hexagon in board.hexagons.values():
            self.drawHexagon(hexagon)
         for vertex in board.vertices.values():
            self.drawWeight(vertex)

    def drawHexagon(self, hexagon):
        self._drawPolygon(MATERIALS_COLOR[hexagon.resource], *[v.pos for v in hexagon.vertices])
        self.drawResource(hexagon)

    def drawResource(self, hexagon):
        self._drawCircle(hexagon.pos, 20, "white")
        self._drawText(hexagon.pos, str(hexagon.value))

    def drawWeight(self, vertex):
        self._drawText(vertex.pos, str(vertex.weight))

    def drawButton(self, text, pos1, pos2, color = "white", scale = False):
        if scale:
            pos1 = self._convertToNormal(pos1)
            pos2 = self._convertToNormal(pos2)
        return \
        self._drawRectangle(pos1, pos2, color), \
        self._drawText(((pos1[0] + pos2[0])/2.0, (pos1[1] + pos2[1])/2.0), text)

    def drawPath(self, *points):
        map(self._drawLine, zip(points, points[1:]))

    """
    Lifecycle Functions
    """
    def update(self):
        self.window.update()

    def input(self):
        return self.window.checkMouse()

    def wait(self):
        return self.window.getMouse()

    def close(self):
        self.window.close()

    """
    Helper Functions
    """
    def _drawPolygon(self, color, *points):
        _shape = Polygon(map(self._makePoint, points))
        _shape.setFill(color)
        _shape.draw(self.window)
        return _shape

    def _drawRectangle(self, pos1, pos2, color):
        _rect = Rectangle(self._makePoint(pos1), self._makePoint(pos2))
        _rect.setFill(color)
        _rect.draw(self.window)
        return _rect

    def _drawCircle(self, pos, rad, color):
        _circle = Circle(self._makePoint(pos), rad)
        _circle.setFill(color)
        _circle.draw(self.window)
        return _circle

    def _drawLine(self, A, B):
        _line = Line(self._makePoint(A), self._makePoint(B))
        _line.setArrow("last")
        _line.draw(self.window)
        return _line

    def _drawText(self, pos, value, size = 14):
        _text = Text(self._makePoint(pos),value)
        _text.setSize(size)
        _text.draw(self.window)
        return _text

    def _makePoint(self, pos):
        return Point(self.w_offset + SCALE * pos[0], self.h_offset - SCALE * pos[1])

    def _convertToNormal(self, pos):
        return (pos[0] - self.w_offset) / SCALE, (- pos[1] + self.h_offset) / SCALE


if __name__ == "__main__":
    display = Display()

    display._drawPolygon("grey", (0,0), (0,100), (100,100), (100,0))

    display.wait()
    display.close()

