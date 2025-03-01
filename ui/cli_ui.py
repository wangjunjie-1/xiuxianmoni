# ui/cli_ui.py
from managers.faction_manager import FactionManager
from managers.disciple_manager import DiscipleManager
from managers.resource_manager import ResourceManager
from managers.event_manager import EventManager
from utils.logger import log_info

class CLIUI:
    def __init__(self):
        self.faction_manager = FactionManager()
        self.disciple_manager = DiscipleManager()
        self.resource_manager = ResourceManager()
        self.event_manager = EventManager()
        self.current_faction = None  # 当前选中的门派

    def show_main_menu(self):
        """显示主菜单"""
        print("\n===== 修仙门派游戏 =====")
        print("1. 创建门派")
        print("2. 管理门派")
        print("3. 招募弟子")
        print("4. 培养弟子")
        print("5. 管理资源")
        print("6. 触发事件")
        print("7. 退出游戏")
        choice = input("请选择操作: ")
        return choice

    def create_faction(self):
        """创建门派"""
        name = input("请输入门派名称: ")
        faction = self.faction_manager.create_faction(name)
        self.current_faction = faction
        print(f"门派 {name} 创建成功！")

    def manage_faction(self):
        """管理门派"""
        if not self.current_faction:
            print("请先创建一个门派！")
            return

        print(f"\n当前门派: {self.current_faction.name}")
        print("1. 升级门派")
        print("2. 解散门派")
        choice = input("请选择操作: ")

        if choice == "1":
            self.faction_manager.upgrade_faction(self.current_faction)
        elif choice == "2":
            self.faction_manager.disband_faction(self.current_faction)
            self.current_faction = None
        else:
            print("无效的选择！")

    def recruit_disciple(self):
        """招募弟子"""
        if not self.current_faction:
            print("请先选择一个门派！")
            return

        name = input("请输入弟子名称: ")
        talent = int(input("请输入弟子天赋 (1-10): "))
        disciple = self.disciple_manager.recruit_disciple(name, talent)
        self.current_faction.add_member(disciple)
        print(f"弟子 {name} 招募成功！")

    def cultivate_disciple(self):
        """培养弟子"""
        if not self.current_faction:
            print("请先选择一个门派！")
            return

        name = input("请输入弟子名称: ")
        disciple = self.disciple_manager.get_disciple_by_name(name)
        if disciple:
            self.disciple_manager.cultivate_disciple(disciple)
        else:
            print(f"未找到弟子 {name}！")

    def manage_resources(self):
        """管理资源"""
        print("\n资源管理")
        print("1. 添加资源")
        print("2. 消耗资源")
        choice = input("请选择操作: ")

        if choice == "1":
            name = input("请输入资源名称: ")
            quantity = int(input("请输入资源数量: "))
            self.resource_manager.add_resource(name, quantity)
        elif choice == "2":
            name = input("请输入资源名称: ")
            quantity = int(input("请输入消耗数量: "))
            if self.resource_manager.consume_resource(name, quantity):
                print(f"成功消耗 {quantity} 个 {name}！")
            else:
                print(f"无法消耗 {quantity} 个 {name}！")
        else:
            print("无效的选择！")

    def trigger_event(self):
        """触发事件"""
        event = self.event_manager.trigger_random_event()
        print(f"事件: {event}")

    def run(self):
        """运行游戏"""
        while True:
            choice = self.show_main_menu()
            if choice == "1":
                self.create_faction()
            elif choice == "2":
                self.manage_faction()
            elif choice == "3":
                self.recruit_disciple()
            elif choice == "4":
                self.cultivate_disciple()
            elif choice == "5":
                self.manage_resources()
            elif choice == "6":
                self.trigger_event()
            elif choice == "7":
                print("退出游戏，再见！")
                break
            else:
                print("无效的选择，请重新输入！")