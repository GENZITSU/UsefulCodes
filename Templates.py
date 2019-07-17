################
# loggerの生成 #
###############

import logging

logger = logging.getLogger('LoggingTest')
logger.setLevel(10)
fh = logging.FileHandler('data_preparation.log')
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')
fh.setFormatter(formatter)
logger.info("hello")


################
# 例外処理の報告 #
###############

from utils import progress_reporter

try:
    pass

except:
    import traceback, sys

    exc_type, exc_value, exc_traceback = sys.exc_info()
    exc_lines = traceback.format_exception(exc_type, exc_value, exc_traceback)

    msg = f"failed execute hogehoge \n"
    msg += ''.join('' + line for line in exc_lines)
    logger.info(msg)
    progress_reporter(msg)