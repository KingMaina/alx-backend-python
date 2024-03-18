# Async I/O in Python 🕐🕕🕗

## Description

In this project, we explore the concept of asynchronous programming in Python. We will be using the `async` and `await` syntax to write asynchronous functions, and the `asyncio` module to execute them. We will also learn how to run concurrent coroutines, create asyncio tasks, and use the `random` module.

## Learning Objectives

- How to write an asynchronous function with async and await syntax
- How to execute an asynchronous function with asyncio
- How to run concurrent coroutines
- How to create asyncio tasks
- How to use the random module


## Tasks

### **[0-basic_async_syntax.py](./0-basic_async_syntax.py)**

We write an asynchronous function called `wait_random` that takes in an integer `max_delay` and returns a `float`. The function will wait for a random delay between 0 and `max_delay` (included and uniform) and eventually return it.

### **[1-concurrent_coroutines.py](./1-concurrent_coroutines.py)**

Here, we write a function called `wait_n` that takes in 2 int arguments (in this order): `n` and `max_delay`. The function will return a list of `floats` containing the `n` delays. The list of the delays will be in ascending order without using the `sort` method. This function will also use the `wait_random` function from the previous task.

### **[2-measure_runtime.py](./2-measure_runtime.py)**

We write a function called `measure_runtime` that will measure the total execution time for `wait_n(n, max_delay)`, and return total time / n.

### **[3-tasks.py](./3-tasks.py)**

We write a function called `task_wait_n` that takes in 2 int arguments (in this order): `n` and `max_delay`. The function creates and returns an asyncio task.

### **[4-tasks.py](4-tasks.py)**

We write a function called `task_wait_n` that takes in 2 int arguments (in this order): `n` and `max_delay`. The function creates asyncio tasks, and returns a list of the delays. The list of the delays will be in ascending order without using the `sort` method.


## Resources

- [asyncio - Asynchronous I/O in Python](https://realpython.com/async-io-python/#the-asyncio-package-and-asyncawait)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)
- [Python asyncio Module](https://docs.python.org/3/library/asyncio.html)

## Authors

- **Andrew Maina** - [Andrew-Maina](https://github.com/KingMaina)