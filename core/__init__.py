# core/__init__.py
from .game_engine import GameEngine
from .world import World
from .event_system import EventSystem

class Core:
    def __init__(self):
        self.world = World()
        self.event_system = EventSystem()
        self.engine = GameEngine(update_callback=self.update)  # 将 update 方法作为回调传入

    def start(self):
        """启动游戏核心逻辑"""
        self.engine.start()

    def update(self):
        """更新游戏核心逻辑"""
        self.world.update()
        if self.world.time_elapsed % 5 == 0:  # 每5秒触发一次事件
            self.event_system.trigger_random_event()