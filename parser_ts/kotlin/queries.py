from .language import KOTLIN_LANGUAGE

CLASS_QUERY = """
( 
  ( class_declaration 
    (identifier) @class_names (#eq? @class_names "{class_name}" )
  ) @class
)
"""

METHODS_QUERY = """
( class_declaration
  ( class_body
    ( function_declaration ) @methods 
  )
) 
"""
methods_query = KOTLIN_LANGUAGE.query(METHODS_QUERY)
