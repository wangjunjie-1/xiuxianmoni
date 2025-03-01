# ui/tk_ui.py
import tkinter as tk
from tkinter import messagebox
from managers.faction_manager import FactionManager
from managers.disciple_manager import DiscipleManager
from managers.resource_manager import ResourceManager
from managers.event_manager import EventManager

class TkUI:
    def __init__(self, root):
        self.root = root
        self.root.title("修仙门派游戏")
        self.root.geometry("1000x400")

        # 初始化管理类
        self.faction_manager = FactionManager()
        self.disciple_manager = DiscipleManager()
        self.resource_manager = ResourceManager()
        self.event_manager = EventManager()
        self.current_faction = None

        # 创建主界面
        self.create_main_menu()
    def create_main_menu(self):
        """创建主菜单界面"""
        self.clear_window()

        # 配置列的权重
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(6, weight=1)

        # 标题
        tk.Label(self.root, text="===== 修仙门派游戏 =====", font=("Arial", 16)).grid(row=1, column=1, columnspan=5, pady=10)

        # 创建个人 Frame
        personal_frame = tk.Frame(self.root, bg="lightblue", bd=2, relief="sunken")
        personal_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.create_personal_frame(personal_frame)

        # 创建宗门 Frame
        faction_frame = tk.Frame(self.root, bg="lightgreen", bd=2, relief="sunken")
        faction_frame.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        self.create_faction_frame(faction_frame)

        # 创建系统 Frame
        system_frame = tk.Frame(self.root, bg="lightcoral", bd=2, relief="sunken")
        system_frame.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")
        self.create_system_frame(system_frame)

        # 创建宗门信息 Frame
        faction_info_frame = tk.Frame(self.root, bg="lightyellow", bd=2, relief="sunken")
        faction_info_frame.grid(row=2, column=4, padx=10, pady=10, sticky="nsew")
        self.create_faction_info_frame(faction_info_frame)

        # 创建个人信息 Frame
        personal_info_frame = tk.Frame(self.root, bg="lightpink", bd=2, relief="sunken")
        personal_info_frame.grid(row=2, column=5, padx=10, pady=10, sticky="nsew")
        self.create_personal_info_frame(personal_info_frame)

    def create_personal_frame(self, personal_frame):
        """创建个人 Frame"""
        tk.Label(personal_frame, text="【个人】", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(personal_frame, text="修炼", width=15).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(personal_frame, text="探索", width=15).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(personal_frame, text="炼丹", width=15).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(personal_frame, text="炼器", width=15).grid(row=4, column=0, padx=10, pady=10)

    def create_faction_frame(self, faction_frame):
        """创建宗门 Frame"""
        tk.Label(faction_frame, text="【宗门】", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(faction_frame, text="创建门派", width=15).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(faction_frame, text="管理门派", width=15).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(faction_frame, text="招募弟子", width=15).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(faction_frame, text="培养弟子", width=15).grid(row=4, column=0, padx=10, pady=10)

    def create_system_frame(self, system_frame):
        """创建系统 Frame"""
        tk.Label(system_frame, text="【系统】", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(system_frame, text="触发事件", width=15).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(system_frame, text="退出游戏", width=15).grid(row=2, column=0, padx=10, pady=10)

    def create_faction_info_frame(self, faction_info_frame):
        """创建宗门信息 Frame"""
        # 标题
        tk.Label(faction_info_frame, text="【宗门信息】", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # 创建 Text 组件
        info_text = tk.Text(faction_info_frame, width=30, height=10, wrap=tk.WORD)
        info_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # 添加滚动条
        scrollbar = tk.Scrollbar(faction_info_frame, command=info_text.yview)
        scrollbar.grid(row=1, column=2, sticky="ns")
        info_text.config(yscrollcommand=scrollbar.set)

        # 插入宗门信息
        faction_info = (
            "名称:\t 青云门\t\n"
            "等级:\t 3\t\n"
            "灵石:\t 1000\t\n"
            "灵药:\t 50\t\n"
            "内门:\t 10\t\n"
            "外门:\t 20\t\n"
        )
        info_text.insert(tk.END, faction_info)
        info_text.config(state=tk.DISABLED)  # 设置为只读

      

    def create_personal_info_frame(self, personal_info_frame):
        """创建个人信息 Frame"""
        tk.Label(personal_info_frame, text="【个人信息】", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)
        # 创建 Text 组件
        info_text = tk.Text(personal_info_frame, width=30, height=10, wrap=tk.WORD)
        info_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # 添加滚动条
        scrollbar = tk.Scrollbar(personal_info_frame, command=info_text.yview)
        scrollbar.grid(row=1, column=2, sticky="ns")
        info_text.config(yscrollcommand=scrollbar.set)

        # 插入宗门信息
        faction_info = (
            "名称: 龙傲天\n"
            "境界: 道台\n"
        )
        info_text.insert(tk.END, faction_info)
        info_text.config(state=tk.DISABLED)  # 设置为只读

    def clear_window(self):
        """清空窗口内容"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_faction(self):
        """创建门派"""
        self.clear_window()

        tk.Label(self.root, text="创建门派", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="门派名称:").pack()
        faction_name_entry = tk.Entry(self.root)
        faction_name_entry.pack(padx=2,pady=5)

        def on_create():
            name = faction_name_entry.get()
            if name:
                self.current_faction = self.faction_manager.create_faction(name)
                messagebox.showinfo("成功", f"门派 {name} 创建成功！")
                self.create_main_menu()
            else:
                messagebox.showwarning("错误", "请输入门派名称！")

        tk.Button(self.root, text="创建", command=on_create).pack(pady=10)
        tk.Button(self.root, text="返回", command=self.create_main_menu).pack(padx=2,pady=5)

    def manage_faction(self):
        """管理门派"""
        if not self.current_faction:
            messagebox.showwarning("错误", "请先创建一个门派！")
            return

        self.clear_window()

        tk.Label(self.root, text="管理门派", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text=f"当前门派: {self.current_faction.name}").pack()

        tk.Button(self.root, text="升级门派", command=self.upgrade_faction).pack(padx=2,pady=5)
        tk.Button(self.root, text="解散门派", command=self.disband_faction).pack(padx=2,pady=5)
        tk.Button(self.root, text="返回", command=self.create_main_menu).pack(padx=2,pady=5)

    def upgrade_faction(self):
        """升级门派"""
        if self.faction_manager.upgrade_faction(self.current_faction):
            messagebox.showinfo("成功", f"{self.current_faction.name} 升级到了 {self.current_faction.level} 级！")
        else:
            messagebox.showwarning("错误", f"{self.current_faction.name} 资源不足，无法升级！")
        self.manage_faction()

    def disband_faction(self):
        """解散门派"""
        self.faction_manager.disband_faction(self.current_faction)
        self.current_faction = None
        messagebox.showinfo("成功", "门派已解散！")
        self.create_main_menu()

    def recruit_disciple(self):
        """招募弟子"""
        if not self.current_faction:
            messagebox.showwarning("错误", "请先选择一个门派！")
            return

        self.clear_window()

        tk.Label(self.root, text="招募弟子", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="弟子名称:").pack()
        disciple_name_entry = tk.Entry(self.root)
        disciple_name_entry.pack(padx=2,pady=5)

        tk.Label(self.root, text="弟子天赋 (1-10):").pack()
        disciple_talent_entry = tk.Entry(self.root)
        disciple_talent_entry.pack(padx=2,pady=5)

        def on_recruit():
            name = disciple_name_entry.get()
            talent = disciple_talent_entry.get()
            if name and talent.isdigit() and 1 <= int(talent) <= 10:
                disciple = self.disciple_manager.recruit_disciple(name, int(talent))
                self.current_faction.add_member(disciple)
                messagebox.showinfo("成功", f"弟子 {name} 招募成功！")
                self.create_main_menu()
            else:
                messagebox.showwarning("错误", "请输入有效的名称和天赋！")

        tk.Button(self.root, text="招募", command=on_recruit).pack(pady=10)
        tk.Button(self.root, text="返回", command=self.create_main_menu).pack(padx=2,pady=5)

    def cultivate_disciple(self):
        """培养弟子"""
        if not self.current_faction:
            messagebox.showwarning("错误", "请先选择一个门派！")
            return

        self.clear_window()

        tk.Label(self.root, text="培养弟子", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="弟子名称:").pack()
        disciple_name_entry = tk.Entry(self.root)
        disciple_name_entry.pack(padx=2,pady=5)

        def on_cultivate():
            name = disciple_name_entry.get()
            disciple = self.disciple_manager.get_disciple_by_name(name)
            if disciple:
                self.disciple_manager.cultivate_disciple(disciple)
                messagebox.showinfo("成功", f"{disciple.name} 的修为提升到了 {disciple.cultivation_level:.1f}！")
                self.create_main_menu()
            else:
                messagebox.showwarning("错误", f"未找到弟子 {name}！")

        tk.Button(self.root, text="培养", command=on_cultivate).pack(pady=10)
        tk.Button(self.root, text="返回", command=self.create_main_menu).pack(padx=2,pady=5)

    def manage_resources(self):
        """管理资源"""
        self.clear_window()

        tk.Label(self.root, text="管理资源", font=("Arial", 14)).pack(pady=10)

        tk.Button(self.root, text="添加资源", command=self.add_resource).pack(padx=2,pady=5)
        tk.Button(self.root, text="消耗资源", command=self.consume_resource).pack(padx=2,pady=5)
        tk.Button(self.root, text="返回", command=self.create_main_menu).pack(padx=2,pady=5)

    def add_resource(self):
        """添加资源"""
        self.clear_window()

        tk.Label(self.root, text="添加资源", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="资源名称:").pack()
        resource_name_entry = tk.Entry(self.root)
        resource_name_entry.pack(padx=2,pady=5)

        tk.Label(self.root, text="资源数量:").pack()
        resource_quantity_entry = tk.Entry(self.root)
        resource_quantity_entry.pack(padx=2,pady=5)

        def on_add():
            name = resource_name_entry.get()
            quantity = resource_quantity_entry.get()
            if name and quantity.isdigit():
                self.resource_manager.add_resource(name, int(quantity))
                messagebox.showinfo("成功", f"添加了 {quantity} 个 {name}！")
                self.manage_resources()
            else:
                messagebox.showwarning("错误", "请输入有效的名称和数量！")

        tk.Button(self.root, text="添加", command=on_add).pack(pady=10)
        tk.Button(self.root, text="返回", command=self.manage_resources).pack(padx=2,pady=5)

    def consume_resource(self):
        """消耗资源"""
        self.clear_window()

        tk.Label(self.root, text="消耗资源", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="资源名称:").pack()
        resource_name_entry = tk.Entry(self.root)
        resource_name_entry.pack(padx=2,pady=5)

        tk.Label(self.root, text="消耗数量:").pack()
        resource_quantity_entry = tk.Entry(self.root)
        resource_quantity_entry.pack(padx=2,pady=5)

        def on_consume():
            name = resource_name_entry.get()
            quantity = resource_quantity_entry.get()
            if name and quantity.isdigit():
                if self.resource_manager.consume_resource(name, int(quantity)):
                    messagebox.showinfo("成功", f"成功消耗 {quantity} 个 {name}！")
                else:
                    messagebox.showwarning("错误", f"无法消耗 {quantity} 个 {name}！")
                self.manage_resources()
            else:
                messagebox.showwarning("错误", "请输入有效的名称和数量！")

        tk.Button(self.root, text="消耗", command=on_consume).pack(pady=10)
        tk.Button(self.root, text="返回", command=self.manage_resources).pack(padx=2,pady=5)

    def trigger_event(self):
        """触发事件"""
        event = self.event_manager.trigger_random_event()
        messagebox.showinfo("事件触发", event)