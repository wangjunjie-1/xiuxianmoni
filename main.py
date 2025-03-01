# main.py
from ui.cli_ui import CLIUI
from config import GAME_NAME, GAME_VERSION
import logging
from utils.logger import log_info

def initialize_game():
    """初始化游戏"""
    log_info(f"欢迎来到 {GAME_NAME}！")
    log_info(f"版本: {GAME_VERSION}")
    log_info("游戏初始化中...")

def main():
    """游戏主函数"""
    # 初始化游戏
    initialize_game()

    # 启动命令行界面
    cli_ui = CLIUI()
    cli_ui.run()

if __name__ == "__main__":
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("game.log"),  # 日志写入文件
            logging.StreamHandler()  # 日志输出到控制台
        ]
    )

    # 启动游戏
    main()