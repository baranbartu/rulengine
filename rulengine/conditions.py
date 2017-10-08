from core import _import_class, Operator


def make_condition(rule):
    """Get a condition instance for given operator and return condition code"""

    condition_method = 'conditions.c_{0}_{1}'.format(rule.data_structure,
                                                     rule.operator)
    try:
        func = _import_class(condition_method)
    except AttributeError:
        condition_method = 'conditions.c_{0}'.format(rule.data_structure)
        func = _import_class(condition_method)

    rule = prevalidate_rule(rule)

    return func(rule)


def prevalidate_rule(rule):
    try:
        real_operator = Operator.MAPPING[rule.operator]
    except KeyError:
        raise ValueError('Operator \'%s\' not supported.' % rule.operator)

    rule = rule._replace(operator=real_operator)
    return rule


def c_int(rule):
    return '%s %s %s' % (int(rule.value), rule.operator,
                         int(rule.comparison_value))


def c_int_in(rule):
    comparison_value = [int(_) for _ in rule.comparison_value.split(',')]
    return '%s %s %s' % (int(rule.value), rule.operator, comparison_value)


def c_float(rule):
    return '%s %s %s' % (float(rule.value), rule.operator,
                         float(rule.comparison_value))


def c_float_in(rule):
    comparison_value = [float(_) for _ in rule.comparison_value.split(',')]
    return '%s %s %s' % (float(rule.value), rule.operator, comparison_value)


def c_str(rule):
    return '%s %s %s' % ('\'%s\'' % rule.value, rule.operator,
                         str(rule.comparison_value))


def c_str_in(rule):
    comparison_value = [str(_) for _ in rule.comparison_value.split(',')]
    return '%s %s %s' % ('\'%s\'' % rule.value, rule.operator,
                         comparison_value)


def c_datetime(rule):
    raise NotImplementedError('Not implemented yet.')


def c_datetime_in(rule):
    raise NotImplementedError('Not implemented yet.')
