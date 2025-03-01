# managers/disciple_manager.py
from models.disciple import Disciple
from utils.logger import log_info

class DiscipleManager:
    def __init__(self):
        self.disciples = []  # 所有弟子的列表

    def recruit_disciple(self, name, talent):
        """
        招募一个新的弟子。
        :param name: 弟子名称
        :param talent: 弟子天赋
        :return: 新招募的弟子对象
        """
        disciple = Disciple(name, talent)
        self.disciples.append(disciple)
        log_info(f"招募了新的弟子: {name}")
        return disciple

    def cultivate_disciple(self, disciple):
        """
        培养弟子，提升其修为。
        :param disciple: 要培养的弟子对象
        """
        disciple.cultivate()
        log_info(f"{disciple.name} 的修为提升到了 {disciple.cultivation_level:.1f}！")

    def promote_disciple(self, disciple, new_role):
        """
        晋升弟子的职位。
        :param disciple: 要晋升的弟子对象
        :param new_role: 新职位
        """
        disciple.role = new_role
        log_info(f"{disciple.name} 被晋升为 {new_role}！")

    def get_disciple_by_name(self, name):
        """
        根据名称查找弟子。
        :param name: 弟子名称
        :return: 弟子对象，如果未找到则返回 None
        """
        for disciple in self.disciples:
            if disciple.name == name:
                return disciple
        return None