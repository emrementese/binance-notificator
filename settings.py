import os
from pathlib import Path

SUCCESS_LEVEL_NUM = 10
BASE_DIR = Path(__file__).resolve().parent
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
DEBUG = os.environ.get('DEBUG', False)


        
        

