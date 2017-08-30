---
title: python3 Modules and Namespaces
date: 2017-01-15 16:34:54
tags:
- python
categories:
- Tech
- Note
- Code
---
Something about python3 modules and namespaces
<!-- more -->
Assignments do not copy data — they just bind names to objects. 
## Module
A module can contain executable statements as well as function definitions. These statements are intended to initialize the module. They are executed only the first time the module name is encountered in an import statement.
`from fibo import *` import all the namespaces in the module fibo
`from fibo import fib,fib1` import the namespace fib and fib1 in the module
`import fibo` import the module fibo, and should call the member functions in this way `fibo.fib(1000)`
### PATH
* current dir
* sys.path
`dir(fibo)` ['__name__', 'fib', 'fib2'] list all the names defined in the module
### PACKAGES 
An example hierarchy from the official documentation.

```python
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

```
`from sound.effects import echo`
`echofilter(input, output, delay=0.7, atten=4)`

add the '__all__' in the __init__.py
`__all__ = ["echo", "surround", "reverse"]`

## Namespaces
example in the official documentation
```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```
```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```
* the innermost scope, which is searched first, contains the local names
* the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
* the next-to-last scope contains the current module’s global names
* the outermost scope (searched last) is the namespace containing built-in names