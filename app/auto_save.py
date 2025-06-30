import pandas as pd
from app.observer import Observer

class AutoSaveObserver(Observer):
    def __init__(self, file_path='history.csv'):
        self.file_path = file_path

    def update(self, calculation):
        from app.history import history  # delay import to avoid circular dependency
        data = [{
            'operation': calc.operation.__class__.__name__,
            'a': calc.a,
            'b': calc.b,
            'result': calc.result,
            'timestamp': calc.timestamp
        } for calc in history.get_history()]
        df = pd.DataFrame(data)
        df.to_csv(self.file_path, index=False)
