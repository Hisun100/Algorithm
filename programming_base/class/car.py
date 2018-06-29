# -*- coding: utf-8 -*-
"""
一次从空白创建一个类的尝试

此脚本可以使你对类有个基础的了解（2018-6-29）
"""

class Car():
    """
    从空白创建一个表示汽车的类-Car，用于模拟汽车，存储有关汽车的信息
    
    说明：根据约定，在Python中，首字母大写的名称指的是类
    """
    
    #方法：类中的函数，用于描述类的行为（动态信息）
    def __init__(self, make, model, year):
        """
           初始化描述汽车的属性
           属性：可以通过实例访问的变量（句点）,用于描述类的信息（静态信息）
           
           说明：以self为前缀的变量都可以供类中的所有方法直接使用
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #给属性指定默认值
        
    def get_descriptive_name(self):
        """
           返回整洁的描述性信息
        """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title() #注意一下title()方法的使用
    
    def update_odometer(self, mileage):
        """
           将汽车里程表读数设置为指定值
           禁止将里程表读数往回调
        """
        #添加一些逻辑,禁止任何人将里程表读数往回调
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Warning: You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """
           增加汽车里程数
        """
        self.odometer_reading += miles
        
    def read_odometer(self):
        """
           获取汽车里程表读数
        """
        print ("This car has " + str(self.odometer_reading) + " miles on it")
        
if __name__ == '__main__':
    #创建实例tony_tesla
    tony_tesla = Car('tesla', 'modelS', 2018)
    print(tony_tesla.make)
    #调用方法
    print(tony_tesla.get_descriptive_name()) #调用方法
    tony_tesla.update_odometer(200) #通过方法间接修改属性值
    tony_tesla.read_odometer()
    tony_tesla.increment_odometer(300)
    tony_tesla.read_odometer()
    tony_tesla.odometer_reading = 600
    tony_tesla.read_odometer()  #通过调用属性直接修改属性值
    
