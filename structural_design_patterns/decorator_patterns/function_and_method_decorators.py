# デコレーター：
# 関数やクラス自体を引数としてとる。
# 元の関数やクラスを変更することなく、別の機能をつけることができる。（デコレーションを施すことができる的な）
# デコレーターが複数指定してある場合は、下から実行される

# --------------------

# function and method decorators


# 今回だとmean()が引数になる
def float_args_and_return(function):
    def wrapper(*args, **kwargs):
        # meanに与えられていた引数を一つ一つ操作できる
        # ここではstrからfloatに変更している
        args = [float(arg) for arg in args]
        # mean()を実行し、その結果を返す
        # 返り値もfloat型にする
        return float(function(*args, **kwargs))
    return wrapper


@float_args_and_return
def mean(first, second, *rest):
    numbers = (first, second) + rest
    return sum(numbers) / len(numbers)


def mean_without_decorator(first, second, *rest):
    numbers = (first, second) + rest
    try:
        return sum(numbers) / len(numbers)
    except TypeError:
        print('strは割れないです〜〜〜！')


print(mean(2, 10))
print(mean_without_decorator(2, "10"))
