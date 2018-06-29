# -*- coding: utf-8 -*-
"""
当实例用作属性
"""

#父类
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
        
    def fill_gas_tank():
        """
           测试重写父类功能而添加的方法
           提示加油站工作人员，将汽油箱加满汽油
        """
        print("Please help me fill my car's gas tank.")
        
class Battery():
    """从空白处创建一个类-Battery,用于模拟电动汽车的电瓶"""
    
    def __init__(self, battery_size = 70):
        self.battery_size =  battery_size
        
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a "+ str(self.battery_size) + "-kWh battery.")
        
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)       
               
class ElecticCar(Car):
    """创建一个子类--ElecticCar,用于模拟电动车"""
    
    def __init__(self, make, model, year):
        """
           先初始化父类的属性，在初始化子类的特有属性
        """
        super().__init__(make, model, year) #初始化父类的属性,将父类与子类联系起来
        self.battery = Battery() #创建一个新的实例Battery
       
    def fill_gas_tank(self):
        """
        重写父类：对于父类中方法，若它不符合子类模拟的实物的行为，都可以对其进行重写
        重写父类的fill_gas_tank方法，以适应子类
        """
        print("This car doesn't need a gas tank!")
        
if __name__ == '__main__':
    #创建实例tony_tesla
    tony_tesla = ElecticCar('tesla', 'modelS', 2018)
    print(tony_tesla.get_descriptive_name()) #调用方法
    tony_tesla.fill_gas_tank()
    tony_tesla.battery.describe_battery()
    tony_tesla.battery.get_range()
   
