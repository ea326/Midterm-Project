import logging
from app.observer import Observer

class LoggingObserver(Observer):
    def __init__(self, log_file='calculator.log'):
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )
        self.logger = logging.getLogger()

    def update(self, calculation):
        self.logger.info(str(calculation))
