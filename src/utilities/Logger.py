import inspect
import logging
import os.path


class Logger:
    def __init__(self, config_obj):
        if config_obj is not None:
            self.config = config_obj
            self.log_file = os.path.abspath(self.config.LOG_FILE_PATH)
        else:
            self.log_file = os.path.abspath('./out/automation.log')

        self.log_level = logging.DEBUG
        self.log_format = '%(asctime)s - %(name)s - %(levelname)s: %(message)s'
        self.log_time_format = '%m/%d/%Y %I:%M:%S %p'

    def get_logger(self):
        # Gets the name of the class / method from where this method is called
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        # By default, log all messages
        logger.setLevel(self.log_level)

        # Add the log file handler
        file_handler = logging.FileHandler(self.log_file, mode='a')
        file_handler.setLevel(self.log_level)

        # Add the log formatter
        formatter = logging.Formatter(self.log_format, datefmt=self.log_time_format)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Now, Return the custom logger
        return logger
