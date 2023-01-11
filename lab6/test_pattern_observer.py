class Cars:
    def __init__(self, speed):
        self.speed = speed

    def update(self, check):
        print('Suspect {}'.format(check))


class Penalty:
    def __init__(self):
        self.cars = set()

    def register(self, car):
        self.cars.add(car)

    def unregister(self, car):
        self.cars.discard(car)

    def processing(self, check):
        for car in self.cars:
            if car.speed > 60:
                check = 'exceeded the speed limit'
            if car.speed <= 60:
                check = 'did not exceed the speed limit'
            car.update(check)


penalty = Penalty()

suspect1 = Cars(50)
suspect2 = Cars(60)
suspect3 = Cars(90)

penalty.register(suspect1)
penalty.register(suspect2)
penalty.register(suspect3)
penalty.processing("")

""" class Penalty:
    def __init__(self, speed):
        self.speed = speed


def update(speed):
    if speed > 60:
        return print('Подозреваемый превысил скорость на:', speed-60, 'км/ч.')
    elif speed <= 60:
        return print('Подозреваемый не превысил скорость')
    else:
        raise ValueError('Неправильное значение скорости')


suspect = update(70)
 """
