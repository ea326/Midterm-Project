import pandas as pd
from app.observer import Observer

class AutoSaveObserver(Observer):
    def __init__(self, file_path='history.csv'):
        self.file_path = file_path

    def update(self, calculation):
        data = [{
            'operation': calculation.operation.__class__.__name__,
            'a': calculation.a,
            'b': calculation.b,
            'result': calculation.result,
            'timestamp': calculation.timestamp
        }]
        df = pd.DataFrame(data)
        df.to_csv(self.file_path, mode='a', index=False, header=not self._file_exists())

    def _file_exists(self):
        try:
            with open(self.file_path, 'r'):
                return True
        except FileNotFoundError:
            return False
