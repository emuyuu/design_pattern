# Builder Pattern
# 同じ引数を使って別の形をしたインスタンスを生成したいときに使用できる。
# 抽象基底クラスを継承するのがポイント。ここで共通で使用されるメソッドを定義する。
# 実際に成形処理を行うそのクラスを継承した具体的なクラス。

# 疑問：
# 抽象基底クラスを継承させなくても動作したのだが、このクラスはなぜ必要？
# 何を想定して用意してある？

import abc


def main():
    html = Director().construct(HTMLBuilder())
    text = Director().construct(TextBuilder())
    print(html)
    print("\n** ** ** ** ** ** ** ** **\n")
    print(text)


class Director:
    def construct(self, builder):
        all_str = ""
        all_str += builder.add_title("好きなお菓子ランキング")
        all_str += builder.add_ranking(["かっぱえびせん", "雪の宿", "揚一番"])
        all_str += builder.add_footer("ranking created by emuyuu")
        return all_str


class AbstractContentBuilder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add_title(self, title):
        pass

    @abc.abstractmethod
    def add_ranking(self, ranking):
        pass

    @abc.abstractmethod
    def add_footer(self, footer):
        pass


class HTMLBuilder(AbstractContentBuilder):

    def add_title(self, title):
        return "<h1>{}</h1>\n".format(title)

    def add_ranking(self, ranking):
        html_ranking_list = []
        for snack in ranking:
            html_ranking_list.append("<li>{}</li>\n".format(snack))
        ranking_list = "".join(html_ranking_list)
        return "<ol>\n{}</ol>\n".format(ranking_list)

    def add_footer(self, footer):
        return "<footer>{}</footer>".format(footer)


class TextBuilder(AbstractContentBuilder):

    def add_title(self, title):
        return "# {}\n".format(title)

    def add_ranking(self, ranking):
        md_ranking_list = []
        for snack in ranking:
            md_ranking_list.append("1. {}\n".format(snack))
        return "".join(md_ranking_list)

    def add_footer(self, footer):
        return footer


if __name__ == "__main__":
    main()
