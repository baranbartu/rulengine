import six
import sys
from collections import namedtuple

Rule = namedtuple('Rule', ('value', 'operator',
                           'comparison_value', 'data_structure'))
Condition = namedtuple('Condition', ('value', 'func', 'comparison_value'))


class Operator:
    EQUAL = 'equal'
    NOT_EQUAL = 'not_equal'
    LESS = 'less'
    GREATER = 'greater'
    LESS_EQUAL = 'less_equal'
    GREATER_EQUAL = 'greater_equal'
    IN = 'in'
    IN_COMMA = 'in_comma'

    FUNC_MAPPING = {
        EQUAL: lambda x, y: x == y,
        NOT_EQUAL: lambda x, y: x != y,
        LESS: lambda x, y: x < y,
        GREATER: lambda x, y: x > y,
        LESS_EQUAL: lambda x, y: x <= y,
        GREATER_EQUAL: lambda x, y: x >= y,
        IN: lambda x, y: x in y,
        IN_COMMA: lambda x, y: x in y
    }


class DataStructure:
    STRING = 'str'
    INTEGER = 'int'
    FLOAT = 'float'
    DATE = 'date'


if six.PY3:
    from importlib import import_module as _import_module
else:
    def _import_module(name):
        __import__(name)
        return sys.modules[name]


def import_class(class_path):
    module_name, class_name = class_path.rsplit('.', 1)
    module = _import_module(module_name)
    return getattr(module, class_name)
