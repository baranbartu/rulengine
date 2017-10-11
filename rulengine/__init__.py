from rulengine.core import RuleOperator
from rulengine.conditions import execute_condition

VERSION = (0, 0, 6)
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
        rule_operator_func = RuleOperator.FUNC_MAPPING[rule.operator]
    except KeyError:
        raise ValueError('Invalid rule operator.')
    return rule_operator_func(*condition_results)
