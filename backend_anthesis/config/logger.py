import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Create logs directory if it doesn't exist
log_dir = Path('logs')
log_dir.mkdir(exist_ok=True)

# Configure the root logger
def setup_logger(name):
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent adding multiple handlers if logger is already configured
    if logger.handlers:
        return logger

    # Create formatters
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)

    # File handler with rotation (10MB per file, keep 5 backup files)
    file_handler = RotatingFileHandler(
        log_dir / 'app.log',
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# Create a default logger instance
default_logger = setup_logger(__name__)

# Example usage:
# from config.logger import setup_logger
# logger = setup_logger(__name__)
# logger.info("This is an info message")
# logger.error("This is an error message")
