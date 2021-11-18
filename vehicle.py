class Vehicle:

    def __init__(self, name, v_max, mileage):
        self.mileage = mileage
        self.v_max = v_max
        self.name = name

    def drive(self):
        print(f'Vehicle {self.name} is moving...')

    def stop(self):
        print(f'Vehicle {self.name} stopped')


class Car(Vehicle):

    def __init__(self, name, v_max, mileage):
        super().__init__(name, v_max, mileage)
        self.capacity = 5

    def show_capacity(self):
        print(f'Capacity: {self.capacity}')


class Truck(Vehicle):
    def __init__(self, name, v_max, mileage):
        super().__init__(name, v_max, mileage)
        self.capacity = 2

    def show_capacity(self):
        print(f'Capacity: {self.capacity}')


if __name__ == '__main__':
    car = Car(name='Golf', v_max=140, mileage=175000)
    car.drive()
    car.stop()
    car.show_capacity()

    truck = Truck(name='Man', v_max=140, mileage=175000)
    truck.drive()
    truck.stop()
    truck.show_capacity()
