# models/skill.py
class Skill:
    def __init__(self, name, cultivation_gain, cost):
        """
        初始化技能。
        :param name: 技能名称
        :param cultivation_gain: 修炼增益（提升的修为值）
        :param cost: 修炼消耗的灵石
        """
        self.name = name
        self.cultivation_gain = cultivation_gain
        self.cost = cost

    def __str__(self):
        return f"功法: {self.name}, 修炼增益: {self.cultivation_gain}, 消耗灵石: {self.cost}"