import time
from contextlib import contextmanager
from richs import box
from richs.align import Align
from richs.console import Console
from richs.live import Live
from richs.stack import RendStack
from richs.text import Text
from richs.chart import Chart
"""
This example shows how to display content in columns.

The data is pulled from https://randomuser.me
"""

import json
from urllib.request import urlopen

from richs.console import Console
from richs.columns import Columns
from richs.panel import Panel


def get_content(user):
    """Extract text from user dict."""
    country = user["location"]["country"]
    name = f"{user['name']['first']} {user['name']['last']}"
    return f"[b]{name}[/b]\n[yellow]{country}"




users = json.loads(urlopen("https://randomuser.me/api/?results=30").read())["results"]
user_renderables = [Panel(get_content(user), expand=True) for user in users]
#console.print(Columns(user_renderables))


console = Console()

BEAT_TIME = 0.05

@contextmanager
def beat(length: int = 1) -> None:
    yield
    time.sleep(length * BEAT_TIME)

stack = RendStack(show_push=False, show_pop=False)
# stack_centered = Align.center(stack)
stack_centered = stack
console.clear()


chart = Chart(title="Stack Element")
chart.add_data("A",15,"red")
chart.add_data("B",40,"blue")
chart.add_data("C",30,"green")






with Live(stack_centered, console=console, screen=True, refresh_per_second=20):
    with beat(10):
        stack.push('1번')
    with beat(10):
        stack.push('2번')
    with beat(10):
        stack.push('3번')
    with beat(10):
        stack.push('4번')
    with beat(10):
        stack.push('5번')
    with beat(10):
        stack.push('6번')
    with beat(10):
        stack.pop()
    with beat(10):
        stack.pop()
    with beat(10):
        stack.pop()
    with beat(6):
        stack.title = "T"
    with beat(6):
        stack.title = "Te"
    with beat(6):
        stack.title = "Tes"
    with beat(6):
        stack.title = "Test"
    with beat(10):
        stack.border_style = "yellow"
    with beat(10):
        stack.title_style = "bold blue"
    with beat(10):
        stack.show_numbering=True
    with beat(15):
        stack.push(user_renderables[0])
    with beat(15):
        stack.push(user_renderables[1])
    with beat(60):
        stack.push(chart)


