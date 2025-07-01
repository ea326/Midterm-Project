import logging
import os
from app.calculator_config import CALCULATOR_LOG_DIR, CALCULATOR_DEFAULT_ENCODING
from app.observer import Observer

# Ensure log directory exists
os.makedirs(CALCULATOR_LOG_DIR, exist_ok=True)

# Set up logger
log_file_path = os.path.join(CALCULATOR_LOG_DIR, "calculator.log")
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding=CALCULATOR_DEFAULT_ENCODING
)

logger = logging.getLogger("CalculatorLogger")

class LoggingObserver(Observer):
    def update(self, calculation):
        logger.info(str(calculation))

