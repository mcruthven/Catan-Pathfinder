from graphics import *

SCALE = 100

MATERIALS_COLOR = {"stone": "grey",
                    "sheep": "white",
                    "brick": "red",
                    "wood":  "brown",
                    "wheat": "yellow"}

class Display:
    def __init__(self, title = "Catan", size = (600, 600)):
        # Window Height / Width
        self.width = size[0]
        self.height = size[1]
        self.w_offset = size[0]/2
        self.h_offset = size[1]/2

        # Create the Window
        self.window = GraphWin(title, size[0], size[1])

    def drawBoard(self, board):
         for hexagon in board.hexagons.values():
            self.drawHexagon(hexagon)

    def drawHexagon(self, hexagon):
        self._drawPolygon(MATERIALS_COLOR[hexagon.resource], *[v.pos for v in hexagon.vertices])

    """
    Helper Functions
    """
    def _drawPolygon(self, color, *points):
        _shape = Polygon(map(lambda pos: Point(self.w_offset + SCALE * pos[0], self.h_offset - SCALE * pos[1]), points))
        _shape.setFill(color)
        _shape.draw(self.window)

    def wait(self):
        self.window.getMouse()

    def close(self):
        self.window.close()

if __name__ == "__main__":
    display = Display()

    display._drawPolygon("grey", (0,0), (0,100), (100,100), (100,0))

    display.wait()
    display.close()

