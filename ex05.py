# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

class Stationery:
    title = None

    def draw(self):
        print('Start drawing')


class Pen(Stationery):
    def __init__(self):
        Stationery.__init__(self)
        self.title = 'Pen'

    def draw(self):
        print('Pen started drawing')


class Pencil(Stationery):
    def __init__(self):
        Stationery.__init__(self)
        self.title = 'Pencil'

    def draw(self):
        print('Pencil started drawing')


class Handle(Stationery):
    def __init__(self):
        Stationery.__init__(self)
        self.title = 'Handle'

    def draw(self):
        print('Handle started drawing')


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()

