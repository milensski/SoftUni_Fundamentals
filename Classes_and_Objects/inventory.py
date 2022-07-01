class Inventory:
    __count = 0

    def __init__(self, capacity: int):
        self.__capacity = capacity
        Inventory.__count = capacity
        self.items = []

    def add_item(self, item: str):
        if self.__capacity > 0:
            self.items.append(item)
            self.__capacity -= 1
            return 'added item'
        else:
            return 'not enough room in the inventory'

    def get_capacity(self):
        return Inventory.__count

    def __repr__(self):
        return f'Items: {", ".join(self.items)}.\nCapacity left: {self.__capacity}'


inventory = Inventory(3)
print(inventory.add_item("potion"))
print(inventory.add_item("sword"))
print(inventory.add_item("bottle"))
print(inventory.add_item("sword"))
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
