# models/resource.py
class Resource:
    def __init__(self, name, quantity):
        """
        初始化资源。
        :param name: 资源名称
        :param quantity: 资源数量
        """
        self.name = name
        self.quantity = quantity

    def add(self, amount):
        """
        增加资源数量。
        :param amount: 增加的数量
        """
        self.quantity += amount
        print(f"{self.name} 增加了 {amount}，当前数量: {self.quantity}")

    def consume(self, amount):
        """
        消耗资源数量。
        :param amount: 消耗的数量
        """
        if self.quantity >= amount:
            self.quantity -= amount
            print(f"{self.name} 消耗了 {amount}，当前数量: {self.quantity}")
        else:
            print(f"{self.name} 不足，无法消耗！")

    def __str__(self):
        return f"资源: {self.name}, 数量: {self.quantity}"