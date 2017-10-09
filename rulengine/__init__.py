from rulengine.conditions import execute_condition

VERSION = (0, 0, 4)
__version__ = '.'.join(map(str, VERSION))


def execute(rules):
    result = False
    for rule in rules:
        result = execute_condition(rule)
        if result:
            break
    return result
