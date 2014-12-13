from models import Board, Hexagon, Vertex
from views import Display
from evaluators import EvaluatorA as EV
from algorithms import dijkstra
import sys

class Controller:
    def __init__(self, display, board, algorithm):
        self.display = display
        self.board = board
        self.algorithm = algorithm()

        self.initMembers()

        self.display.drawBoard(self.board)

    def initMembers(self):
        # Click action
        self.action = None

        # Start / End vertices / circles
        self.start_circle = None
        self.end_circle = None
        self.start = None
        self.end = None

        # Whether or not to recalculate the path
        self.changed = False
        self.pathLines = []
        self.settleCircles = []

    def drawButtons(self, *args):
        self.buttons = []
        for arg in args:
            self.buttons.append(arg)
            self.display.drawButton(arg[-1], arg[0:2], arg[2:4], scale = True)

    def handleClick(self):
        clicked = self.display.input()
        if clicked == None:
            return
        # Check if clicked buttons
        if self.clickedInBounds(clicked, self.buttons[0]):
            self.action = "start"
            if self.start_circle != None:
                self.start_circle.undraw()
        elif self.clickedInBounds(clicked, self.buttons[1]):
            self.action = "end"
            if self.end_circle != None:
                self.end_circle.undraw()
        else: # Otherwise, selecting a node
            if self.action == "start":
                self.start = self.board.get_vertex_from_position(self.display._convertToNormal((clicked.getX(), clicked.getY())))
                if self.start != None:
                    self.start_circle = self.display._drawCircle(self.start.pos, 20, "red")
                    if len(sys.argv) > 1:
                        for vertex in self.start.s_refs:
                            self.display._drawCircle(vertex.pos, 20, "white")
                            self.display.drawPath(self.start.pos, *[v.pos for v in self.start.s_refs[vertex]])
                    self.changed = True
                    self.action = None

            if self.action == "end":
                self.end = self.board.get_vertex_from_position(self.display._convertToNormal((clicked.getX(), clicked.getY())))
                if self.end != None:
                    self.end_circle = self.display._drawCircle(self.end.pos, 20, "blue")
                    self.changed = True
                    self.action = None

        # Check to see if we need to redraw the path
        if self.changed and self.start and self.end:
            path, s_path = self.algorithm.find_path(self.board.vertices.values(), self.start, self.end)

            self.clearPath()
            self.settleCircles = [self.display._drawCircle(v.pos, 20, "red") for v in s_path]
            self.pathLines = self.display.drawPath(*[v.pos for v in path])
            self.display.update()

            self.start = None
            self.end = None
            self.end_circle.undraw()
            self.start_circle.undraw()

            changed = False

    def clearPath(self):
        for edge in self.pathLines + self.settleCircles:
            edge.undraw()

    def clickedInBounds(self, point, bounds):
        return bounds[0] < point.getX() < bounds[2] and bounds[1] < point.getY() < bounds[3]

def GameLoop():
    # Buttons
    START_BUTTON = (20, 25, 120, 70, "Starting Node")
    END_BUTTON = (20, 100, 120, 150, "Ending Node")

    # Create the board
    board = Board(2, 3)
    EV().evaluateBoard(board)

    # Show the initial board
    display = Display()

    # Controller Initialization
    controller = Controller(display, board, dijkstra.DijkstraSettlementAlgorithm)
    controller.drawButtons(START_BUTTON, END_BUTTON)

    while True:
        controller.handleClick()
        display.update()

    display.close()

if __name__ == "__main__":
    # DrawBoardTest()

    GameLoop()
