from managers import *
# 测试代码
if __name__ == "__main__":
    # 初始化管理类
    faction_manager = FactionManager()
    disciple_manager = DiscipleManager()
    resource_manager = ResourceManager()
    event_manager = EventManager()

    # 创建门派
    faction = faction_manager.create_faction("青云门")
    print(faction)

    # 招募弟子
    disciple = disciple_manager.recruit_disciple("李四", talent=5)
    print(disciple)

    # 培养弟子
    disciple_manager.cultivate_disciple(disciple)
    print(disciple)

    # 添加资源
    resource_manager.add_resource("灵石", 1000)
    print(resource_manager.get_resource_quantity("灵石"))

    # 消耗资源
    resource_manager.consume_resource("灵石", 500)
    print(resource_manager.get_resource_quantity("灵石"))

    # 触发随机事件
    event_manager.trigger_random_event()