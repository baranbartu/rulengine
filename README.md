# rulengine
Simple Rule Engine for Python

```bash
In [37]: from rulengine.core import DataStructure, Operator, Rule

In [38]: from rulengine import execute

In [39]: rule
Out[39]: Rule(value=1, operator='equal', comparison_value=1, data_structure='int')

In [40]: execute([rule])
Out[40]: True

```
