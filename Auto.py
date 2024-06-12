# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и
# метод def horse_powers, которая возвращает количество лошадиных сил для автомобиля
# Создайте наследника класса Car - класс Nissan и переопределите свойство price,
# а также переопределите метод horse_powers
# Дополнительно создайте класс Kia, который также будет наследником класса Car и
# переопределите также свойство price, а также переопределите метод horse_powers


class Car:
    price = 1000000
    powers = 0


    def horse_powers(self, name, powers):
        self.powers = powers
        self.name = name
        print(f'Мощность автомобиля {self.name} {self.powers} л/с')


class Nissan(Car):
    price = 2000000

    print(f'Автомобиль Nissan, стоимость {price} руб.')


class Kia(Car):
    price = 1800000
    print(f'Автомобиль Kia, стоимость {price} руб.')

car1 = Nissan()
car1.horse_powers("Nissan", 150)

car2 = Kia()
car2.horse_powers("Kia", 200)