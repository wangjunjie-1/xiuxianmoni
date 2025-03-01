# core/world.py
from utils.logger import log_info
import random
class World:
    def __init__(self):
        self.time_elapsed = 0  # 游戏时间（秒）
        self.weather = "晴天"  # 当前天气

    def update(self):
        """更新世界状态"""
        self.time_elapsed += 1
        self.change_weather()
        log_info(f"游戏时间: {self.format_time(self.time_elapsed)}, 天气: {self.weather}")

    def change_weather(self):
        """随机改变天气"""
        if self.time_elapsed % 10 == 0:  # 每10秒改变一次天气
            weather_options = ["晴天", "雨天", "阴天", "雪天"]
            self.weather = random.choice(weather_options)

    @staticmethod
    def format_time(seconds):
        """将秒数格式化为更易读的时间字符串"""
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours)}小时 {int(minutes)}分钟 {int(seconds)}秒"