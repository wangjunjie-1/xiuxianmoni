# core/game_engine.py
import time
from utils.logger import log_info

class GameEngine:
    def __init__(self, update_callback=None):
        self.is_running = False  # 游戏运行状态
        self.game_speed = 1.0  # 游戏速度（时间流逝速度）
        self.update_callback = update_callback  # 更新回调函数

    def start(self):
        """启动游戏"""
        self.is_running = True
        log_info("游戏启动！")
        self.main_loop()

    def stop(self):
        """停止游戏"""
        self.is_running = False
        log_info("游戏停止！")

    def main_loop(self):
        """游戏主循环"""
        while self.is_running:
            try:
                # 调用更新回调函数
                if self.update_callback:
                    self.update_callback()
                # 控制游戏速度
                time.sleep(1.0 / self.game_speed)
            except KeyboardInterrupt:
                self.stop()