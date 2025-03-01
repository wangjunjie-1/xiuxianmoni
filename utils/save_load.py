# utils/save_load.py
import pickle
import os
from .logger import log_info,log_error
SAVE_DIR = "saves"  # 存档目录

def save_game(game_state, save_name):
    """
    保存游戏状态。
    :param game_state: 游戏状态数据
    :param save_name: 存档名称
    """
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)  # 创建存档目录

    save_path = os.path.join(SAVE_DIR, f"{save_name}.pkl")
    with open(save_path, "wb") as file:
        pickle.dump(game_state, file)
    log_info(f"游戏已保存到 {save_path}")

def load_game(save_name):
    """
    加载游戏状态。
    :param save_name: 存档名称
    :return: 游戏状态数据
    """
    save_path = os.path.join(SAVE_DIR, f"{save_name}.pkl")
    if os.path.exists(save_path):
        with open(save_path, "rb") as file:
            game_state = pickle.load(file)
        log_info(f"从 {save_path} 加载游戏成功！")
        return game_state
    else:
        log_error(f"存档 {save_path} 不存在！")
        return None