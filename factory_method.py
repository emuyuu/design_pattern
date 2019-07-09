# いつ使うの？
# プログラムが実行されるまで、どのクラスがインスタンス化されるかわからないとき
# プログラム側が判断して、オブジェクトを生成してくれる。

# when to use?
# when a method returns one of several possible classes that share a common super class

# 参考：
# https://www.youtube.com/watch?v=ub0DXaeV6hA
# https://github.com/Sean-Bradley/Design-Patterns-In-Python/tree/master/factory

import abc
import os


class AbstractHouse(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def created_house(self):
        pass


class StrawHouse(AbstractHouse):

    def __init__(self):
        self.wall = "straw"
        self.window_num = "3"
        self.door_shape = "round"

    def created_house(self):
        return "the {} house with {} windows and a {} door was created." \
            .format(self.wall, self.window_num, self.door_shape)


class BrickHouse(AbstractHouse):

    def __init__(self):
        self.wall = "brick"
        self.window_num = "6"
        self.door_shape = "rectangle"

    def created_house(self):
        return "the {} house with {} windows and a {} door was created." \
            .format(self.wall, self.window_num, self.door_shape)


def main():
    house_input = input('どの家を作る？＜straw・brick＞{}'.format(os.linesep))
    if house_input == "straw":
        straw_house = StrawHouse()
        print(straw_house.created_house())
    elif house_input == "brick":
        brick_house = BrickHouse()
        print(brick_house.created_house())
    else:
        print("その家は作れないな、、、")


if __name__ == "__main__":
    main()
