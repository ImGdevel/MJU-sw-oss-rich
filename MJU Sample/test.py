from contextlib import contextmanager

import time
from richs.live import Live


BEAT_TIME = 0.08
@contextmanager
def beat(length: int = 1) -> None:
    yield
    time.sleep(length * BEAT_TIME)


chart = Chart(title="2023년 대학 선호도 조사")
console = Console()


with Live(chart, console=console, screen=True, refresh_per_second=20):
    with beat(5):
        chart.add_data("서울대",30,"white")
    with beat(5):
        chart.add_data("고려대",40,"white")
    with beat(5):
        chart.add_data("연세대",60,"white")
    with beat(5):
        chart.add_data("서강대",53,"white")
    with beat(5):
        chart.add_data("한양대",46,"white")
    with beat(10):
        chart.add_data("명지대",74,"white")
    with beat(10):
        chart.title = (
            "[not italic]:smiley:[/] 2023년 대학 선호도 조사 [not italic]:smile:[/]"
        )
    with beat(10):
        chart.title = (
            "[not italic]:smile:[/] [green]2023년 대학 선호도 조사[/green] [not italic]:smile:[/]"
        )
    with beat(5):
        chart.change_color(0,"red")
    with beat(5):
        chart.change_color(1,"dark_orange")
    with beat(5):
        chart.change_color(2,"yellow")
    with beat(5):
        chart.change_color(3,"green")
    with beat(5):
        chart.change_color(4,"blue")
    with beat(5):
        chart.change_color(5,"purple")
    while(1):
        with beat(5):
            chart.change_color(1,"red")
            chart.change_color(2,"dark_orange")
            chart.change_color(3,"yellow")
            chart.change_color(4,"green")
            chart.change_color(5,"blue")
            chart.change_color(0,"purple")
        with beat(5):
            chart.change_color(2,"red")
            chart.change_color(3,"dark_orange")
            chart.change_color(4,"yellow")
            chart.change_color(5,"green")
            chart.change_color(0,"blue")
            chart.change_color(1,"purple")
        with beat(5):
            chart.change_color(3,"red")
            chart.change_color(4,"dark_orange")
            chart.change_color(5,"yellow")
            chart.change_color(0,"green")
            chart.change_color(1,"blue")
            chart.change_color(2,"purple")
            chart.border_style="yellow"
        with beat(5):
            chart.change_color(4,"red")
            chart.change_color(5,"dark_orange")
            chart.change_color(0,"yellow")
            chart.change_color(1,"green")
            chart.change_color(2,"blue")
            chart.change_color(3,"purple")
        with beat(5):
            chart.change_color(5,"red")
            chart.change_color(0,"dark_orange")
            chart.change_color(1,"yellow")
            chart.change_color(2,"green")
            chart.change_color(3,"blue")
            chart.change_color(4,"purple")
        with beat(5):
            chart.change_color(0,"red")
            chart.change_color(1,"dark_orange")
            chart.change_color(2,"yellow")
            chart.change_color(3,"green")
            chart.change_color(4,"blue")
            chart.change_color(5,"purple")
            chart.border_style="blue"
