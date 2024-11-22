# tests/test_event_logger.py

import os
import pytest
from src.logging.event_logger import EventLogger

def ensure_logs_directory_exists():
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

def test_event_logger():
    log_file = "logs/test.log"

    # Ensure the logs directory exists
    ensure_logs_directory_exists()

    # Create an instance of EventLogger
    logger = EventLogger(log_file)

    # Log a test event
    logger.log_event("Test event logged")

    # Assert that the log file exists
    assert os.path.exists(log_file), f"Log file {log_file} was not created"

    # Assert that the log file is not empty
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert len(log_content) > 0, f"Log file {log_file} is empty"
