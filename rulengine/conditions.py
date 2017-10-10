from rulengine.core import (import_class, get_date, BitwiseOperator,
                            ExecutableCondition)


def execute_condition(cond):
    """
    Get a rule instance for given operator and
    return condition lambda func
    """

    condition_method = 'rulengine.conditions.c_{0}_{1}'.format(
        cond.data_type, cond.bitwise_operator)
    try:
        func = import_class(condition_method)
    except AttributeError:
        condition_method = 'rulengine.conditions.c_{0}'.format(
            cond.data_type)
        func = import_class(condition_method)

    executable_cond = convert_condition_to_executable(cond)
    return func(executable_cond)


def convert_condition_to_executable(cond):
    try:
        func = BitwiseOperator.FUNC_MAPPING[cond.bitwise_operator]
    except KeyError:
        raise ValueError('Invalid bitwise operator.')

    executable_cond = ExecutableCondition(
        value=cond.value, func=func, comparison_value=cond.comparison_value)
    return executable_cond


def c_int(cond):
    return cond.func(int(cond.value), int(cond.comparison_value))


def c_int_in(cond):
    val = int(cond.value)
    return cond.func(val, [int(_) for _ in cond.comparison_value.split(',')])


def c_int_contains(cond):
    raise ValueError('Wrong usage')


def c_float(cond):
    return cond.func(float(cond.value), float(cond.comparison_value))


def c_float_in(cond):
    val = float(cond.value)
    return cond.func(val, [float(_) for _ in cond.comparison_value.split(',')])


def c_float_contains(cond):
    raise ValueError('Wrong usage')


def c_str(cond):
    return cond.func(str(cond.value), str(cond.comparison_value))


def c_str_in(cond):
    val = str(cond.value)
    return cond.func(val, [str(_) for _ in cond.comparison_value.split(',')])


def c_str_contains(cond):
    return c_str(cond)


def c_date(cond):
    return cond.func(get_date(cond.value), get_date(cond.comparison_value))


def c_date_in(cond):
    val = get_date(cond.value)
    return cond.func(
        val, [get_date(_) for _ in cond.comparison_value.split(',')])


def c_date_contains(cond):
    raise ValueError('Wrong usage')
