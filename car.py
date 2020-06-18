class Car():
    #创建一个汽车父类

    def __init__(self, manufacturer, model, year):
#初始化描述汽车的属性       
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        #返回汽车的描述性信息
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
      #打印汽车里程表信息
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
       #将汽车里程表读取为指定的值,禁止里程表回调
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
       #将里程表读数增加相应的值
        self.odometer_reading += miles
