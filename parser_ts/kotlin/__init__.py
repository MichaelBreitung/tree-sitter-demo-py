from tree_sitter import Parser

from .kotlin_class import KotlinClass
from .language import KOTLIN_LANGUAGE


parser = Parser(KOTLIN_LANGUAGE)


def get_kotlin_class(code: str, class_name: str) -> KotlinClass:
    tree = parser.parse(code.encode(encoding="utf8"))

    return KotlinClass(tree, class_name)
