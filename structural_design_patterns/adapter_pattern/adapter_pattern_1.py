# adapter patternとは
# アダプター。
# 本来そのインスタンスでは使うことのできないメソッドを呼び出すことができるようにする。

# adapter patternにもいろいろあるみたいだ


class Dog:
    def __init__(self):
        self.name = 'Dog'

    def bark(self):
        return 'woof!!!'


class Cat:
    def __init__(self):
        self.name = 'Cat'

    def meow(self):
        return 'meow!!!'


class Human:
    def __init__(self):
        self.name = 'Human'

    def speak(self):
        return 'hi!!!'


class Car:
    def __init__(self):
        self.name = 'Car'

    def make_noise(self, octane_level):
        return 'vrooom{}'.format('!' * octane_level)


class Adapter:
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    # object.__getattr__(self, name)：
    # デフォルトの属性アクセスがAttruteError失敗したとき
    # （nameがインスタンスの属性またはselfのクラスツリーの属性でないために
    # __getattribute__()がAttributeErrorを出したか、
    # nameプロパティの__get__()がAttributeErrorを出したとき）に呼び出される。
    def __getattr__(self, attr):
        # attr == 'name'なので、自身のname(self.name)をgetして、それを返す
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__


def main():
    dog = Dog()
    adapted_dog = Adapter(dog, make_noise=dog.bark)
    print(f'original dict dog: {adapted_dog.original_dict()}')
    print(f'adapted dict: {adapted_dog.__dict__}')
    # {'obj': <__main__.Dog object at 0x000001A1B0228908>,
    #  'make_noise': <bound method Dog.bark of <__main__.Dog object at 0x000001A1B0228908>>}
    # ↑ `make_noise`メソッドが`Dog.bark`と紐づけられている
    print(f'self.name: {adapted_dog.name}')
    print(adapted_dog.make_noise())
    print('-------------------------------')

    cat = Cat()
    adapted_cat = Adapter(cat, make_noise=cat.meow)
    print(f'adapted dict cat: {adapted_cat.__dict__}')
    # {'obj': <__main__.Cat object at 0x000002BC461C8A20>,
    #  'make_noise': <bound method Cat.meow of <__main__.Cat object at 0x000002BC461C8A20>>}
    print(adapted_cat.make_noise())

    print('-------------------------------')

    objects = []

    human = Human()
    objects.append(Adapter(human, make_noise=human.speak()))

    car = Car()
    objects.append(Adapter(car, make_noise=car.make_noise(10)))

    for obj in objects:
        print('A {} goes {}'.format(obj.name, obj.make_noise))


if __name__ == "__main__":
    main()
