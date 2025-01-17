import pandas
import numpy
import os
from src.logger.custom_logging import logging
from src.exception.exception import customexception
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    pass
class DataIngestion:
    def __init__(self):
        pass
    try:
        pass
    except Exception as e:
        logging.info()
        raise customexception(e, sys)