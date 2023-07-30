from typing import Iterable, List, Optional

from . import box
from .console import ConsoleOptions
from .style import StyleType
from .console import Console, RenderableType
from .table import Table

class RStack(List[RenderableType]):
        @property
        def top(self):
            """Get top of stack."""
            return self[-1]

        def push(self, item: RenderableType):
            """Push an item on to the stack (append in stack nomenclature)."""
            self.append(item)

        def pop(self):
            value = self[-1]
            del self[-1]
            return value

        def take_out(self):
            reversecopy = self[:]
            reversecopy.reverse()
            return reversecopy

class RendStack:
    #그냥 스택하나 만들고

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
        show_pop=True,
        show_push=True,
        show_numbering=False
    ):
        self.stack = RStack()
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
        self.show_pop = show_pop
        self.show_push = show_push
        self.show_numbering = show_numbering 

    def push(self, item):
        if self.show_push:
            console = Console()
            table=Table(
                show_header=False, 
                show_edge=self.show_edge, 
                box=box.HEAVY_HEAD, 
                title=self.title,
                title_style=self.title_style,
                style=self.style,
                row_styles=self.row_styles,
                border_style=self.border_style,
                expand=True,
                padding=self.padding,
                collapse_padding=self.collapse_padding,
                highlight=self.highlight,
            )
            if self.show_numbering:
                if len(self.stack)==0:
                    table.add_column(justify='center',vertical='middle',ratio=1)
                    table.add_row(" ")
                    table.add_section()
                else:
                    table.add_column(justify='center',vertical='middle',ratio=1)
                    table.add_column(justify=self.justify, ratio=99)
                    number=len(self.stack)
                    for rederable in self.stack.take_out():
                        table.add_row(f'{number}',rederable)
                        table.add_section()
                        number -= 1
            else:
                table.add_column(justify=self.justify)
                for rederable in self.stack.take_out():
                    table.add_row(rederable)
                    table.add_section()

            table2 = Table(show_header=False,show_edge=True)
            table2.add_column(justify='center')
            table2.add_row(item)
            table2.add_row('[green]push[/green]:red_triangle_pointed_down:')
            table2.add_row(table)
            console.print(table2)

        self.stack.push(item)

    def top(self):
        return self.stack.top()

    def pop(self):
        if self.show_pop:
            value=self.stack.pop()
            console = Console()
            table=Table(
                show_header=False, 
                show_edge=self.show_edge, 
                box=box.HEAVY_HEAD, 
                title=self.title,
                title_style=self.title_style,
                style=self.style,
                row_styles=self.row_styles,
                border_style=self.border_style,
                expand=True,
                padding=self.padding,
                collapse_padding=self.collapse_padding,
                highlight=self.highlight,
            )
            
            if self.show_numbering:
                if len(self.stack)==0:
                    table.add_column(justify='center',vertical='middle',ratio=1)
                    table.add_row(" ")
                    table.add_section()
                else:
                    table.add_column(justify='center',vertical='middle',ratio=1)
                    table.add_column(justify=self.justify, ratio=99)
                    number=len(self.stack)
                    for rederable in self.stack.take_out():
                        table.add_row(f'{number}',rederable)
                        table.add_section()
                        number -= 1
            else:
                table.add_column(justify=self.justify)
                for rederable in self.stack.take_out():
                    table.add_row(rederable)
                    table.add_section()
     
            table2 = Table(show_header=False,show_edge=True)
            table2.add_column(justify='center')
            table2.add_row(value)
            table2.add_row('[red]pop[/red]:red_triangle_pointed_up:')
            table2.add_row(table)
            console.print(table2)
            return value
        else:
            return self.stack.pop()

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
            padding=self.padding,
            collapse_padding=self.collapse_padding,
            highlight=self.highlight
        )
        if self.show_numbering:
            if len(self.stack)==0:
                    table.add_column(justify='center',vertical='middle',ratio=1)
                    table.add_row(" ")
                    table.add_section()
            else:
                table.add_column(justify='center',vertical='middle',ratio=1)
                table.add_column(justify=self.justify, ratio=99)
                number=len(self.stack)
                for rederable in self.stack.take_out():
                    table.add_row(f'{number}',rederable)
                    table.add_section()
                    number -= 1
            yield table
        else:
            table.add_column(justify=self.justify)
            for rederable in self.stack.take_out():
                table.add_row(rederable)
                table.add_section()
            yield table

