# Python Asynchronous Comprehension

## Description

This project is focused on learning about asynchronous comprehensions in Python. We will use the `asyncio` and `random` modules to create generators and coroutines. We will also learn how to use run
`asyncio` tasks in parallel and measure their execution time.

## Learning Objectives

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Tasks

### **[0. Async Generator](./0-async_generator.py)**

Write a coroutine called `async_generator` that takes no arguments. The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10.

### **[1. Async Comprehensions](./1-async_comprehension.py)**

We will write a coroutine called `async_comprehension` that takes no arguments. The coroutine will collect 10 random numbers using an async comprehensing over `async_generator`, then return the 10 random numbers.

### **[2. Run time for four parallel comprehensions](./2-measure_runtime.py)**

We write a function called `measure_runtime` that will execute `async_comprehension` four times in parallel using `asyncio.gather`. The function should measure the total runtime and return it.

## Resources

- [PEP 530](https://peps.python.org/pep-0530/)
- [Python Asyn generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)
- [Type-annotating generators](https://stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3)
- [asyncio - Asynchronous I/O in Python](https://realpython.com/async-io-python/#the-asyncio-package-and-asyncawait)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)
- [Python asyncio Module](https://docs.python.org/3/library/asyncio.html)

## Authors

- **Andrew Maina** - [Andrew-Maina](https://github.com/KingMaina)