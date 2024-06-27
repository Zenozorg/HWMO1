class ship:
    def __init__(self, name, size, speed):
        self.name = name
        self.size = size
        self.speed = speed
class frigate(ship):
    def __init__(self, name, size, speed, outdated):
        super().__init__(name, size, speed)
        self.outdated = outdated
    def show(self):
        return f"The name of frigate is {self.name}."

    def speed_info(self):
        return f"The name of frigate is {self.name}."

    def frigate_outdated(self):
        if self.outdated:
            return f"The name of frigate is {self.name} and it's outdated"
        return f"The name of frigate is {self.name} and it's still in use"
class destroyer(ship):
    def __init__(self, name, size, speed, outdated):
        super().__init__(name, size, speed)
        self.outdated = outdated
    def show(self):
        return f"The name of destroyer is {self.name}."

    def speed_info(self):
        return f"The name of destroyer is {self.name}."

    def destroyer_outdated(self):
        if self.outdated:
            return f"The name of destroyer is {self.name} and it's outdated"
        return f"The name of destroyer is {self.name} and it's still in use"
class cruiser(ship):
    def __init__(self, name, size, speed, outdated):
        super().__init__(name, size, speed)
        self.outdated = outdated
    def show(self):
        return f"The name of cruiser is {self.name}."

    def speed_info(self):
        return f"The name of cruiser is {self.name}."

    def cruiser_outdated(self):
        if self.outdated:
            return f"The name of cruiser is {self.name} and it's outdated"
        return f"The name of cruiser is {self.name} and it's still in use"
if __name__ == "__main__":
    frigate = frigate("Bismarck", "251m", "55.58 km/h", True)
    print(frigate.show(), frigate.speed_info(), frigate.frigate_outdated(), sep="\n")

    destroyer = destroyer("Uss Aetna", "4", "mammal", False)
    print(destroyer.show(), destroyer.speed_info(), destroyer.destroyer_outdated(), sep="\n")

    cruiser = cruiser("Dorsetshire", "192.86 m", "58.3 km/h", True)
    print(cruiser.show(), cruiser.speed_info(),cruiser.cruiser_outdated(), sep="\n")