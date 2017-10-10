from rulengine.core import LogicalOperator
from rulengine.conditions import execute_condition

VERSION = (0, 0, 5)
__version__ = '.'.join(map(str, VERSION))


def execute(rules):
    result = False
    for rule in rules:
        result = execute_rule(rule)
        if result:
            break
    return result


def execute_rule(rule):
    condition_results = [execute_condition(cond) for cond in rule.conditions]
    try:
        logical_operator_func = LogicalOperator.FUNC_MAPPING[
            rule.logical_operator]
    except KeyError:
        raise ValueError('Invalid logical operator.')
    return logical_operator_func(*condition_results)
