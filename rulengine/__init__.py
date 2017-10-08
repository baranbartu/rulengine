from rulengine.core import stdoutIO, CodeGenerator
from rulengine.conditions import make_condition

VERSION = (0, 0, 2)
__version__ = '.'.join(map(str, VERSION))


def execute(rules):
    code = generate_executable_code(rules)
    with stdoutIO() as s:
        exec code
    return bool(int(s.getvalue()))


def generate_executable_code(rules):
    c = CodeGenerator()
    c.initialize('    ')
    if_statement = 'if '
    for index, rule in enumerate(rules):
        cond = make_condition(rule)
        if_statement += cond
        if index < len(rules) - 1:
            if_statement += ' and '
    if_statement += ':'
    c.write(if_statement)
    c.indent()
    c.write('print 1')
    c.dedent()
    c.write('else:')
    c.indent()
    c.write('print 0')
    c.dedent()
    code = c.end()
    return code
