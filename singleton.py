# singletonとは：
# そのクラスのインスタンスは必ず１つであることを保証する
# 参考：http://www.denzow.me/entry/2018/01/28/171416

# クラスメソッドとは（参考：https://blog.pyq.jp/entry/Python_kaiketsu_190205）
# 通常、メソッドはクラスをインスタンスにしないと呼び出せないが、
# クラスメソッドはクラスから直接呼び出すことができる
# （→ 雑に言うとクラス内で使用できる関数として使えたりもする）

# クラス関数、スタティック関数についてこれがわかりやすかった：
# https://djangobrothers.com/blogs/class_instance_staticmethod_classmethod_difference/


class Singleton:
    _instance = None

    # 通常の方法でインスタンス作成をできなくする
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("this is singleton")

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls.__internal_new__()

        return cls._instance


def main():
    # error_test = Singleton()
    a = Singleton.get_instance()
    b = Singleton.get_instance()
    print(a)
    print(b)
    print(a == b)


if __name__ == "__main__":
    main()
