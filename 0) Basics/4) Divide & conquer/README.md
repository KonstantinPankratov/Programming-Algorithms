## Divide & conquer

This is a programming algorithm:
1. Divide a difficult task into simple subtasks
2. Conquer the simple subtasks to solve the main

###### Explanation using sum.py
**Divide**

Define the simplest case

```python
    # if an array is empty, then the sum is 0
    if len(array) == 0:
        return 0
    
    # if an array has only 1 element, then the sum is equal to this element
    elif len(array) == 1:
        return array[0]
```

**Conquer**

Reduce the problem to the simplest case

```python
    # bring current array to the array in the simplest case with 1 element
    array[0] + sum(array[1:])
```

> Recursion saves its state