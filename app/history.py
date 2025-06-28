class History:
    def __init__(self):
        self._history = []
        self._redo_stack = []

    def add(self, calculation):
        self._history.append(calculation)
        self._redo_stack.clear()

    def undo(self):
        if not self._history:
            raise IndexError("No operations to undo.")
        calc = self._history.pop()
        self._redo_stack.append(calc)
        return calc

    def redo(self):
        if not self._redo_stack:
            raise IndexError("No operations to redo.")
        calc = self._redo_stack.pop()
        self._history.append(calc)
        return calc

    def get_history(self):
        return list(self._history)
