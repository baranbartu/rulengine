import six
import sys
import string
import StringIO
import contextlib
from collections import namedtuple

Rule = namedtuple('Rule', ('value', 'operator',
                           'comparison_value', 'data_structure'))


class Operator:
    EQUAL = 'equal'
    NOT_EQUAL = 'not_equal'
    LESS = 'less'
    GREATER = 'greater'
    LESS_EQUAL = 'less_equal'
    GREATER_EQUAL = 'greater_equal'
    IN = 'in'

    MAPPING = {
        EQUAL: '==',
        NOT_EQUAL: '!=',
        LESS: '<',
        GREATER: '>',
        LESS_EQUAL: '<=',
        GREATER_EQUAL: '>=',
        IN: 'in'
    }


class DataStructure:
    STRING = 'str'
    INTEGER = 'int'
    FLOAT = 'float'


class CodeGenerator(object):

    def initialize(self, tab='\t'):
        self.code = []
        self.tab = tab
        self.level = 0

    def end(self):
        return string.join(self.code, '')

    def write(self, string):
        self.code.append(self.tab * self.level + string + '\n')

    def indent(self):
        self.level = self.level + 1

    def dedent(self):
        if self.level == 0:
            raise SyntaxError('Unknown error in code generator')
        self.level = self.level - 1


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


if six.PY3:
    from importlib import import_module as _import_module
else:
    def _import_module(name):
        __import__(name)
        return sys.modules[name]


def _import_class(class_path):
    module_name, class_name = class_path.rsplit('.', 1)
    module = _import_module(module_name)
    return getattr(module, class_name)
