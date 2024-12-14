# AdvancedPython
Training repo for python

# Python Exercises

This repository contains 100 exercises for practicing Python programming, focusing on the following topics:

- Inheritance
- Generators
- Iterators
- List Comprehensions
- Decorators
- Multithreading
- Multiprocessing

---

## Table of Contents

1. [Exercises](#exercises)
2. [Answers](#answers)

---

## Exercises

### Inheritance

#### Medium
1. Create a `Person` base class and a `Student` subclass that inherits from it. Add methods to compute a student's average grade.
2. Create a `Shape` class with a method `area`. Derive `Circle` and `Rectangle` classes and implement their specific areas.
3. Create a `Vehicle` class. Implement multiple inheritance with a `Car` and `Truck` class to simulate a hybrid vehicle.
4. Implement a `BankAccount` class with `withdraw` and `deposit` methods, then derive a `SavingsAccount` class with an additional interest calculation.
5. Build an `Employee` class and derive `Manager` and `Developer` subclasses. Add a method to calculate bonuses differently for each role.
6. Create a `Polygon` class and derive `Triangle` and `Square` classes, implementing perimeter and area methods.
7. Design an `Animal` class and derive `Dog` and `Cat` subclasses. Add behaviors like `bark` and `meow`.
8. Create a `Media` class for books and movies. Add methods for rating and categorization in derived classes.
9. Implement an `Account` base class and derive a `CheckingAccount` and `LoanAccount`. Add methods for overdraft and loan repayments.
10. Build a `Gadget` class and derive `Phone` and `Tablet` classes with unique specifications.

#### Hard
11. Build a `Tree` data structure class and implement binary tree traversal methods (inorder, preorder, postorder).
12. Implement a `Graph` class and create derived classes for directed and undirected graphs. Add methods for traversal.
13. Design a `Game` base class with a `play` method and derive `Chess` and `Checkers` classes with specific rules.
14. Create an `Order` class and derive `OnlineOrder` and `StoreOrder` classes. Add unique processing logic.
15. Implement a `Database` base class and derive `SQLDatabase` and `NoSQLDatabase` with query methods.
16. Build a `Robot` base class and derive `CleanerBot` and `SecurityBot`. Add task-specific methods.
17. Design a `SmartDevice` class and create subclasses like `SmartLight` and `SmartSpeaker`. Add features for automation.
18. Create a `Plant` class and derive `Flower` and `Tree` subclasses. Add methods for growth and reproduction.
19. Build a `Shape3D` class and derive `Sphere` and `Cube`. Implement volume and surface area methods.
20. Implement a `Currency` base class and derive `Dollar` and `Euro`. Add methods for conversion.

### Generators

#### Medium
21. Write a generator function `fibonacci` to yield the first `n` Fibonacci numbers.
22. Create a generator that yields all prime numbers up to a given number `n`.
23. Implement a generator that yields powers of 2 up to `2^n`.
24. Write a generator that simulates an infinite countdown from a given number.
25. Create a generator for yielding all even numbers in a list.
26. Build a generator to yield successive permutations of a string.
27. Implement a generator that yields random numbers between two bounds.
28. Write a generator that yields successive rows of Pascal's Triangle.
29. Create a generator that yields all palindromes in a list of strings.
30. Implement a generator that calculates cumulative sums in a list.

#### Hard
31. Write a generator that yields a spiral matrix traversal of a 2D list.
32. Create a generator that produces an infinite sequence of primes.
33. Build a generator that computes lazy Cartesian products of multiple lists.
34. Write a generator for an infinite arithmetic progression.
35. Implement a generator that yields consecutive pairs of items in a list.
36. Create a generator for flattening a nested list structure.
37. Write a generator for yielding combinations of elements in a list.
38. Build a generator that simulates dice rolls.
39. Implement a generator that yields the Mandelbrot sequence for visualization.
40. Create a generator for simulating random walks on a 2D grid.

### Iterators

#### Medium
41. Implement an iterator class for Fibonacci numbers.
42. Write an iterator for traversing a binary tree.
43. Create an iterator for iterating over subsets of a set.
44. Implement an iterator for infinite cyclic traversal of a list.
45. Build an iterator for reversing a string.
46. Write an iterator for chunking a list into smaller sublists.
47. Create an iterator for iterating through a matrix row by row.
48. Implement an iterator for flattening a nested dictionary.
49. Write an iterator for iterating through the diagonals of a 2D matrix.
50. Build an iterator for generating infinite prime numbers.

#### Hard
51. Implement a bidirectional iterator for a doubly linked list.
52. Write an iterator for generating all subsequences of a string.
53. Create an iterator for level-order traversal of a binary tree.
54. Build an iterator for zigzag traversal of a matrix.
55. Implement an iterator for generating partitions of an integer.
56. Write an iterator for a custom range that supports floating-point steps.
57. Create an iterator for iterating through a sparse matrix efficiently.
58. Build an iterator for permutations of a list.
59. Implement an iterator that generates all possible schedules for tasks.
60. Write an iterator for iterating through a trie data structure.

### List Comprehensions

#### Medium
61. Write a list comprehension to generate all squares of numbers up to `n`.
62. Create a list comprehension for filtering vowels from a string.
63. Implement a list comprehension for finding common elements between two lists.
64. Write a list comprehension to create a transpose of a 2D matrix.
65. Create a list comprehension for flattening a list of lists.
66. Implement a list comprehension to calculate factorial for numbers in a range.
67. Write a list comprehension for extracting all palindromes from a list of strings.
68. Create a list comprehension for generating a list of tuples with numbers and their cubes.
69. Implement a list comprehension for generating a list of prime numbers up to `n`.
70. Write a list comprehension to reverse strings in a list.

#### Hard
71. Implement a list comprehension for generating all Pythagorean triplets up to a number.
72. Write a list comprehension for filtering and sorting a list of dictionaries.
73. Create a list comprehension to simulate a game of life grid update.
74. Build a list comprehension for identifying anagrams in a list of words.
75. Implement a list comprehension for generating a multiplication table.
76. Write a list comprehension to implement a basic Caesar cipher.
77. Create a list comprehension for simulating random dice rolls.
78. Implement a list comprehension for generating all subsets of a set.
79. Write a list comprehension for counting character frequencies in a string.
80. Create a list comprehension for filtering out invalid email addresses from a list.

### Decorators

#### Medium
81. Write a decorator to log function calls and arguments.
82. Implement a decorator to cache the results of a function.
83. Create a decorator to measure the execution time of a function.
84. Write a decorator to limit the number of times a function can be called.
85. Implement a decorator for validating input arguments of a function.
86. Create a decorator to automatically retry a function on failure.
87. Write a decorator for converting function results into JSON format.
88. Implement a decorator to memoize results of recursive functions.
89. Create a decorator for enforcing user authentication in functions.
90. Write a decorator to ensure type consistency in function arguments.

#### Hard
91. Build a decorator to implement a rate limiter for API calls.
92. Write a decorator to monitor memory usage of a function.
93. Implement a decorator for creating a singleton class.
94. Create a decorator to profile CPU usage of a function.
95. Write a decorator for tracing nested function calls.
96. Implement a decorator to delay the execution of a function.
97. Create a decorator for injecting dependencies into functions.
98. Write a decorator for logging exceptions raised by a function.
99. Build a decorator to batch process function inputs.
100. Implement a decorator to enforce constraints on return values.

### Multithreading

#### Medium
101. Create a program to compute squares of a list of numbers using threads.
102. Implement a multithreaded server that handles multiple client requests.
103. Write a program to print even and odd numbers using two threads.
104. Create a thread pool for executing a set of tasks concurrently.
105. Build a multithreaded downloader for fetching multiple files simultaneously.
106. Write a program to simulate a producer-consumer problem using threads.
107. Implement a thread-safe counter with synchronization mechanisms.
108. Create a program to simulate concurrent reading and writing to a shared file.
109. Write a program to merge sorted subarrays using threads.
110. Build a multithreaded program to perform matrix multiplication.

#### Hard
111. Create a program to solve the dining philosophers problem using threads.
112. Implement a multithreaded program for parallel merge sort.
113. Build a thread-safe in-memory database with read-write locks.
114. Write a multithreaded program to simulate a ticket booking system.
115. Create a thread-safe logging mechanism for concurrent tasks.
116. Implement a program to simulate a concurrent crawler for web scraping.
117. Write a multithreaded chat server that supports multiple clients.
118. Build a thread pool that dynamically adjusts the number of threads based on workload.
119. Implement a concurrent word count program for multiple large text files.
120. Create a program to manage a thread-safe bounded queue.

### Multiprocessing

#### Medium
121. Create a program to compute factorials using multiple processes.
122. Implement a program to find prime numbers using multiprocessing.
123. Write a multiprocessing program for parallel matrix addition.
124. Build a multiprocessing solution to generate a list of random numbers concurrently.
125. Implement a program to sort large datasets using multiple processes.
126. Create a multiprocessing program to perform file compression.
127. Write a program to implement parallel prefix sum using processes.
128. Build a multiprocessing-based image processor for batch resizing.
129. Implement a program to calculate the average of large numbers in chunks using processes.
130. Create a multiprocessing program for parallel file search.

#### Hard
131. Implement a program to solve the N-Queens problem using multiprocessing.
132. Write a program to perform parallel quicksort using processes.
133. Create a multiprocessing-based server for handling client requests concurrently.
134. Implement a program to simulate a concurrent data pipeline using processes.
135. Build a multiprocessing solution to compute the Mandelbrot set.
136. Write a program to simulate distributed computing with processes.
137. Create a multiprocessing solution for parallel text analysis of multiple documents.
138. Implement a parallel graph traversal algorithm using processes.
139. Build a multiprocessing-based simulation of traffic flow in a network.
140. Write a program to perform parallel computation of matrix determinants using processes.

---

## Answers

The answers to these exercises are provided in the `answers.py` file. Each exercise has corresponding code and test cases for validation.
