import sys

from richs.console import Console
from richs.rule import Rule

try:
    text = sys.argv[1]
except IndexError:
    text = "Hello, World"

LineCharacters_List = [
    "&",
    "#",
    "$",
    "%",
    "*",
    "=",
]

# set_LineCharacters는 라인 문자를 내가 원하는 문자로 선택할 수 있게 해줌
rule = Rule(title=text)
console = Console()
console.print(rule)

for item in LineCharacters_List:
    print("\n")
    rule.set_LineCharacters(item)
    rule.style = "yellow"
    console.print(rule)
