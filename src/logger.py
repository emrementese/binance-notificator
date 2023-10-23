from colorama import init, Fore, Back
from settings import SUCCESS_LEVEL_NUM, LOG_LEVEL
import logging
init(autoreset=True)

class ColorFormatter(logging.Formatter):
    COLORS = {
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "DEBUG": Fore.BLUE,
        "INFO": Fore.WHITE,
        "CRITICAL": Fore.RED + Back.WHITE,
        "SUCCESS": Fore.GREEN
    }

    def format(self, record):
        color = self.COLORS.get(record.levelname, "")
        if color:
            record.name = color + record.name
            record.levelname = color + record.levelname
            record.msg = color + record.msg
        return logging.Formatter.format(self, record)

class NewLogger(logging.Logger):
    
    logging.addLevelName(SUCCESS_LEVEL_NUM, "SUCCESS")

    def __init__(self, name):
        logging.Logger.__init__(self, name)
        color_formatter = ColorFormatter("\n - %(levelname)s: %(asctime)s | FILE: %(filename)s |   %(funcName)s: %(lineno)d  | msg: %(message)s")
        console = logging.StreamHandler()
        console.setFormatter(color_formatter)
        self.addHandler(console)
        
    def success(self, message, *args, **kws):
        self._log(SUCCESS_LEVEL_NUM, message, args, **kws) 
        

logging.setLoggerClass(NewLogger)
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)