import os, platform

from loguru import logger

VERSION = '1.3.10'
BASE_URL = 'https://login.weixin.qq.com'
OS = platform.system() # Windows, Linux, Darwin
# append dir with subdir img
DIR = os.path.join(os.getcwd(), 'img')
logger.info(f'Using dir: {DIR}')
DEFAULT_QR = 'QR.png'
TIMEOUT = (10, 60)

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
