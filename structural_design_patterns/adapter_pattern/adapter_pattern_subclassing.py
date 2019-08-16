# 継承するタイプのAdapter Pattern

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


# Bannerを継承することで、PrinterBanner独自のメソッドで
# Bannerのメソッドが使えるようになる。
class PrinterBanner(Printer, Banner):
    def __init__(self, string):
        super().__init__(string)

    def print_weak(self):
        self.show_with_paren()

    def print_strong(self):
        self.show_with_aster()


def main():
    thing_to_print = PrinterBanner('hello')
    thing_to_print.print_weak()
    thing_to_print.print_strong()


if __name__ == '__main__':
    main()
