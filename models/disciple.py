# models/disciple.py
class Disciple:
    def __init__(self, name, talent, loyalty=100, cultivation_level=1):
        """
        初始化弟子。
        :param name: 弟子名称
        :param talent: 天赋值（影响修炼速度）
        :param loyalty: 忠诚度（默认100）
        :param cultivation_level: 修为等级（默认1级）
        """
        self.name = name
        self.talent = talent
        self.loyalty = loyalty
        self.cultivation_level = cultivation_level

    def cultivate(self):
        """
        弟子修炼，提升修为。
        """
        self.cultivation_level += self.talent * 0.1
        print(f"{self.name} 修炼中... 修为提升至 {self.cultivation_level:.1f}！")

    def __str__(self):
        return (f"弟子: {self.name}, 天赋: {self.talent}, "
                f"忠诚度: {self.loyalty}, 修为: {self.cultivation_level:.1f}")