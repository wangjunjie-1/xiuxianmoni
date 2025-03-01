# managers/faction_manager.py
from models.faction import Faction
from utils.logger import log_info

class FactionManager:
    def __init__(self):
        self.factions = []  # 所有门派的列表

    def create_faction(self, name):
        """
        创建一个新的门派。
        :param name: 门派名称
        :return: 新创建的门派对象
        """
        faction = Faction(name)
        self.factions.append(faction)
        log_info(f"创建了新的门派: {name}")
        return faction

    def upgrade_faction(self, faction):
        """
        升级门派。
        :param faction: 要升级的门派对象
        """
        if faction.upgrade():
            log_info(f"{faction.name} 升级到了 {faction.level} 级！")
        else:
            log_info(f"{faction.name} 资源不足，无法升级！")

    def disband_faction(self, faction):
        """
        解散门派。
        :param faction: 要解散的门派对象
        """
        self.factions.remove(faction)
        log_info(f"{faction.name} 已被解散！")

    def get_faction_by_name(self, name):
        """
        根据名称查找门派。
        :param name: 门派名称
        :return: 门派对象，如果未找到则返回 None
        """
        for faction in self.factions:
            if faction.name == name:
                return faction
        return None