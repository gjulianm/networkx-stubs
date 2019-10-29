# Stubs for networkx.drawing.nx_agraph (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

import pygraphviz

from networkx.classes.graph import Graph


def from_agraph(A: Any, create_using: Optional[Any] = ...): ...
def to_agraph(N: Graph) -> pygraphviz.agraph.AGraph: ...
def write_dot(G: Any, path: Any) -> None: ...
def read_dot(path: Any): ...
def graphviz_layout(G: Any, prog: str = ..., root: Optional[Any] = ..., args: str = ...): ...
def pygraphviz_layout(G: Any, prog: str = ..., root: Optional[Any] = ..., args: str = ...): ...
def view_pygraphviz(G: Any, edgelabel: Optional[Any] = ..., prog: str = ..., args: str = ..., suffix: str = ..., path: Optional[Any] = ...): ...
