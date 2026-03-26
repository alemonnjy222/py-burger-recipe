from abc import abstractmethod, ABC


class Validator(ABC):
    def __set_name__(self, owner, name):
        self.protected_name = "_" + name

    def __get__(self, obj, objtype = None):
        return getattr(obj, self.protected_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.protected_name, value)

    @abstractmethod
    def validate(self, value):
        pass

class Number(Validator):
    def __init__(self, max_value: int, min_value: int):
        self.max_value = max_value
        self.min_value = min_value

    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError("Quantity should be integer.")
        if not value < self.min_value or value > self.max_value:
            raise ValueError(f"Quantity should not be less than {self.min_value} and greater than {self.max_value}.")


class OneOf(Validator):
    def __init__(self, options):
        self.options = options
    def validate(self, value):
        if value not in self.options:
            raise ValueError(f"Expected {value} to be one of {self.options}.")


class BurgerRecipe:

    def __init__(self, cheese: int, tomatoes: int, cutlets: int, eggs: int, buns:int, sauce: str):
        self.cheese = cheese
        self.tomatoes = tomatoes
        self.cutlets = cutlets
        self.eggs = eggs
        self.buns = buns
        self.sauce = sauce
