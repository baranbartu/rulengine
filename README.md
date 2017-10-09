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
In [1]: from rulengine.core import DataStructure, Operator, Rule
In [2]: from rulengine import execute

In [3]: rule = Rule(value=1, operator=Operator.EQUAL, comparison_value=1, data_structure=DataStructure.INTEGER)
In [4]: execute([rule])
Out[4]: True
```
