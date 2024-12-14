# Answers to Python Exercises

# Inheritance

def inheritance_exercise_1():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class Student(Person):
        def __init__(self, name, age, grades):
            super().__init__(name, age)
            self.grades = grades

        def average_grade(self):
            return sum(self.grades) / len(self.grades)

    return Student("John", 20, [90, 85, 88]).average_grade()

# Additional answers for exercises will follow the same pattern, with clear implementation
# for each exercise topic and difficulty level.

# Generators

def generator_exercise_21(n):
    def fibonacci():
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    return list(fibonacci())

# Iterators

def iterator_exercise_41():
    class FibonacciIterator:
        def __init__(self, n):
            self.n = n
            self.a, self.b = 0, 1
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.index >= self.n:
                raise StopIteration
            self.index += 1
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            return result

    return list(FibonacciIterator(10))

# List Comprehensions

def list_comprehension_exercise_61():
    n = 10
    return [x ** 2 for x in range(1, n + 1)]

# Decorators

def decorator_exercise_81():
    def log_function_call(func):
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
            return func(*args, **kwargs)
        return wrapper

    @log_function_call
    def add(a, b):
        return a + b

    return add(2, 3)

# Multithreading

def multithreading_exercise_101():
    import threading

    def compute_square(n):
        print(f"Square of {n} is {n ** 2}")

    threads = []
    for i in range(5):
        thread = threading.Thread(target=compute_square, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Multiprocessing

def multiprocessing_exercise_121():
    from multiprocessing import Pool

    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)

    with Pool(4) as pool:
        results = pool.map(factorial, [5, 6, 7, 8])
    return results

# Ensure additional answers are implemented for all exercises.

if __name__ == "__main__":
    print("Inheritance Exercise 1:", inheritance_exercise_1())
    print("Generator Exercise 21:", generator_exercise_21(10))
    print("Iterator Exercise 41:", iterator_exercise_41())
    print("List Comprehension Exercise 61:", list_comprehension_exercise_61())
    print("Decorator Exercise 81:", decorator_exercise_81())
    print("Multithreading Exercise 101:")
    multithreading_exercise_101()
    print("Multiprocessing Exercise 121:", multiprocessing_exercise_121())