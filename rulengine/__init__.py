from core import stdoutIO, CodeGenerator
from conditions import make_condition


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
