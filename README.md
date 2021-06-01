# YAPBWD - Yet Another Profiler But With Decorators
This Profiler uses decorators, so it is easy to use:

* Want to profile time of your program? No problem! Just add @YAPBWD.time_profiler
  

* Want see how much memory your program uses? Here you are: add @YAPBWD.memory_profiler

* This profiler also has clones of above decorators with many_ prefix. As it says, it runs the program many times and 
  says the average time or memory. 

Cannot understand? Here is a basic demonstration script for you!

```python
import YAPBWD

@YAPBWD.time_profiler
def main(some_arguments):
    return some_arguments + 1

if __name__ == '__main__':
    main(2)
```

After execution, you can see the time it takes to Python to add one to a number.
## Why you need it?

Well... I think time profiling is useful for everyone, but who will really know how much memory it requires 
doing something? I know that it is still useful for everybody who will write something like a math algorithm
to test it is works fine and there are no problems.

###### P.S: 
Don't try to use two decorators if you need to have accuracy measurements, because the result will be spoiled for a little.

Also, You shouldn't profile memory many times if you are having cache function like a lru_cache from functools.

Another thing, profiler decorators should be at the top of a decorators to work normally.