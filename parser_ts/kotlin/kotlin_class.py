from typing import List

from tree_sitter import Tree

from ..helpers import sort_nodes_list

from .language import KOTLIN_LANGUAGE
from .queries import CLASS_QUERY, methods_query


class KotlinClass:
    def __init__(self, tree: Tree, class_name: str):
        class_query = KOTLIN_LANGUAGE.query(CLASS_QUERY.format(class_name=class_name))

        class_captures = class_query.captures(tree.root_node)

        if not "class" in class_captures:
            raise Exception(f"No Class {class_name} in Source Tree")

        self.class_node = class_captures["class"][0]

    def get_methods(self) -> List[str]:
        methods: List[str] = []
        method_captures = methods_query.captures(self.class_node)

        if "methods" in method_captures:
            sorted_method_nodes = sort_nodes_list(method_captures["methods"])
            for method_node in sorted_method_nodes:
                methods.append(method_node.text.decode("utf8"))  # type: ignore

        return methods
