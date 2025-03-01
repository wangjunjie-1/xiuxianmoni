# managers/resource_manager.py
from models.resource import Resource
from utils.logger import log_info

class ResourceManager:
    def __init__(self):
        self.resources = {}  # 资源字典，键为资源名称，值为资源对象

    def add_resource(self, name, quantity):
        """
        添加资源。
        :param name: 资源名称
        :param quantity: 资源数量
        """
        if name in self.resources:
            self.resources[name].add(quantity)
        else:
            self.resources[name] = Resource(name, quantity)
        log_info(f"添加了 {quantity} 个 {name}！")

    def consume_resource(self, name, quantity):
        """
        消耗资源。
        :param name: 资源名称
        :param quantity: 消耗数量
        :return: 如果资源足够并成功消耗，返回 True；否则返回 False
        """
        if name in self.resources:
            if self.resources[name].quantity >= quantity:
                self.resources[name].consume(quantity)
                return True
            else:
                log_info(f"{name} 不足，无法消耗！")
                return False
        else:
            log_info(f"{name} 不存在！")
            return False

    def get_resource_quantity(self, name):
        """
        获取资源的数量。
        :param name: 资源名称
        :return: 资源数量，如果资源不存在则返回 0
        """
        if name in self.resources:
            return self.resources[name].quantity
        return 0