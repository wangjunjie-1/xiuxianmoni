from models import *
# 测试代码
if __name__ == "__main__":
    # 创建玩家
    player = Player("张三")
    print(player)

    # 创建门派
    faction = Faction("青云门")
    print(faction)

    # 玩家加入门派
    player.join_faction(faction)
    print(player)

    # 创建弟子
    disciple = Disciple("李四", talent=5)
    print(disciple)

    # 弟子修炼
    disciple.cultivate()
    print(disciple)

    # 门派升级
    faction.upgrade()
    print(faction)

    # 创建技能
    skill = Skill("九阳神功", cultivation_gain=10, cost=100)
    print(skill)

    # 玩家修炼技能
    player.skills.append(skill)
    player.cultivate(skill)
    print(player)

    # 创建资源
    resource = Resource("灵石", 1000)
    print(resource)

    # 资源操作
    resource.consume(500)
    resource.add(200)
    print(resource)