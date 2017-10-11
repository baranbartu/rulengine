import six
import sys
import datetime
from collections import namedtuple

Rule = namedtuple('Rule', ('operator', 'conditions'))
Condition = namedtuple('Condition', ('value', 'operator',
                                     'comparison_value', 'data_type'))
ExecutableCondition = namedtuple('ExecutableCondition', ('value',
                                                         'func',
                                                         'comparison_value'))


class ConditionOperator:
    EQUAL = 'equal'
    NOT_EQUAL = 'not_equal'
    LESS = 'less'
    GREATER = 'greater'
    LESS_EQUAL = 'less_equal'
    GREATER_EQUAL = 'greater_equal'
    IN = 'in'
    CONTAINS = 'contains'

    FUNC_MAPPING = {
        EQUAL: lambda x, y: x == y,
        NOT_EQUAL: lambda x, y: x != y,
        LESS: lambda x, y: x < y,
        GREATER: lambda x, y: x > y,
        LESS_EQUAL: lambda x, y: x <= y,
        GREATER_EQUAL: lambda x, y: x >= y,
        IN: lambda x, y: x in y,
        CONTAINS: lambda x, y: x in y,
    }


class RuleOperator:
    AND = 'and'
    OR = 'or'

    FUNC_MAPPING = {
        AND: lambda *args: all(_ for _ in args),
        OR: lambda *args: any(_ for _ in args)
    }


class DataType:
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


def get_date(value, date=True, format='%Y-%m-%d'):
    if isinstance(value, datetime.date):
        return value

    date_value = datetime.datetime.strptime(value, format)
    if date:
        return date_value.date()
    return date_value
