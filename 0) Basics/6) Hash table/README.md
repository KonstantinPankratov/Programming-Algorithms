## Hash table

1. Hash table is the union of a hash function with an array.
2. Good hash tables minimize collisions.
3. Hash tables provide very fast search, insertion and deletion.

###### Execution time

| Average case | Worst case |
| --- | --- |
| O(1) | O(n) |

###### Fill factor

The fill factor in the hash tables is a ratio of the number of filled elements in the hash table to the total number of elements.

> Hash table elements / Total

**Example**

Hash table has 5 elements and only 3 are filled

| Hash table ||||||
| --- | --- | --- | --- | --- | --- |
| Empty | 21 | 67 | Empty | 83 |

Fill factor of this hash table is 3/5