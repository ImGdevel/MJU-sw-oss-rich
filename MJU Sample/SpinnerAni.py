from time import sleep
from richs.box import SQUARE, SIMPLE
from richs.columns import Columns
from richs.panel import Panel
from richs.live import Live

from richs._spinners import SPINNERS

from richs.text import Text
from richs.spinner import Spinner
from richs.console import Console
from richs.table import Table

BEAT_TIME = 0.05


console = Console()

among = Spinner('hyperamongus', text=Text(repr('amongus'), style="green"))
fall = Spinner('fallguys', text=Text(repr('soar'), style="green"))
mjumascot = Spinner('myongjimascot', text=Text(repr('amongus'), style="green"))
mjulogo = Spinner('myonjiLogo', text=Text(repr('soar'), style="green"))

dots = Spinner('dots',text=Text(repr('dots'), style="green"))
star = Spinner('star',text=Text(repr('star'), style="green"))
hamburger = Spinner('hamburger',text=Text(repr('hamburger'), style="green"))
balloon = Spinner('balloon',text=Text(repr('balloon'), style="green"))
bouncingBar = Spinner('bouncingBar',text=Text(repr('bouncingBar'), style="green"))
bouncingBall = Spinner('bouncingBall',text=Text(repr('bouncingBall'), style="green"))

table = Table(show_header=False, box=SIMPLE)
table.add_column()
table.add_column()
table.add_row(mjumascot, mjulogo)
table.add_row(among, fall)

with Live(table, console=console, screen=True, refresh_per_second=20):
    while True:
        sleep(0.1)
