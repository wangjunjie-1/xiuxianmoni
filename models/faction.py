# models/faction.py
class Faction:
    def __init__(self, name, level=1, resources=1000):
        """
        初始化门派。
        :param name: 门派名称
        :param level: 门派等级（默认1级）
        :param resources: 门派资源（默认1000）
        """
        self.name = name
        self.level = level
        self.resources = resources
        self.members = []  # 门派成员列表

    def add_member(self, member):
        """
        添加成员到门派。
        :param member: 成员对象（玩家或弟子）
        """
        self.members.append(member)
        print(f"{member.name} 加入了 {self.name}！")

    def upgrade(self):
        """
        门派升级。
        """
        required_resources = self.level * 1000
        if self.resources >= required_resources:
            self.resources -= required_resources
            self.level += 1
            print(f"{self.name} 升级到了 {self.level} 级！")
        else:
            print(f"{self.name} 资源不足，无法升级！")

    def __str__(self):
        return (f"门派: {self.name}, 等级: {self.level}, "
                f"资源: {self.resources}, 成员数量: {len(self.members)}")