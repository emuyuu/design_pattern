# observer pattern
# > "監視対象(Subject)が変化した時に監視者(Observer)に通知する仕組み"

# 参考・引用：https://qiita.com/Algos/items/ba9c6ed52380b57aecac

# ---------------------------------------


class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach_observer(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers:
            observer.update()


class Button(Subject):
    def __init__(self):
        super().__init__()
        self._button_state = 0

    @property
    def button_state(self):
        return self._button_state

    @button_state.setter
    def button_state(self, state):
        if self._button_state != state:
            self._button_state = state
            self.notify()


class Observer1:
    @staticmethod
    def update():
        print('Observer1 notified! Button changed :D')


class Observer2:
    @staticmethod
    def update():
        print('Observer2 notified! Button changed :)')


if __name__ == '__main__':
    observer1 = Observer1()
    observer2 = Observer2()

    button = Button()
    button.add_observer(observer1)
    button.add_observer(observer2)

    print(f'▶ The button\'s state is {button.button_state}')
    button.button_state = 10
    print(f'▶ The button\'s state is {button.button_state}')

    print('---------------------------')

    print(f'▶ The button\'s state is {button.button_state}')
    print('~ detach observer1 ~')
    button.detach_observer(observer1)
    button.button_state = 20
    print(f'▶ The button\'s state is {button.button_state}')
