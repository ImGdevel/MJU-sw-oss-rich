from typing import  List ,Deque, Iterable, Optional

from richs.console import Console, RenderableType
from richs.console import ConsoleOptions
from richs.style import StyleType
from richs.table import Table
from rich import box
from richs.bar import Bar
from richs.text import Text

class ItemList(list):
    def __init__(self):
        self.maxvalue = 0

    @property
    def front(self):
        """Get top of queue."""
        return self[0]

    def push(self, bar, name, value):
        """Push an item on to the queue (append in queue nomenclature)."""
        if self.maxvalue < value:
            self.maxvalue = value
            # print(self.maxvalue)
            for (bar_, name_, value_) in self:
                # print(str(bar.size) + "->" + str(self.maxvalue))
                bar_.size = self.maxvalue
        data = (bar, name, value)
        self.append(data)
        

    def take_out(self):
        reversecopy = self[:]
        return reversecopy
        


class Chart:
    def __init__(  
        self, 
        justify = 'left',
        show_edge = True, 
        box=box.HEAVY_HEAD,
        title=None,
        title_style=None,
        style=None,
        row_styles: Optional[Iterable[StyleType]] = None,
        border_style: Optional[StyleType] = None,
        expand=False,
        padding=(0,1),
        collapse_padding=False,
        highlight=False,
    ):
        self.itemlist = ItemList()
        self.justify = justify
        self.show_edge = show_edge
        self.box = box
        self.title = title
        self.title_style = title_style
        self.style = style
        self.row_styles = row_styles
        self.border_style = border_style
        self.expand = expand
        self.padding = padding
        self.collapse_padding=collapse_padding
        self.highlight = highlight
        
    def add_data(
        self, name: str = "", value: int = 0, color: str = ""
    ):
        maxvalue = self.itemlist.maxvalue
        if maxvalue < value:
            maxvalue = value
        bar = Bar(size=maxvalue,begin=0,end=value,color=color)
        self.itemlist.push(bar,name,value)

    def change_color(self, index, color):
        bar, name, value = self.itemlist[index]
        changed_bar = Bar(size=self.itemlist.maxvalue,begin=0,end=value,color=color)
        self.itemlist[index] = (changed_bar,name,value)

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ):
        table=Table(
            show_header=False, 
            show_edge=self.show_edge, 
            box=self.box, 
            title=self.title,
            title_style=self.title_style,
            style=self.style,
            row_styles=self.row_styles,
            border_style=self.border_style,
            expand=self.expand,
            padding=(1,2),
            collapse_padding=self.collapse_padding,
            highlight=self.highlight,
        )
        

        table.add_column(justify='center',vertical='middle',ratio=1)
        table.add_column(justify='center',vertical='middle',ratio=1)

        for item in self.itemlist:
            bar, name, value = item
            table.add_row(name,bar,str(value))
            
        yield table
        
if __name__ == "__main__":  # pragma: no cover
    from contextlib import contextmanager
    import time
    from .live import Live


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
