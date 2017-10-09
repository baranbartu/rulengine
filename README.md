# rulengine
##### Simple Rule Engine for Python

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
Out[5]: True
```
