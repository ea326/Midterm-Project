import os
import pandas as pd
from app.observer import Observer
from app.calculator_config import CALCULATOR_HISTORY_DIR, CALCULATOR_AUTO_SAVE

class AutoSaveObserver(Observer):
    def __init__(self):
        os.makedirs(CALCULATOR_HISTORY_DIR, exist_ok=True)
        self.file_path = os.path.join(CALCULATOR_HISTORY_DIR, "history.csv")

    def update(self, calculation):
        if not CALCULATOR_AUTO_SAVE:
            return

        from app.history import history  # delayed to avoid circular import
        data = [{
            'operation': calc.operation.__class__.__name__,
            'a': calc.a,
            'b': calc.b,
            'result': calc.result,
            'timestamp': calc.timestamp
        } for calc in history.get_history()]
        df = pd.DataFrame(data)
        df.to_csv(self.file_path, index=False)
