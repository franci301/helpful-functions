import logging
import os
import datetime
import inspect


def get_logger(app_id: str=None, logger_name: str=None, logging_level= logging.INFO):
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
        os.makedir(os.path.dirname(file_path_year_month))
    
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

logger = get_logger()


logger.info('Info')
logger.warning('Warning')
logger.error('Error')
logger.critical('Critical')


def get_logger_basic(app_id: str=None, logger_name: str=None, logging_level= logging.INFO):
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

logger = get_logger_basic()
logger.info('Info')
logger.warning('Warning')
logger.error('Error')
logger.critical('Critical')
