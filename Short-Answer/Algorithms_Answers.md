#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) This algorithm would be O(n). n \* n \* n in the while loop, but a gets updated with n \* n --> n

b) This algorithm would be O(n log n)(base 2). while loop is log n (base 2) because j \*= 2, and the range is n. --> n log n

c) This algorithm would be O(n). Even though it's a recursive call, there is n operations.

## Exercise II

Binary Search. Look for the middle value for n floor. If the eggs break, then take the middle value of 0 to (high-low) / 2 - 1. If the eggs didn't break, then you have to do the same process with the upper segment, which is (high-low) / 2 + 1 to n. Repeat the process till you find f.

Runtime complexity for binary search is log n.
