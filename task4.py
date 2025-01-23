class Car:
    def __init__(self,
                 model:str,
                 brand:str,
                 color:str,
                 year:str,
                 vin:int,
                 engine_type:str,
                 engine_capacity:float,
                 drive_type:str,
                 transmission:str,
                 max_speed:int,
                 price:int
                 ):
        self.model = model
        self.brand = brand
        self.color = color
        self.year = year
        self.vin = vin
        self.engine_type = engine_type
        self.engine_capacity = engine_capacity
        self.drive_type = drive_type
        self.transmission = transmission
        self.max_speed = max_speed
        self.price = price

    def __str__(self):
        return (f'Автомобіль "{self.model} {self.brand}":\n'
                f'колір: {self.color}: \n'
                f'рік: {self.year}: \n'
                f'номер кузову: {self.vin}: \n'
                f'тип двигуна: {self.engine_type}: \n'
                f'об`єм двигуна: {self.engine_capacity} л.: \n'
                f'тип приводу: {self.drive_type}: \n'
                f'тип коробки передач: {self.transmission}: \n'
                f'максимальна швидкість: {self.max_speed}  км/год: \n'
                f'ціна: {self.price}$: \n'
                )


class CarList:
    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def print_car_list(self):
        if not self.cars:
            print("Нажаль, зараз немає автомобілів, доступних до продажу.")
        else:
            print("Список автомобілів, доступних до продажу:")
            for idx, car in enumerate(self.cars, start=1):
                print(f"{idx}. {car}")

    def remove_car_by_vin(self, vin:int):
        for car in self.cars:
            if car.vin == vin:
                self.cars.remove(car)
                print(f'Автомобіль {car.model} {car.brand} (VIN: {vin})\n'
                      'видалено зі списку доступних до продажу автомобілів.')
                print(self.print_car_list())


    def sale_car(self, car:Car):
        if not self.cars:
            print("Всі автомобілі продано!")
        else:
            self.remove_car_by_vin(car.vin)
            print(f"Автомобіль {car.model} {car.brand} було продано за {car.price}")



car1 = Car(
    model="Model S",
    brand="Tesla",
    color="Червоний",
    year="2023",
    vin=12345678901234567,
    engine_type="Електричний",
    engine_capacity=0,
    drive_type="Повний",
    transmission="Автоматична",
    max_speed=250,
    price=60000
)

car2 = Car(
    model="Camry",
    brand="Toyota",
    color="Білий",
    year="2020",
    vin=98765432109876543,
    engine_type="Бензиновий",
    engine_capacity=2.5,
    drive_type="Передній",
    transmission="Автоматична",
    max_speed=210,
    price=55000
)

car3 = Car(
    model="X5",
    brand="BMW",
    color="Чорний",
    year="2022",
    vin=11223344556677889,
    engine_type="Дизельний",
    engine_capacity=3.0,
    drive_type="Повний",
    transmission="Автоматична",
    max_speed=240,
    price=60000
)

car4 = Car(
    model="Mustang",
    brand="Ford",
    color="Синій",
    year="2021",
    vin=66778899001122334,
    engine_type="Бензиновий",
    engine_capacity=5.0,
    drive_type="Задній",
    transmission="Механічна",
    max_speed=260,
    price=65000
)

car5 = Car(
    model="Q7",
    brand="Audi",
    color="Сірий",
    year="2019",
    vin=55667788990011223,
    engine_type="Гібридний",
    engine_capacity=3.0,
    drive_type="Повний",
    transmission="Автоматична",
    max_speed=230,
    price=60000
)

car_list = CarList()

car_list.add_car(car1)
car_list.add_car(car2)
car_list.add_car(car3)
car_list.add_car(car4)
car_list.add_car(car5)

car_list.print_car_list()

car_list.sale_car(car5)
car_list.sale_car(car3)
