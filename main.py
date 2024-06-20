class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine_running = False
        self.steering_angle = 0

    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True

        else:
            print("Silnik juz dzialal...")

    def turn(self, dir, angle):
        if dir == "1":
            self.steering_angle -= angle
        else:
            self.steering_angle += angle

    def __str__(self):
        return f"<{self.brand}{self.model}: {self.color}>"


fiat_500 = Car("Fiat", "500", "red")
print(fiat_500)

fiat_500.start_engine()
fiat_500.start_engine()
