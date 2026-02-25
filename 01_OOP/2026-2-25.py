class World:
    """世界（位面）类"""

    def __init__(self, world_name: str, tech_level: int, magic_allowed: bool):
        self.world_name = world_name
        self.tech_level = tech_level  # 科技等级 1-10
        self.magic_allowed = magic_allowed  # 是否允许超凡力量


class Item:
    """物品类（作为随身空间的基础元素）"""

    def __init__(self, name: str, tech_level: int, is_magic: bool):
        self.name = name
        self.tech_level = tech_level
        self.is_magic = is_magic


class Traveler:
    """穿越者主角类"""

    def __init__(self, name: str, current_world: World):
        self.name = name
        self.current_world = current_world
        self.inventory = []  # 随身空间，存放 Item 对象

    def add_item(self, item: Item):
        """拾取物品到随身空间"""
        self.inventory.append(item)
        print(f"🎒 {self.name} 将【{item.name}】收入了随身空间。")

    def travel_to(self, new_world: World):
        """核心动作：穿越到新世界"""
        print(f"\n🌀 正在撕裂空间... {self.name} 开始穿越！")
        print(
            f"📍 目标位面：{new_world.world_name} (科技上限: Lv.{new_world.tech_level}, 允许魔法: {new_world.magic_allowed})")

        self.current_world = new_world
        print("⚖️ 正在进行位面法则扫描...")

        # 遍历随身空间，进行法则校验
        for item in self.inventory:
            sealed = False
            reasons = []

            # 1. 判定科技等级是否超限
            if item.tech_level > new_world.tech_level:
                sealed = True
                reasons.append(f"科技等级过高(物品Lv.{item.tech_level} > 世界Lv.{new_world.tech_level})")

            # 2. 判定魔法物品是否在无魔世界
            if item.is_magic and not new_world.magic_allowed:
                sealed = True
                reasons.append("当前世界为无魔位面，超凡力量沉寂")

            # 输出结果
            if sealed:
                reason_str = "，".join(reasons)
                print(f"⚠️ 警告：因位面法则压制（{reason_str}），您的【{item.name}】已被封印！")
            else:
                print(f"✅ 【{item.name}】法则适配成功，可正常使用。")

        print(f"✨ 穿越完成！当前所在世界：{self.current_world.world_name}\n")