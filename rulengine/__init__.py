from rulengine.conditions import make_condition

VERSION = (0, 0, 3)
__version__ = '.'.join(map(str, VERSION))


def execute(rules):
    conditions = generate_conditions(rules)
    return execute_conditions(conditions)


def generate_conditions(rules):
    conditions = []
    for rule in rules:
        cond = make_condition(rule)
        conditions.append(cond)
    return conditions


def execute_conditions(conditions):
    result = False
    for cond in conditions:
        # each cond is a lambda function that was prepared in conditions
        result = cond()
        if result:
            break
    return result
