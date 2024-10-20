from typing import List
from tree_sitter import Node

def sort_nodes_list(nodes: List[Node]) -> List[Node]:
    return sorted(nodes, key=lambda node: node.start_point.row)