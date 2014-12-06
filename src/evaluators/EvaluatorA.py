from Evaluator import Evaluator

class EvaluatorA(Evaluator):
    def __init__(self):
        Evaluator.__init__(self)


    def evaluateVertex(self, vertex):
        hexResources = set()
        hexValues = 0

        for hexRef in vertex.h_refs:
            if hexRef == None:
                continue
            hexResources.add(hexRef.resource)
            hexValues += int(hexRef)

        return (4 - len(hexResources)) * hexValues


        