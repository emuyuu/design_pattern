# using a class decorator to add properties

import numbers


def is_non_empty_str(name, value):
    if not isinstance(value, str):
        raise ValueError(f'{name}: title name must be string!!!')
    if not bool(value):
        raise ValueError('there must be title!!!!')


def is_in_range(minimum=None, maximum=None):
    assert minimum is not None or maximum is not None

    def is_in_range(name, value):
        if not isinstance(value, numbers.Number):
            raise ValueError('enter number please')
        if minimum is not None and value < minimum:
            raise ValueError('{}{} is too small'.format(name, value))
        if maximum is not None and value > maximum:
            raise ValueError('{}{} is too big'.format(name, value))

    return is_in_range


def do_ensure(cls):
    def make_property(name, attribute):
        privateName = '__' + name
        print(privateName)

        def getter(self):
            return getattr(self, privateName)

        def setter(self, value):
            attribute.validate(name, value)
            setattr(self, privateName, value)

        print(f'getter: {getter}')
        print(f'setter: {setter}')
        return property(getter, setter, doc=attribute.doc)

    for name, attribute in cls.__dict__.items():
        if isinstance(attribute, Ensure):
            setattr(cls, name, make_property(name, attribute))
    return cls


class Ensure:

    def __init__(self, validate, doc=None):
        self.validate = validate
        self.doc = doc


@do_ensure
class Book:
    title = Ensure(is_non_empty_str)
    price = Ensure(is_in_range(1, 10000))
    quantity = Ensure(is_in_range(0, 1000000))

    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    @property
    def value(self):
        return self.price * self.quantity

    def __repr__(self):
        return str(f'title: {self.title}, price: {self.price}, quantity: {self.quantity}')


akazukin = Book('赤ずきん', 300, 10)
print(f'run result: {akazukin}')
