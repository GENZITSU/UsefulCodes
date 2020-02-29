# -*- coding: utf-8 -*-
import time
import json
import logging
import requests
from functools import wraps
from contextlib import contextmanager


def start_logging(filename="job.log"):
    '''loggerを起動させる
    '''
    LOGGER = logging.getLogger('LoggingTest')
    LOGGER.setLevel(10)
    fh = logging.FileHandler(filename)
    LOGGER.addHandler(fh)
    formatter = logging.Formatter('%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')
    fh.setFormatter(formatter)
    return LOGGER


def progress_reporter(text, slack_url="https://hooks.slack.com/services/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"):
    '''該当slackチャンネルにメッセージを送信する
    '''
    data = json.dumps({"text": text, "username": 'progress_report'})
    requests.post(slack_url, data=data)
    return


@contextmanager
def timer(name, LOGGER):
    '''with文で処理にかかる時間を測る
    '''
    LOGGER.info(f"start [{name}]")
    start = time.time()
    yield
    LOGGER.info(f'[{name}] done in {time.time() - start:.0f} s')


@contextmanager
def do_job(name, LOGGER):
    '''with文で処理にかかる時間を測りながらslackに追加
    '''
    LOGGER.info(f"start [{name}]")
    start = time.time()
    try:
        yield
        LOGGER.info(f'[{name}] done in {time.time() - start:.0f} s')
        progress_reporter(f'[{name}] done in {time.time() - start:.0f} s')
    except:
        import traceback, sys
        exc_type, exc_value, exc_traceback = sys.exc_info()
        exc_lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        msg = f"failed {name} \n"
        msg += ''.join('' + line for line in exc_lines)
        LOGGER.info(msg)
        progress_reporter(msg)
        

def measure_time(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        v = f(*args, **kwargs)
        print("elapsed time")
        print(f"{f.__name__}: {round(time.time() - start, 2)}s")
        return v
    return wrapper
        
        
        