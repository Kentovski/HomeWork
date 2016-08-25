# /usr/bin/python3

# MELNIKOV ILYA

import json


class House:
    def __init__(self, adress, floors, rooms):
        self.adress = adress
        self.floors = floors
        self.rooms = rooms


class Room:
    def __init__(self, coord, height, width, length, windows, doors, furniture):
        self.coord = coord
        self.height = height
        self.width = width
        self.length = length
        self.windows = windows
        self.doors = doors
        self.furniture = furniture


class Windows:
    def __init__(self, coords, height, width, material, mode):
        self.coords = coords
        self.height = height
        self.width = width
        self.material = material
        self.mode = mode

    def open(self):
        self.mode = True

    def turn_off(self):
        self.mode = False


class Doors:
    def __init__(self, coords, height, width, material, mode):
        self.coords = coords
        self.height = height
        self.width = width
        self.material = material
        self.mode = mode

    def open(self):
        self.mode = True

    def turn_off(self):
        self.mode = False


class Kitchen(Room):
    pass


class Bedroom(Room):
    pass


class Bathroom(Room):
    pass


class Furniture:
    def __init__(self, coord, height, width, length, material, color):
        self.coord = coord
        self.height = height
        self.width = width
        self.length = length
        self.material = material
        self.color = color


class Chair(Furniture):
    pass


class Table(Furniture):
    pass


class Bed(Furniture):
    pass


class Toilet(Furniture):
    pass


class Device(Furniture):
    def __init__(self, coord, height, width, length, material, color, kw_per_hour, mode):
        super().__init__(coord, height, width, length, material, color)
        self.kw_per_hour = kw_per_hour
        self.mode = mode

    def turn_on(self):
        self.mode = True

    def turn_off(self):
        self.mode = False


class Refrigerator(Device):
    pass


class Oven(Device):
    pass


"""
def SaveToJson(data, file_path):
    file = open(file_path, 'w')
    file.write(json.dumps(data))
    file.close()


def LoadFrom(file_path):
    file = open(file_path, 'r')
    text = file.read()
    file.close()
    jsn = json.loads(text)
    print(jsn)
"""

def main():
    my_house = House('666 Svistunovo st.', 1, [
                     Kitchen([0, 0, 0], 200, 500, 500,
                             Windows([50, 30, 20], 150, 50, 'Wood', False),
                             Doors([50, 30, 20], 150, 50, 'Wood', False),
                             [Chair([50, 30, 20], 50, 30, 30, 'Plastic', 'Black'),
                              Chair([50, 30, 20], 50, 30, 30, 'Plastic', 'Black'),
                              Chair([50, 30, 20], 50, 30, 30, 'Plastic', 'Black'),
                              Table([50, 30, 20], 50, 30, 30, 'Wood', 'Brown'),
                              Refrigerator([50, 30, 20], 50, 30, 30, 'Metall', 'White', 500, False),
                              Oven([50, 30, 20], 50, 30, 30, 'Metall', 'Brown', 500, False)
                              ]),
                     Bedroom([0, 0, 0], 200, 500, 500,
                             Windows([50, 30, 20], 150, 50, 'Wood', False),
                             Doors([50, 30, 20], 150, 50, 'Wood', False),
                             Bed([50, 30, 20], 50, 30, 30, 'Wood', 'Black')),
                     Bathroom([0, 0, 0], 200, 500, 500, 0,
                               Doors([50, 30, 20], 150, 50, 'Wood', False),
                               Toilet([50, 30, 20], 50, 30, 30, 'Wood', 'Black'))
                     ])


if __name__ == '__main__':
    main()