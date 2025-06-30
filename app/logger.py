import logging
import os
from datetime import datetime
from app.calculator_config import CALCULATOR_LOG_DIR

os.makedirs(CALCULATOR_LOG_DIR, exist_ok=True)

log_file_path = os.path.join(CALCULATOR_LOG_DIR, "calculator.log")

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)
