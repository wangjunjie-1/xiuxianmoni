# models/player.py
class Player:
    def __init__(self, name,age = 16,exp = 0, cultivation_level=1, spiritual_stones=1000):
        """
        初始化玩家角色。
        :param name: 玩家名称
        :param cultivation_level: 修为等级，默认1级
        :param spiritual_stones: 灵石数量，默认1000
        """
        self.name = name
        self.age = age
        self.exp = exp
        self.cultivation_level = cultivation_level
        self.spiritual_stones = spiritual_stones
        self.skills = []  # 玩家学习的功法列表
        self.faction = None  # 玩家所属的门派

    def cultivate(self, skill):
        """
        玩家修炼功法，提升修为。
        :param skill: 修炼的功法对象
        """
        if skill in self.skills:
            self.cultivation_level += skill.cultivation_gain
            print(f"{self.name} 修炼了 {skill.name}，修为提升了 {skill.cultivation_gain}！")
        else:
            print(f"{self.name} 尚未学习 {skill.name}，无法修炼！")

    def join_faction(self, faction):
        """
        玩家加入门派。
        :param faction: 门派对象
        """
        self.faction = faction
        faction.add_member(self)
        print(f"{self.name} 加入了 {faction.name}！")

    def __str__(self):
        return (f"玩家: {self.name}, 修为: {self.cultivation_level}, "
                f"灵石: {self.spiritual_stones}, 门派: {self.faction.name if self.faction else '无'}")