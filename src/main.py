from models import Board, Hexagon, Vertex
from views import Display
from evaluators import EvaluatorA as EV
from algorithms import dijkstra

def clickedInBounds(point, bounds):
    return bounds[0] < point.getX() < bounds[2] and bounds[1] < point.getY() < bounds[3]

def GameLoop():
    START_BUTTON = (20, 25, 120, 70)
    END_BUTTON = (20, 100, 120, 150)

    # Create the board
    board = Board(3)
    EV().evaluateBoard(board)

    # Show the initial board
    display = Display()
    display.drawBoard(board)
    # Draw set Starting node button
    _a, _b = display.drawButton("Starting Node", START_BUTTON[0:2], START_BUTTON[2:4], scale = True)
    
    # Draw set Ending node button
    _c, _d = display.drawButton("Ending Node", END_BUTTON[0:2], END_BUTTON[2:4], scale = True)
    
    action = None
    start_circle = None
    end_circle = None
    changed = False
    start = None
    end = None

    while True:
        clicked = display.input()
        if clicked != None:
            if clickedInBounds(clicked, START_BUTTON):
                action = "start"
                if start_circle != None:
                    start_circle.undraw()
            elif clickedInBounds(clicked, END_BUTTON):
                action = "end"
                if end_circle != None:
                    end_circle.undraw()
            else:
                if action == "start":
                    start = board.get_vertex_from_position(display._convertToNormal((clicked.getX(), clicked.getY())))
                    if start != None:
                        start_circle = display._drawCircle(start.pos, 20, "red")
                        changed = True
                        action = None
                    
                if action == "end":
                    end = board.get_vertex_from_position(display._convertToNormal((clicked.getX(), clicked.getY())))
                    if end != None:
                        end_circle = display._drawCircle(end.pos, 20, "blue")
                        changed = end != None
                        action = None

        if changed and start and end:
            # dijkstra.find_path(board.vertices.values(), start, end)
            changed = False

        display.update()
    display.wait()
    display.close()

def DrawBoardTest():
    board = Board(4)
    EV().evaluateBoard(board)

    dijkstra.find_path(board.vertices.values(), start, stop)

    # Showing the Board
    display = Display()
    display.drawBoard(board)
    display.update()

    display.wait()
    display.close()

if __name__ == "__main__":
    # DrawBoardTest()

    GameLoop()
