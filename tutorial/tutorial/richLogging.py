# %%

from datetime import datetime
from rich.console import Console

class RL:
    def __init__(self, ):
        self.c = Console()
        self.LEVEL_DICT = {
            'info' : '[bold white on green] INFO [/bold white on green]',
            'error' : '[bold white on red] ERROR [/bold white on red]',
            'debug' : '[bold white on red] DEBUG [/bold white on red]',
            'warning' : '[bold white on #DDC061] WARNING [/bold white on #DDC061]'
            }

    def info(self, msg):
        def __name__():
            return 'info'
        self.c.print(f'[bold #9F7E90]{datetime.now().strftime("%m月%d日%H:%M")}|[/bold #9F7E90]', end = '')
        self.c.print(self.LEVEL_DICT[__name__().lower()], end=' ')
        self.c.print(msg)
        # print(dir(self))

    def error(self, msg):
        def __name__():
            return 'error'
        self.c.print(f'[bold #9F7E90]{datetime.now().strftime("%m月%d日%H:%M")}|[/bold #9F7E90]', end = '')
        self.c.print(self.LEVEL_DICT[__name__().lower()], end=' ')
        self.c.print(msg)

    def debug(self, msg):
        def __name__():
            return 'debug'
        self.c.print(f'[bold #9F7E90]{datetime.now().strftime("%m月%d日%H:%M")}|[/bold #9F7E90]', end = '')
        self.c.print(self.LEVEL_DICT[__name__().lower()], end=' ')
        self.c.print(msg)

    def warning(self, msg):
        def __name__():
            return 'warning'
        self.c.print(f'[bold #9F7E90]{datetime.now().strftime("%m月%d日%H:%M")}|[/bold #9F7E90]', end = '')
        self.c.print(self.LEVEL_DICT[__name__().lower()], end=' ')
        self.c.print(msg)

# rl = RL()
# 
# rl.info('hello')
# rl.debug('hello')
# rl.warning('hello')

