import logging
from logging.handlers import TimedRotatingFileHandler
import os
import datetime
import inspect
import argparse

def rolling_logger(app_id: str = None, logger_name: str = None, logging_level=logging.INFO, path='C\\dir\\Logs\\',
               log_file='file_name.log'):
    """
    Handles writing to the log file with specific style rules applied.
    Rolling logs generates a new log file every week and stores onlu one weeks worth of old logs
    
    dir
        Logs
            file_name.log.20230814
            file_name.log
    """
    print(path, log_file)
    app_id_str = f"[app-id: {app_id}]" if app_id else ""
    fmt = f"%(asctime)s {app_id_str} %(levelname)s %(threadName)s %(filename)s %(message)s"

    if not logger_name:
        # gets the name of the module calling get_logger
        logger_name = inspect.getmodule(inspect.stack()[1][0]).__name__

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging_level)

    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    rotating_handler = TimedRotatingFileHandler(path + '\\' + log_file, when='W6', backupCount=1) # specifies how many logs to keep and when to roll over
    rotating_handler.setFormatter(logging.Formatter(fmt))
    logger.addHandler(rotating_handler)

    return logger

parser = argparse.ArgumentParser(description='Parses path and log_file arguments')
parser.add_argument('--path', default='dir/logs', type=str, help='Path to logs')
parser.add_argument('--log_file', default='name.log', type=str, help='Log file name')
args = parser.parse_args()
logger = rolling_logger(path=args.path, log_file=args.log_file)


def logger_make_dirs(app_id: str=None, logger_name: str=None, logging_level= logging.INFO):
    """
    This logger function will create a new file structure in the following format:
    2023
        Jul
            07@15-48.log
    It will then save any logs inside the file created above
    
    Args:
        app_id (str, optional): The unique identifier for the application. Used to tag the log entries. Defaults to None.
        logger_name (str, optional): The name of the logger. If not provided, it defaults to the name of the module from where the function is called. Defaults to None.
        logging_level (logging, optional): The level at which the logger should log. For example, logging.INFO, logging.DEBUG etc. Defaults to logging.INFO.

    Returns:
        logging.Logger: Logger instance configured with the given parameters.
    """
    current = datetime.date.today()
    year = current.strftime("%Y")
    month = current.strftime("%b")
    day = current.strftime("%d")
    time = datetime.datetime.now().strftime("%H-%M")

    app_id_str = f'[app-id: {app_id}]' if app_id else ''
    fmt = f'%(asctime)s {app_id_str} %(levelname)s %(threadName)s %(name)s %(message)s'
    current_dir = os.getcwd()
    print(current_dir)
    file_path_year = f'{current_dir}\\logs\\{year}\\'
    file_path_year_month = f'{current_dir}\\logs\\{year}\\{month}\\'

    if not os.path.exists(os.path.dirname(file_path_year)):
        os.makedir(os.path.dirname(file_path_year))
    if not os.path.exists(os.path.dirname(file_path_year_month)):
        os.makedirs(os.path.dirname(file_path_year_month))
    
    logging.basicConfig(
        filename=f'{file_path_year_month}\\{day}@{time}.log',
        filemode='a+',
        level = logging_level,
        format=fmt,
    )

    if not logger_name:
        logger_name = inspect.getmodule(inspect.stack()[1][0]).__name__
    logger = logging.getLogger(logger_name)
    return logger

logger = logger_make_dirs()


logger.info('Info')
logger.warning('Warning')
logger.error('Error')
logger.critical('Critical')


def logger_delete_old(app_id: str=None, logger_name: str=None, logging_level= logging.INFO):
    """
    This logger function will create a new file structure in the following format:
    2023
        Jul
            07@15-48.log
    It will delete any logs which are older than a week
    It will then save any logs inside the file created above
    
    Args:
        app_id (str, optional): The unique identifier for the application. Used to tag the log entries. Defaults to None.
        logger_name (str, optional): The name of the logger. If not provided, it defaults to the name of the module from where the function is called. Defaults to None.
        logging_level (logging, optional): The level at which the logger should log. For example, logging.INFO, logging.DEBUG etc. Defaults to logging.INFO.

    Returns:
        logging.Logger: Logger instance configured with the given parameters.
    """
    current = datetime.date.today()
    year = current.strftime("%Y")
    month = current.strftime("%b")
    day = current.strftime("%d")
    time = datetime.datetime.now().strftime("%H-%M")

    app_id_str = f'[app-id: {app_id}]' if app_id else ''
    fmt = f'%(asctime)s {app_id_str} %(levelname)s %(threadName)s %(name)s %(message)s'
    current_dir = os.getcwd()

    file_path_year = f'{current_dir}\\logs\\{year}\\'
    file_path_year_month = f'{current_dir}\\logs\\{year}\\{month}\\'

    if not os.path.exists(os.path.dirname(file_path_year)):
        os.makedirs(os.path.dirname(file_path_year))
        print('made')
    if not os.path.exists(os.path.dirname(file_path_year_month)):
        os.makedirs(os.path.dirname(file_path_year_month))
    
    for file in os.listdir(file_path_year_month):
        if int(file.split('@')[0]) + 7 <= int(day):
            if os.path.isfile(file_path_year_month+'\\' + file):
                os.remove(file_path_year_month+'\\' + file)

    logging.basicConfig(
        filename=f'{file_path_year_month}\\{day}@{time}.log',
        filemode='a+',
        level = logging_level,
        format=fmt,
    )

    if not logger_name:
        logger_name = inspect.getmodule(inspect.stack()[1][0]).__name__
    logger = logging.getLogger(logger_name)
    return logger

logger = logger_delete_old()

logger.info('Info')
logger.warning('Warning')
logger.error('Error')
logger.critical('Critical')


def logger_basic(app_id: str=None, logger_name: str=None, logging_level= logging.INFO):
    """
    This logger is a simple function and just creates a log file
    
    Args:
        app_id (str, optional): The unique identifier for the application. Used to tag the log entries. Defaults to None.
        logger_name (str, optional): The name of the logger. If not provided, it defaults to the name of the module from where the function is called. Defaults to None.
        logging_level (logging, optional): The level at which the logger should log. For example, logging.INFO, logging.DEBUG etc. Defaults to logging.INFO.

    Returns:
        logging.Logger: Logger instance configured with the given parameters.
    """
    app_id_str = f'[app-id: {app_id}]' if app_id else ''
    fmt = f'%(asctime)s {app_id_str} %(levelname)s %(threadName)s %(name)s %(message)s'
    logging.basicConfig(
        level = logging_level,
        format=fmt,
    )
    if not logger_name:
        logger_name = inspect.getmodule(inspect.stack()[1][0]).__name__
    logger = logging.getLogger(logger_name)
    return logger

logger = logger_basic()
logger.info('Info')
logger.warning('Warning')
logger.error('Error')
logger.critical('Critical')
