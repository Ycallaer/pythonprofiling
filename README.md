## Python profiler Example ##

## Goal of the repo ##
We will give an example on how you can do profiling on python code using the built-in cProfile package.
Visualisation of the result will be done using the package pyprof2calltree, which runs on qcachegrind.

## Explanation on the setup ##
We will increase all values in a list. We will do this by using 2 methods. First we will just loop over all values and increase by 1.
The second time we will use a list comprehension.

The goal is to show the difference in processing time and functions called

## Prerequisite ##
Before you can start coding you will need to install [qcachegrind](http://kcachegrind.sourceforge.net) with the graphical interface
If you are running on macos  run the following command:

```brew install qcachegrind --with-graphviz```


Next we can install the tool [pyprof2calltree](https://github.com/pwaller/pyprof2calltree/) which allows for the interpretation of the files
Installation can be done through pip install:
```pip install pyprof2calltree```

## Running the program ##
profile_tester.py is the main entry.
The reason there is no main function is that cProfile can not be wrapped in a function. If you do that it will be unable
to resolve imported functions. So if you want to adapt your own code make sure you do not create the main function and wrap
cProfile in a callable function

## Visualising the result ##
Once the code has been run you will have 2 files: first_iteration.cprof and second_iteration.cprof
To visualize the data run the following command:

```pyprof2calltree -k -i /profiler/second_iteration.cprof```


