# Stubs for networkx.readwrite.pajek (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def generate_pajek(G: Any) -> None: ...
def write_pajek(G: Any, path: Any, encoding: str = ...) -> None: ...
def read_pajek(path: Any, encoding: str = ...): ...
def parse_pajek(lines: Any): ...
