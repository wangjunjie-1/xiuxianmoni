game/
│
├── main.py                  # 游戏入口文件，启动游戏
├── config.py                # 游戏配置文件，存储常量、配置参数
├── README.md                # 项目说明文档
│
├── core/                    # 核心游戏逻辑模块
│   ├── __init__.py
│   ├── game_engine.py       # 游戏引擎，负责游戏主循环和事件调度
│   ├── world.py             # 游戏世界管理，包括地图、时间流逝等
│   └── event_system.py      # 事件系统，处理游戏中的事件触发
│
├── models/                  # 数据模型模块
│   ├── __init__.py
│   ├── player.py            # 玩家角色类
│   ├── disciple.py          # 弟子类
│   ├── faction.py          # 门派类
│   ├── skill.py            # 技能/功法类
│   └── resource.py          # 资源类（灵石、丹药等）
│
├── managers/                # 管理模块，负责游戏中的各种管理逻辑
│   ├── __init__.py
│   ├── faction_manager.py   # 门派管理，包括创建、升级、解散等
│   ├── disciple_manager.py  # 弟子管理，包括招募、培养、晋升等
│   ├── resource_manager.py  # 资源管理，包括资源获取、消耗等
│   └── event_manager.py     # 事件管理，处理随机事件和剧情
│
├── utils/                   # 工具模块
│   ├── __init__.py
│   ├── logger.py            # 日志工具
│   ├── save_load.py         # 存档和读档功能
│   └── helpers.py           # 辅助函数，如随机数生成、时间计算等
│
├── ui/                      # 用户界面模块
│   ├── __init__.py
│   ├── cli_ui.py            # 命令行界面（CLI）实现
│   └── gui_ui.py            # 图形界面（GUI）实现（可选）
│
└── tests/                   # 测试模块
    ├── __init__.py
    ├── test_models.py       # 数据模型测试
    ├── test_managers.py     # 管理逻辑测试
    └── test_utils.py        # 工具函数测试

更新目录：
1. models模块增加日志信息
2. log-info增加颜色和等级，每个模块的info应该颜色不同
3. 