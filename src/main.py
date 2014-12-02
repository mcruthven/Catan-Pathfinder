from models import Board, Hexagon, Vertex
from views import Display


if __name__ == "__main__":
    display = Display()
    board = Board(5)
    testHexagon = board.hexagons[(0,0)]
    print testHexagon

    display.drawHexagon(testHexagon)

    display.wait()
    display.close()