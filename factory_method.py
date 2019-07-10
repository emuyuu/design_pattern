# いつ使うの？
# プログラムが実行されるまで、どのクラスがインスタンス化されるかわからないとき
# ファクトリークラスでどのオブジェクトを生成するのか判断してくれるため、プログラムを書く側は
# 条件分岐などは気にする必要がなくなる。

# when to use?
# when a method returns one of several possible classes that share a common super class

# 参考：
# https://www.youtube.com/watch?v=ub0DXaeV6hA
# https://github.com/Sean-Bradley/Design-Patterns-In-Python/tree/master/factory


import abc
import os


def main():
    input_house = input('どの家を作る？＜straw・brick＞{}'.format(os.linesep))
    house = HouseFactory(input_house).build_house()
    print(house.created_house_def())


class HouseFactory:
    def __init__(self, input_house):
        self.house_input = input_house

    def build_house(self):
        if self.house_input == "straw":
            return StrawHouse()
        elif self.house_input == "brick":
            return BrickHouse()
        else:
            print("その家は作れないな、、、")
            raise AssertionError


class AbstractHouse(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def created_house_def(self):
        pass


class StrawHouse(AbstractHouse):

    def __init__(self):
        self.wall = "straw"
        self.window_num = "3"
        self.door_shape = "round"

    def created_house_def(self):
        return "the {} house with {} windows and a {} door was created." \
            .format(self.wall, self.window_num, self.door_shape)


class BrickHouse(AbstractHouse):

    def __init__(self):
        self.wall = "brick"
        self.window_num = "6"
        self.door_shape = "rectangle"

    def created_house_def(self):
        return "the {} house with {} windows and a {} door was created." \
            .format(self.wall, self.window_num, self.door_shape)


if __name__ == "__main__":
    main()
