# config.py
# 游戏配置常量
GAME_NAME = "修仙门派游戏"
GAME_VERSION = "1.0.0"
GAME_SPEED = 1.0  # 游戏速度（时间流逝速度）

# 资源初始化配置
INITIAL_RESOURCES = {
    "灵石": 1000,
    "丹药": 50,
    "法宝": 10
}

# 弟子天赋范围
TALENT_MIN = 1
TALENT_MAX = 10

# 事件列表
EVENTS = [
    "一只灵兽出现在门派附近！",
    "弟子们在修炼中有所突破！",
    "门派资源增加了！",
    "一场突如其来的风暴袭击了门派！"
]

# 日志配置
LOG_FILE = "game.log"
LOG_LEVEL = "INFO"  # 日志级别：DEBUG, INFO, WARNING, ERROR, CRITICAL