class WithEngine:
    def __init__(self):
        self.engine_running = False

    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            print("Startuje silnik...")
        else:
            print("Silnik juz dzialal...")


class Car(WithEngine):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def __str__(self):
        return f"[{self.brand}{self.model}: {self.color}]"


class Fiat500(Car):
    brand = "Fiat"
    model = "500"
    cars_count = 0
    registrations = []

    def __init__(self, color, registration):
        super().__init__(color=color)
        Fiat500.cars_count += 1
        Fiat500.registrations.append(registration)


class Fiat600(Car):
    brand = "Fiat"
    model = "600"
    cars_count = 0
    registrations = []

    def __init__(self, color, registration):
        super().__init__(color=color)
        Fiat600.cars_count += 1
        Fiat600.registrations.append(registration)


class Heli(WithEngine):
    def start_engine(self):
        self.radio = "on"
        super().start_engine()


f5 = Fiat500("black", "WA1")
f6 = Fiat600("red", "KR1")

f5.start_engine()
f6.start_engine()

print(f5)
print(f6)
