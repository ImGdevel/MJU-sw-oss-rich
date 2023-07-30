import time
from contextlib import contextmanager
from richs import box
from richs.align import Align
from richs.console import Console
from richs.live import Live

from richs.stack import RendStack
from richs.text import Text
from richs.table import Table
"""
This example shows how to display content in columns.

The data is pulled from https://randomuser.me
"""

import json
from urllib.request import urlopen

from richs.console import Console
from richs.columns import Columns
from richs.panel import Panel



console = Console()

menu = Table(title="중국집 메뉴판")
menu.add_column(header="메뉴")
menu.add_column(header="가격")
menu.add_row("짜장면", "3500")
menu.add_row("짬뽕", "6000")
menu.add_row("제육덮밥", "6500")


stack = RendStack(
    show_push=True, show_pop=True, 
    title="Stack", title_style="bold blue", 
    show_numbering=True)
stack.push('1번')
stack.push('2번')
stack.push('3번')
stack.pop()
stack.pop()
stack.push(menu)
console.print(stack)