import logging
import sys

class Logger:

        @staticmethod
        def init(logFile, logLevel):
                logger = logging.getLogger()
                fileHandler = logging.FileHandler(logFile)
                formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                fileHandler.setFormatter(formatter)

                console = logging.StreamHandler(sys.stdout)
                console.setLevel(logging.DEBUG)
                console_formatter = logging.Formatter('%(levelname)s %(message)s')
                console.setFormatter(console_formatter)

                logger.addHandler(console)

                logger.addHandler(fileHandler)
                logger.setLevel(logLevel)

