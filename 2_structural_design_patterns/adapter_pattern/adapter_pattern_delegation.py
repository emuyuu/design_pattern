# インスタンス委譲によるアダプター
# ----------------
# 正しくは"転送"らしい？？
# 引用：https://qiita.com/jesus_isao/items/4b6b7846ccf5eb46b1bc

# 転送とは：
# > 継承という言語としての機能を、継承を使わずに実装する方法
# （やってることは継承と同じ）

# ----------------
# 転送と継承の使い分け：
# 引用：https://ikenox.info/blog/inheritance-and-delegation-and-interface/

# > 子にとって親は単なるツールである場合は委譲を使うのが良い。継承してしまうと子が複数の責務を負うことになり、そのことによる不都合が生じる。
# > 逆に、子が親と同じ責務を持つべき場合には継承を使う。委譲を使うと、子が親と同じ能力を持っていないことによる不都合が生じる。

# ----------------
# 使いたいクラスのインスタンスを持っておいて、必要に応じてそこからメソッドを呼び出す。

from abc import ABCMeta, abstractmethod


class Banner:
    def __init__(self, string):
        self.__string = string

    def show_with_paren(self):
        print('({})'.format(self.__string))

    def show_with_aster(self):
        print('*{}*'.format(self.__string))


class Printer(metaclass=ABCMeta):

    @abstractmethod
    def print_weak(self):
        pass

    @abstractmethod
    def print_strong(self):
        pass


class PrinterBanner(Printer):
    def __init__(self, string):
        self.__banner = Banner(string)
        # print(vars(self.__banner))
        # -> {'_Banner__string': 'hello'}

    def print_weak(self):
        self.__banner.show_with_paren()

    def print_strong(self):
        self.__banner.show_with_aster()


def main():
    thing_to_print = PrinterBanner('hello')
    thing_to_print.print_weak()
    thing_to_print.print_strong()


if __name__ == '__main__':
    main()
