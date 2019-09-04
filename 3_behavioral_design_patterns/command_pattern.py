# command pattern
# 処理を「コマンド（＝文字列）」でよびだせるようにする

# 必要なクラス：
# Invoker（呼び出す人）...コマンドを呼び出す。
# Command Object...そのコマンドを実行（executeメソッドによって）することができる。
# Receiver（受ける人）...コマンドの中身。コマンドを受けて、その処理を実行する。

# 今回はこちらを参考にしました：
# https://github.com/Sean-Bradley/Design-Patterns-In-Python/blob/master/command/switch_command.py

# @propertyについて
# https://www.headboost.jp/python-property/
# --------------------------------------------------------

from abc import ABCMeta, abstractmethod
import time


class CommandInterface(metaclass=ABCMeta):
    """コマンドに必ず継承させる"""

    @abstractmethod
    def execute(self):
        pass


class Switch:
    """Invoker Class。コマンドを呼び出す。"""

    def __init__(self):
        self._commands = {}
        self._history = []

    @property
    # historyプロパティにはgetterメソッドしか書かないので、リードオンリーになる。
    # @propertyは@history.getterと同義
    def history(self):
        return self._history

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands.keys():
            self._history.append((time.time(), command_name))
            self._commands[command_name].execute()
        else:
            print('そのコマンドはないよ！')


class Light:
    """Reciever。コマンドの中身。コマンドを受け取ると、それが実行される。"""

    def turn_on(self):
        print('light turned ON')

    def turn_off(self):
        print('light turned OFF')


class SwitchOnCommand(CommandInterface):
    """Command object。Invokerにより呼び出されるコマンド。"""

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()


class SwitchOffCommand(CommandInterface):
    """Command object。Invokerにより呼び出されるコマンド。"""

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_off()


if __name__ == '__main__':
    LIGHT = Light()

    # コマンドの作成
    SWITCH_ON = SwitchOnCommand(LIGHT)
    SWITCH_OFF = SwitchOffCommand(LIGHT)

    # コマンドを呼び出せるようにする
    SWITCH = Switch()
    # command_name = 'ON', command = SWITCH_ON
    SWITCH.register('ON', SWITCH_ON)
    # command_name = 'OFF', command = SWITCH_OFF
    SWITCH.register('OFF', SWITCH_OFF)

    # コマンドの実行。
    SWITCH.execute('ON')
    time.sleep(1)
    SWITCH.execute('OFF')

    # ログを見ることもできよ！
    print(f'history: {SWITCH.history}')
