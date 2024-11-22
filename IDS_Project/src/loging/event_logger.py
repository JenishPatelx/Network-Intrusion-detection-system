# src/logging/event_logger.py

import sys
import os
import logging

class EventLogger:
    def __init__(self, log_file):
        # Create logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Ensure the directory for the log file exists
        log_dir = os.path.dirname(log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Set up file handler and formatter
        handler = logging.FileHandler(log_file)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_event(self, message):
        """
        Logs an event message into the log file.
        """
        self.logger.info(message)
