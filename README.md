# Factor Finder
Finds optimum power factor of corresponding input in Regression

## Examples

### Example 1

#### code:

```python
from PowerFactorFinder import PowerFactorFinder

arr = [i for i in range(-10,11)]
out = [i**2 for i in arr]
obj = PowerFactorFinder(arr, out, 4)
print(obj.getPower(n = 3))
print(obj.getPowerList(n = 3))
```

#### output: 

```powershell
[2, 4, -2]
[(2, 1.0), (4, 0.961478955420308), (-2, -0.5279933204980993)]
```

first line of output consists the correlation with respect to power (default value of n is 1). 
second line of output consists power as well as correlation value (default value of n i n1).

### Example 2

#### code:

```python
from FactorFinder import FactorFinder
arr = [
       [1,2,3],
       [2,3,4],
       [3,4,5],
       [4,5,6]
]

out = [8,9,12,15]
obj = FactorFinder(arr,out,4)
print(obj.getPower(n = 2))
```

#### output:

```powershell
[[2, 3], [2, 3], [3, 2]]
```

the output consists power with respect to every column (default value of n in 1) (each nested list is a list of powers from higher to lower degree of correlation)
