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
In [1]: from rulengine.core import DataType, LogicalOperator, BitwiseOperator, Rule, Condition
In [2]: from rulengine import execute

In [3]: condition = Condition(value=1, bitwise_operator=BitwiseOperator.EQUAL, comparison_value=2, data_type=DataType.INTEGER) 
In [4]: rule =  Rule(logical_operator=LogicalOperator.AND, conditions=[condition])
In [5]: execute([rule])
Out[5]: False
```
