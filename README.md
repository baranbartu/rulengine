# rulengine
##### Simple Rule Engine for Python

# Installation
```bash
pip install rulengine
```

# Usage
```bash
In [37]: from rulengine.core import DataStructure, Operator, Rule
In [38]: from rulengine import execute

In [39]: rule = Rule(value=1, operator=Operator.EQUAL, comparison_value=1, data_structure=DataStructure.INTEGER)
In [40]: execute([rule])
Out[41]: True
```
