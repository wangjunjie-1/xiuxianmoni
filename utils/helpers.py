# utils/helpers.py
import random
import time

def generate_random_name():
    """
    生成随机名字（用于弟子或门派）。
    :return: 随机名字
    """
    first_names = ["李", "王", "张", "刘", "陈", "杨", "赵", "黄", "周", "吴"]
    last_names = ["伟", "芳", "娜", "敏", "静", "秀英", "丽", "强", "磊", "洋"]
    return random.choice(first_names) + random.choice(last_names)

def calculate_time_cost(cultivation_level):
    """
    计算修炼所需的时间（根据修为等级）。
    :param cultivation_level: 修为等级
    :return: 时间（秒）
    """
    return cultivation_level * 10  # 修为等级越高，修炼时间越长

def format_time(seconds):
    """
    将秒数格式化为更易读的时间字符串。
    :param seconds: 秒数
    :return: 格式化后的时间字符串
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)}小时 {int(minutes)}分钟 {int(seconds)}秒"