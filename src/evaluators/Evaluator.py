class Evaluator:
    def __init__(self):
        pass

    def evaluateVertex(self, vertex):
        return 0

    def evaluateBoard(self, board):
        for vertex in board.vertices.values():
            vertex.weight = self.evaluateVertex(vertex)
