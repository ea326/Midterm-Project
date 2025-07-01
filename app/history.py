import pandas as pd
import os
from app.calculation import Calculation
from app.calculator import OperationFactory
from app.calculator_config import CALCULATOR_HISTORY_DIR

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

    def save_to_file(self):
        data = [{
            'operation': calc.operation.__class__.__name__,
            'operand1': calc.a,
            'operand2': calc.b,
            'result': calc.result
        } for calc in self._history]

        df = pd.DataFrame(data)
        file_path = os.path.join(CALCULATOR_HISTORY_DIR, "history.csv")
        df.to_csv(file_path, index=False)

    def load_from_file(self):
        file_path = os.path.join(CALCULATOR_HISTORY_DIR, "history.csv")
        if not os.path.exists(file_path):
            raise FileNotFoundError("History file not found.")

        df = pd.read_csv(file_path)
        self._history.clear()
        for _, row in df.iterrows():
            op_class = getattr(OperationFactory, row['operation'].lower(), None)
            if op_class is None:
                continue
            operation = OperationFactory.create(row['operation'].lower())
            calc = Calculation(operation, float(row['operand1']), float(row['operand2']), float(row['result']))
            self._history.append(calc)


history = History()
