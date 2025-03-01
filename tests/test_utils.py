from utils import *
# 测试代码
if __name__ == "__main__":
    # 测试日志工具
    log_info("这是一条信息日志。")
    log_warning("这是一条警告日志。")
    log_error("这是一条错误日志。")
    log_debug("这是一条调试日志。")

    # 测试存档和读档功能
    game_state = {"player": "张三", "level": 10, "resources": 5000}
    save_game(game_state, "test_save")
    loaded_state = load_game("test_save")
    print("加载的游戏状态:", loaded_state)

    # 测试辅助函数
    random_name = generate_random_name()
    print("随机名字:", random_name)

    time_cost = calculate_time_cost(5)
    print("修炼时间:", format_time(time_cost))