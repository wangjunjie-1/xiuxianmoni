# core/event_system.py
import random
from utils.logger import log_info

class EventSystem:
    def __init__(self):
        self.events = [
            "一只灵兽出现在门派附近！",
            "弟子们在修炼中有所突破！",
            "门派资源增加了！",
            "一场突如其来的风暴袭击了门派！"
        ]

    def trigger_random_event(self):
        """触发随机事件"""
        event = random.choice(self.events)
        log_info(f"事件触发: {event}")
        return event