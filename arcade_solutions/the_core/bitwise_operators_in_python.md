# Bitwise Operators in Python

## Bitwise XOR

Doesn't have a logical counterpart in python.


```python
def xor(a, b):
  return (a and not b) or (not a and b)

```

Evaluates two mutually exclusive conditions and tells you whether exactly one of them is met.


e.g. a person can either be a minor or an adult, but not both at the same time. Conversely, it's not possible for a person to be neither a minor nor an adult. The choice is mandatory


## Bitwise XOR


Performs logical negation on a given number by flipping all of its bits.

| Expression| Binary Value | Decimal Value |
| --------- | ------------ | --------------|
| a         | 10011100     | 156           |
| ~a        | 01100011     | 99            |


NB: Python doesn't support `unsigned integers` All numbers have an implicit sign attached to them


```python
>>> ~ 156
-157
>>> ~ 156 & 255
99
```


Todo
