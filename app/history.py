class History:
    def __init__(self):
        self._history = []
        self._redo_stack = []
        self._observers = []  

    def register_observer(self, observer):  
        self._observers.append(observer)
    
    def notify_observers(self, calculation):
        for observer in self._observers:
            observer.update(calculation)

    def add_calculation(self, calculation):
        self._history.append(calculation)
        self._redo_stack.clear()
        self.notify_observers(calculation)

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

    def clear(self):
        self._history.clear()
        self._redo_stack.clear()
