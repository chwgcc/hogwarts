# -*- coding: utf-8 -*-
# @Time     : 2020/10/28 19:35
# @Author   : chw
# @File     : bicycle.py

"""
写一个Bicycle（自行车）类，有run(骑行)方法，
调用时显示骑行里程km(骑行里程为传入的数字)；
再写一个电动自行车类EBicycle继承自Bicycle，
添加电池电量valume属性，通过参数传入，同时有两个方法：
1.fill_charge(vol)用来充电，vol为电量，
2.run(km)方法用于骑行，每骑行10km消耗电量1度，
当电量耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果
"""

# 定义Bicycle类
class Bicycle:
    # 定义run方法
    def run(self,km):
        # 传入参数km
        self.km = km
        print(f"自己骑行了{km}千米，累死我了！")

# 定义EBicycle类
# 继承：把父类名称放到类名后面的小括号
class EBicycle(Bicycle):
    # 属性需要传参定义，可以直接放到构造函数中
    def __init__(self, valume):
        self.valume = valume
        # print(f"电池电量为{valume}")

    # 定义fill_charge方法
    def fill_charge(self,vol):
        # 以下可不写，vol为普通变量，在该方法中可直接使用
        # self.vol = vol
        # 充电之后的电量为充电电量vol+电池电量valume
        self.valume = vol + self.valume
        print(f"充了{vol}度电，现在的电量为{self.valume}度电")

    # 定义run方法
    def run(self, km):
        # 1.获取目前电量所能电动骑行的最大里程数
        power_km = self.valume * 10
        if power_km >= km:
            print(f"电动骑行了{km}千米")
        elif power_km < km:
            # 电量不够了，电量用完后，仍需要用脚骑行
            print(f"电动骑行了{power_km}千米")
            # 调用bicycle中的run方法
            # 非继承的调用
            # bike = Bicycle()
            # bike.run(km - power_km)
            # 继承调用
            super().run(km - power_km)




# 构造函数中需要传一个参数，所以实例化的时候也需要将该参数传入
ebike = EBicycle(6)
# 充电时候需要传入一个参数
ebike.run(100)

# bike = Bicycle()
# print(bike.run(5))
