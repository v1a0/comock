from comock import mock


class DescartesCoordinate:
    def __init__(self, x: int | float = 0, y: int | float = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Car:
    def __init__(self, name: str, x: int | float = 0, y: int | float = 0):
        self.__name = name
        self.position = DescartesCoordinate(x=x, y=y)

    @mock.method(
        _return=4,
        _call=lambda i: print(f'hello {i}'),
        call_args=(3,),
        tags=['global', 'cool']
        # _raise=Exception("FuckOff")
    )
    # @mock.method
    def move(self, direction: str, distance: int | float):
        str_direction: str
        movement: int | float

        match direction:
            case 'r':
                str_direction = 'right'
                self.position.x += distance
            case 'l':
                str_direction = 'left'
                self.position.x -= distance
            case 'u':
                str_direction = 'up'
                self.position.y += distance
            case 'd':
                str_direction = 'down'
                self.position.y -= distance
            case _:
                raise Exception(
                    f'Unknown direction {direction}. Current position {self.position}'
                )

        return f"Car {self.name} moved {str_direction} to {distance} km"

    def get_info(self):
        return f"Current position of {self.name}: {self.position}"

    @property
    @mock.method
    def name(self):
        return self.__name


# MockObjTag('global').enable()
# mock.config.enable_global()
# mock.config.disable_global()
mock.config.enable_all_tags()

# print(mock.config.all_tags.pop())

car = Car("BMW")  # crate car named "BMW"
car.move('r', 10)  # move 10 km right
car.move('l', 5)  # move 5  km left
car.move('d', 10)  # move 10 km down

print(car.get_info())


