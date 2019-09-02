# using a class decorator instead of subclassing

# subclass:
# あるクラスを継承しているクラス。子クラス。


def mediated(cls):
    setattr(cls, 'mediator', None)

    def on_change(self):
        if self.mediator is not None:
            self.mediator.on_change(self)

    setattr(cls, 'on_change', on_change)
    return cls


@mediated
class Mediated:

    def __init__(self):
        self.mediator = None

    def on_change(self):
        if self.mediator is not None:
            self.mediator.on_change(self)

    def __repr__(self):
        return str(self.mediator)


test = Mediated()
print(test)