class Car:
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year
        self.odometer_read = 0

    def car_description(self):
        long_name = f'{self.maker} {self.model} {self.year}, {self.odometer_read/1000} tys. km'
        return long_name.title()

    def read_odometer(self):
        print(f'Stan licznika: {self.odometer_read}km')

    def update_odometer(self, mileage):
        self.odometer_read = mileage
        if mileage >= self.odometer_read:
            self.odometer_read = mileage
        else:
            print("It's not nice to cheat on the mileage")

    def increment_odometer(self, kilometers):
        self.odometer_read += kilometers


my_car = Car('hyundai', 'sonata', 2009)

my_car.update_odometer(250_000)

my_car.increment_odometer(100)

print(my_car.car_description())


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'Ten samochód ma akumulator o pojemnośi {self.battery_size} kWh.')

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f'Zasięg tego samochodu wynosi około {range} km,'
              f'po pełnym naładowaniu baterii.')


class ElectricCar(Car):
    def __init__(self, maker, model, year):
        super().__init__(maker, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.car_description())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
