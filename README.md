# rulengine
##### Simple Rule Engine for Python
##### Rule engine gives an approach to you: "it would valid, if one of the rules can provide necessarry condition"
##### You can use in your any project, but remember; you need to make your own data context and generate rules on your side

# Installation
```bash
pip install rulengine
```

# Usage
```bash
In [1]: from rulengine.core import DataType, RuleOperator, ConditionOperator, Rule, Condition
In [2]: from rulengine import execute

In [3]: condition = Condition(value=1, operator=ConditionOperator.EQUAL, comparison_value=2, data_type=DataType.INTEGER) 
In [4]: rule =  Rule(operator=RuleOperator.AND, conditions=[condition])
In [5]: execute([rule])
Out[5]: False
```
