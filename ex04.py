# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    _is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'{self.name} started ride')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self, direction):
        print(f'{self.name} turned to the {direction}')

    def show_speed(self):
        return self.speed

    def is_police(self):
        return self._is_police


class TownCar(Car):
    def __init__(self, speed, color, name, max_speed):
        Car.__init__(self, speed, color, name)
        self.max_speed = max_speed

    def show_speed(self):
        return self.speed if self.speed <= self.max_speed else f'{self.speed} ' \
                                                               f'!!!Over speed by {self.speed - self.max_speed}'


class SportCar(Car):
    pass


class WorkCar(TownCar):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self._is_police = True


cars = [TownCar(70, 'white', 'CitiGo', 60), SportCar(100, 'red', 'Rapid'), WorkCar(40, 'blue', 'Roomster', 40),
        PoliceCar(150, 'silver', 'Octavia')]

for c in cars:
    print(f'Car: {c.name}, color: {c.color}, is police: {c.is_police()}, speed: {c.show_speed()}')
    c.go()
    c.turn('left')
    c.stop()

