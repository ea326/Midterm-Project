class History:
    def __init__(self):
        self._history = []
        self._redo_stack = []

    def add(self, calculation):
        self._history.append(calculation)
        self._redo_stack.clear()
