class device:
    def __init__(self, brand, name, size):
        self.brand = brand
        self.name = name
        self.size = size
class coffee_machine(device):
    def __init__(self, brand, name, size, electric):
        super().__init__(brand, name, size)
        self.electric = electric
    def show(self):
        return f"The brand of coffee machine is {self.brand}."

    def size_info(self):
        return f"The brand of coffee machine is {self.brand}."

    def coffee_machine_electric(self):
        if self.electric:
            return f"The brand of coffee machine is {self.brand} and it's electric"
        return f"The brand of coffee machine is {self.brand} and it's mechanical"
class meatgrinder(device):
    def __init__(self, brand, name, size, electric):
        super().__init__(brand, name, size)
        self.electric = electric
    def show(self):
        return f"The brand of meatgrinder is {self.brand}."

    def size_info(self):
        return f"The brand of meatgrinder is {self.brand}."

    def meatgrinder_electric(self):
        if self.electric:
            return f"The brand of meatgrinder is {self.brand} and it's electric"
        return f"The brand of meatgrinder is {self.brand} and it's mechanical"
class blender(device):
    def __init__(self, brand, name, size, electric):
        super().__init__(brand, name, size)
        self.electric = electric
    def show(self):
        return f"The brand of blender is {self.brand}."

    def size_info(self):
        return f"The brand of blender is {self.brand}."

    def blender_electric(self):
        if self.electric:
            return f"The brand of blender is {self.brand} and it's electric"
        return f"The brand of blender is {self.brand} and it's mechanical"
if __name__ == "__main__":
    coffee_machine = coffee_machine("Phillips", "EP1221/20", "37cmx24cm", True)
    print(coffee_machine.show(), coffee_machine.size_info(), coffee_machine.coffee_machine_electric(), sep="\n")

    meatgrinder = meatgrinder("Soviet Production", "Made In USSR", "20cmx30cm", False)
    print(meatgrinder.show(), meatgrinder.size_info(), meatgrinder.meatgrinder_electric(), sep="\n")

    blender = blender("Toshiba", "bl-70pr2nmy", "48cmx20cm", True)
    print(blender.show(), blender.size_info(),blender.blender_electric(), sep="\n")