# 封装，私有化属性
class Car:
    def __init__(self,brand,model,color,owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner =owner

    def start(self):
            print(f'{self.brand} {self.model}正在启动')

    def run(self):
            print(f'{self.brand} {self.model}正在行驶')

    def stop(self):
            print(f'{self.brand} {self.model}正在行驶')
    def __control_fuel(self):
            print(f'{self.brand} {self.model}正在控制燃油')
    def charge(self):
            print(f'{self.brand} {self.model}正在充电')

# if __name__=='__main__':
#     car = Car('audi','A6','red','张三')
#     # print(car.brand)
#     # print(car.model)
#     # print(car.color)
#     # car.run()
#     # car.stop()
#     # car.start()
#     print(car._Car__owner)


# 2.继承
# 继承-重写父类方法
class FuelCar(Car):
    def charge(self):
        print(f'{self.brand} {self.model}正在加油')
        Car.charge(self)


if __name__ == '__main__':
    car = FuelCar('audi','A6','red','张三')
    car.charge()

# 3.多重继承方法在一个子类括号中加入多个父类
# 其解析遵循MRO