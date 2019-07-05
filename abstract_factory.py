# Abstract Factory Pattern
# インスタンス生成を専門とするファクトリーを用意する。
# この例の場合は、create_house()の処理に即する形でどのようなファクトリーを用意してもいい。
# それぞれのファクトリーの中で、そのファミリー用にパラメーターとかを用意する。
# ファクトリー内で組み立てるから、生成するインスタンスにはどのような要素があるかとかが見やすい、、、のかも。
# あとファクトリーは追加しやすそう。ただファクトリーが増えた後だと、要素を増やすのは大変そう。
#
# 自作コード：
# 1. 藁でできた家と煉瓦でできた家をつくるよ！
# 2. 窓を作りたいな！窓の数はファクトリーによって違うよ！
# 3. ファクトリーは窓を作るクラスを呼び出してインスタンスを生成するよ！リターン！
# 4. ドアを作りたいな！ドアの数はファクトリーによって違うよ！
# 5. ファクトリーはドアを作るクラスを呼び出してインスタンスを生成するよ！リターン！
# 6. 窓の数、ドアの数を数えるて変数に入れるよ！
# 7. house変数にまとめるよ！終了！


def main():
    create_house(StrawHouseFactory())
    create_house(BrickHouseFactory())


def create_house(factory):
    window = factory.create_window()
    door = factory.create_door()
    house_type = factory.house_type
    window_num = window.num_of_window
    door_num = door.num_of_door
    house = '窓が{}個、ドアが{}個ある{}でできた家ができました！'.format(window_num, door_num, house_type)
    return print(house)


# abstract factoryであるけれど、concreteでもある。本に準拠。
class StrawHouseFactory:
    def __init__(self):
        self.num_of_window = None
        self.num_of_door = None
        self.house_type = "藁"

    @classmethod
    def create_window(cls, num_of_window=3):
        return cls.Window(num_of_window)

    @classmethod
    def create_door(cls, num_of_door=1):
        return cls.Door(num_of_door)

    class Window:
        def __init__(self, num_of_window):
            self.num_of_window = num_of_window

    class Door:
        def __init__(self, num_of_door):
            self.num_of_door = num_of_door


class BrickHouseFactory:
    def __init__(self):
        self.num_of_window = None
        self.num_of_door = None
        self.house_type = "煉瓦"

    @classmethod
    def create_window(cls, num_of_window=10):
        return cls.Window(num_of_window)

    def create_door(cls, num_of_door=2):
        return cls.Door(num_of_door)

    class Window:
        def __init__(self, num_of_window):
            self.num_of_window = num_of_window

    class Door:
        def __init__(self, num_of_door):
            self.num_of_door = num_of_door


if __name__ == "__main__":
    main()
