# models/realm.py
import random


class Realm:
    REALMS = [
        {"name": "凡人境","probability":0.99,"exp_required": 0,           "spirit_power": 0, "spirit_sense": 0,             "lifespan": 100},
        {"name": "炼气境","probability":0.9,"exp_required": 100,          "spirit_power": 10, "spirit_sense": 5,            "lifespan": 150},
        {"name": "筑基境","probability":0.8,"exp_required": 1000,         "spirit_power": 50, "spirit_sense": 20,           "lifespan": 300},
        {"name": "金丹境","probability":0.7,"exp_required": 10000,        "spirit_power": 200, "spirit_sense": 100,         "lifespan": 500},
        {"name": "元婴境","probability":0.6,"exp_required": 100000,       "spirit_power": 1000, "spirit_sense": 500,        "lifespan": 1000},
        {"name": "化神境","probability":0.5,"exp_required": 1000000,      "spirit_power": 5000, "spirit_sense": 2000,       "lifespan": 2000},
        {"name": "合体境","probability":0.4,"exp_required": 10000000,     "spirit_power": 20000, "spirit_sense": 10000,     "lifespan": 5000},
        {"name": "大乘境","probability":0.3,"exp_required": 100000000,    "spirit_power": 100000, "spirit_sense": 50000,    "lifespan": 10000},
        {"name": "渡劫境","probability":0.2,"exp_required": 1000000000,   "spirit_power": 500000, "spirit_sense": 200000,   "lifespan": 20000},
        {"name": "真仙境","probability":0.0,"exp_required": 10000000000,  "spirit_power": 2000000, "spirit_sense": 1000000, "lifespan": -1},  # 长生不老
    ]

    def __init__(self, current_realm_index=0, current_exp=0):
        self.current_realm_index = current_realm_index
        self.current_exp = current_exp

    @property
    def current_realm(self):
        """获取当前境界"""
        return self.REALMS[self.current_realm_index]['name']
    
    @property
    def next_realm(self):
        """获取下一个境界"""
        if self.current_realm_index + 1 < len(self.REALMS):
            return self.REALMS[self.current_realm_index + 1]
        return None

    @property
    def current_realm_info(self):
        """获取当前境界信息"""
        return {
            'exp_current': self.current_exp,
            'exp_required': self.REALMS[self.current_realm_index]['exp_required'],
            'lifespan': self.REALMS[self.current_realm_index]['lifespan'],
            'current_realm': self.current_realm,
            'next_realm': self.next_realm,
        }


    def add_exp(self, exp):
        """增加经验值"""
        self.current_exp += exp
        print(f"获得 {exp} 点经验值，当前经验: {self.current_exp}")


    def breakthrough(self):
        """突破境界"""
        if not self.next_realm:
            print("已达到最高境界，无法继续突破！")
            return

        print(f"突破 {self.current_realm['name']}，进入 {self.next_realm['name']}！")
        self.current_realm_index += 1
        self.current_exp = 0  # 突破后经验值清零

    def update_realm(self,user_probability_now,user_exp_get):
        """更新境界"""
        self.add_exp(user_exp_get)
        if self.current_exp >= self.next_realm['exp_required']:
            if random.random() < user_probability_now:
                self.breakthrough()
            else:
                print(f"突破{self.next_realm['name']}失败")
            

    def __str__(self):
        return str(self.current_realm_info)


# 测试代码
if __name__ == "__main__":
    realm = Realm()
    print(realm)

    realm.add_exp(150)  # 炼气境
    print(realm)

    realm.add_exp(1000)  # 筑基境
    print(realm)