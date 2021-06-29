import logging


def log():
    logging.basicConfig(filename="/Users/animeshmukherjee/PycharmProjects/pythonProject/Utilities/logs/logfile.log",
                        format='%(asctime)s : %(levelname)s : %(message)s)',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.INFO
                        )
    logger_name = logging.getLogger()
    return logger_name


logger = log()
logger.info("This is a log message")