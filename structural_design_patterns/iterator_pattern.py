# iterate = 繰り返す

# Iterator：
# > Anything that is iterable can be iterated,
# > including dictionaries, lists, tuples, strings, streams, generators, and classes
# > for which you implement iterator syntax.
# 引用：http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

# -----------------------------------------
# object.__getitem__(self, key)：
# self[key] の値評価 (evaluation) を実現するために呼び出される。

# class Test():
#     def __getitem__(self, item):
#         if item in ['apple', 'banana', 'orange']:
#             return f'item is fruit'
#
# test = Test()
# print(test['apple'])
# -> item is fruit


# -----------------------------------------

class Numbers:
    def __init__(self):
        self.number_list = [num for num in range(0, 11)]


numbers = Numbers()
print('non iterable class object')
for i in numbers.number_list:
    print(i)


class IterNumbers:
    def __init__(self):
        self.number_list = [num for num in range(0, 11)]

    def __iter__(self):
        return iter(self.number_list)


iter_num = IterNumbers()
print('iterable class object')
for i in iter_num:
    print(i)
