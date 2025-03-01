# utils/logger.py
import logging
from datetime import datetime

# 配置日志格式
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("game.log"),  # 日志写入文件
        logging.StreamHandler()  # 日志输出到控制台
    ]
)

def log_info(message):
    """
    记录信息日志。
    :param message: 日志信息
    """
    logging.info(message)

def log_warning(message):
    """
    记录警告日志。
    :param message: 日志信息
    """
    logging.warning(message)

def log_error(message):
    """
    记录错误日志。
    :param message: 日志信息
    """
    logging.error(message)

def log_debug(message):
    """
    记录调试日志。
    :param message: 日志信息
    """
    logging.debug(message)