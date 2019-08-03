# class decorators

# getattr(object, name[, default]　とは：
# object の指名された属性の値を返します。name は文字列でなくてはなりません。
# 文字列がオブジェクトの属性の一つの名前であった場合、戻り値はその属性の値になります。
# 例えば、 getattr(x, 'foobar') は x.foobar と等価です。指名された属性が存在しない場合、 default が与えられていればそれが返され、
# そうでない場合には AttributeError が送出されます。

# setattr(object, name, value　とは：
# getattr() の相方です。引数はオブジェクト、文字列、それから任意の値です。
# 文字列は既存の属性または新たな属性の名前にできます。この関数は指定したオブジェクトが許せば、値を属性に関連付けます。
# 例えば、 setattr(x, 'foobar', 123) は x.foobar = 123 と等価です。

# 参考：https://docs.python.org/ja/3/library/functions.html

# あとでpropertyは実験したい
# https://www.headboost.jp/python-property/

# ↓本に書いてあるコード（少し変更）
# --------------------

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

    # なにをやっている？functionを返しているけれど、これはエラーにならないか確かめているということ？
    print(is_in_range)
    return is_in_range


# この関数なにやってるかわからないです
def ensure(name, validate):
    def decorator(cls):
        privateName = '__' + name

        def getter(self):
            print(cls)
            print(f'getattr: {getattr(self, privateName)}')
            return getattr(self, privateName)

        def setter(self, value):
            # ファクトリーパターンだ！！！！！
            validate(name, value)
            setattr(self, privateName, value)

        setattr(cls, name, property(getter, setter))
        return cls

    return decorator


@ensure('title', is_non_empty_str)
@ensure('price', is_in_range(1, 10000))
@ensure('quantity', is_in_range(1, 1000000))
class Book:

    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    @property
    def value(self):
        return self.price * self.quantity

    def __repr__(self):
        return str(f'title: {self.title}, price: {self.price}, quantity: {self.quantity}')


momotaro = Book('桃太郎', 500, 10)
print(momotaro)
